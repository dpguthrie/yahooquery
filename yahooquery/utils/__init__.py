import datetime
import random
import re

import pandas as pd
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_futures.sessions import FuturesSession


DEFAULT_TIMEOUT = 5

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
]

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://finance.yahoo.com",
    "referer": "https://finance.yahoo.com",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
}


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super(TimeoutHTTPAdapter, self).__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super(TimeoutHTTPAdapter, self).send(request, **kwargs)


def _init_session(session=None, **kwargs):
    session_headers = headers
    if session is None:
        if kwargs.get("asynchronous"):
            session = FuturesSession(max_workers=kwargs.get("max_workers", 8))
        else:
            session = Session()
        if kwargs.get("proxies"):
            session.proxies = kwargs.get("proxies")
        retries = Retry(
            total=kwargs.get("retry", 5),
            backoff_factor=kwargs.get("backoff_factor", 0.3),
            status_forcelist=kwargs.get("status_forcelist", [429, 500, 502, 503, 504]),
        )
        if kwargs.get("verify") is not None:
            session.verify = kwargs.get("verify")
        session.mount(
            "https://",
            TimeoutHTTPAdapter(
                max_retries=retries, timeout=kwargs.get("timeout", DEFAULT_TIMEOUT)
            ),
        )
        # TODO: Figure out how to utilize this within the validate_response
        # TODO: This will be a much better way of handling bad requests than
        # TODO: what I'm currently doing.
        # session.hooks['response'] = \
        #     [lambda response, *args, **kwargs: response.raise_for_status()]
        user_agent = kwargs.get("user_agent", random.choice(USER_AGENT_LIST))
        session_headers["User-Agent"] = user_agent
        if kwargs.get("headers") and isinstance(kwargs.get("headers"), dict):
            session_headers.update(**headers)
        session.headers.update(**session_headers)
    return session


# def get_cookies(user_agent):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--user-agent=' + user_agent)
#     options.add_argument('headless')
#     driver = webdriver.Chrome(
#         ChromeDriverManager().install(), chrome_options=options)
#     driver.get("https://finance.yahoo.com/screener/new")
#     cookies = driver.get_cookies()
#     driver.quit()
#     return cookies


def _flatten_list(ls):
    return [item for sublist in ls for item in sublist]


def _convert_to_list(symbols, comma_split=False):
    if isinstance(symbols, str):
        if comma_split:
            return [x.strip() for x in symbols.split(",")]
        else:
            return re.findall(r"[\w\-.=^&]+", symbols)
    return symbols


def _convert_to_timestamp(date=None, start=True):
    if date is not None:
        return int(pd.Timestamp(date).timestamp())
    if start:
        return int(pd.Timestamp("1942-01-01").timestamp())
    return int(pd.Timestamp.now().timestamp())


def _get_daily_index(data, index_utc, adj_timezone):
    # evalute if last indice represents a live interval
    timestamp = data["meta"]["regularMarketTime"]
    if timestamp is None:
        # without last trade data unable to ascertain if there's a live indice
        has_live_indice = False
    else:
        last_trade = pd.Timestamp.fromtimestamp(timestamp)
        has_live_indice = index_utc[-1] >= last_trade - pd.Timedelta(2, "S")
    if has_live_indice:
        # remove it
        live_indice = index_utc[-1]
        index_utc = index_utc[:-1]
        ONE_DAY = datetime.timedelta(1)
        # evaluate if it should be put back later. If the close price for
        # the day is already included in the data, i.e. if the live indice
        # is simply duplicating data represented in the prior row, then the
        # following will evaluate to False (as live_indice will now be
        # within one day of the prior indice)
        keep_live_indice = index_utc.empty or live_indice > index_utc[-1] + ONE_DAY

    tz = data["meta"]["exchangeTimezoneName"]
    index_local = index_utc.tz_convert(tz)
    times = index_local.time

    bv = times <= datetime.time(14)
    if (bv).all() or data["meta"].get("exchangeName", "Nope") == "SAO":  # see issue 163
        index = index_local.floor("d", ambiguous=True)
    elif (~bv).all():
        index = index_local.ceil("d", ambiguous=True)
    else:
        # mix of open times pre and post 14:00.
        index1 = index_local[bv].floor("d", ambiguous=True)
        index2 = index_local[~bv].ceil("d", ambiguous=True)
        index = index1.union(index2)

    index = pd.Index(index.date)
    if has_live_indice and keep_live_indice:
        live_indice = live_indice.astimezone(tz) if adj_timezone else live_indice
        if not index.empty:
            index = index.insert(len(index), live_indice.to_pydatetime())
        else:
            index = pd.Index([live_indice.to_pydatetime()], dtype="object")
    return index


def _event_as_srs(event_data, event):
    index = pd.Index([int(v) for v in event_data.keys()], dtype="int64")
    if event == "dividends":
        values = [d["amount"] for d in event_data.values()]
    else:
        values = [
            d["numerator"] / d["denominator"] if d["denominator"] else float('inf')
            for d in event_data.values()
        ]
    return pd.Series(values, index=index)


def _history_dataframe(data, daily, adj_timezone=True):
    data_dict = data["indicators"]["quote"][0].copy()
    cols = [
        col for col in ("open", "high", "low", "close", "volume") if col in data_dict
    ]
    if "adjclose" in data["indicators"]:
        data_dict["adjclose"] = data["indicators"]["adjclose"][0]["adjclose"]
        cols.append("adjclose")

    if 'events' in data:
        for event, event_data in data["events"].items():
            if event not in ("dividends", "splits"):
                continue
            data_dict[event] = _event_as_srs(event_data, event)
            cols.append(event)

    df = pd.DataFrame(data_dict, index=data["timestamp"])  # align all on timestamps
    df.dropna(how="all", inplace=True)
    df = df[cols]  # determine column order

    index = pd.to_datetime(df.index, unit="s", utc=True)
    if daily and not df.empty:
        index = _get_daily_index(data, index, adj_timezone)
        if len(index) == len(df) - 1:
            # a live_indice was removed
            df = df.iloc[:-1]
    elif adj_timezone:
        tz = data["meta"]["exchangeTimezoneName"]
        index = index.tz_convert(tz)

    df.index = index
    return df
