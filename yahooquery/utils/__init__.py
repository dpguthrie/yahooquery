import random
import re
import time
from datetime import datetime

import pandas as pd
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_futures.sessions import FuturesSession


DEFAULT_TIMEOUT = 5

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
]

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://finance.yahoo.com',
    'referer': 'https://finance.yahoo.com',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs['timeout']
            del kwargs['timeout']
        super(TimeoutHTTPAdapter, self).__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get('timeout')
        if timeout is None:
            kwargs['timeout'] = self.timeout
        return super(TimeoutHTTPAdapter, self).send(request, **kwargs)


def _init_session(session, **kwargs):
    session_headers = headers
    if session is None:
        if kwargs.get('asynchronous'):
            session = FuturesSession(max_workers=kwargs.get('max_workers', 8))
        else:
            session = Session()
        if kwargs.get('proxies'):
            session.proxies = kwargs.get('proxies')
        retries = Retry(
            total=kwargs.get('retry', 5),
            backoff_factor=kwargs.get('backoff_factor', .3),
            status_forcelist=kwargs.get(
                'status_forcelist', [429, 500, 502, 503, 504]),
            method_whitelist=['HEAD', 'GET', 'OPTIONS', 'POST', 'TRACE'])
        if kwargs.get('verify'):
            session.verify = kwargs.get('verify')
        session.mount('https://', TimeoutHTTPAdapter(
            max_retries=retries,
            timeout=kwargs.get('timeout', DEFAULT_TIMEOUT)))
        # TODO: Figure out how to utilize this within the validate_response
        # TODO: This will be a much better way of handling bad requests than
        # TODO: what I'm currently doing.
        # session.hooks['response'] = \
        #     [lambda response, *args, **kwargs: response.raise_for_status()]
        user_agent = kwargs.get('user_agent', random.choice(USER_AGENT_LIST))
        # if kwargs.get('cookies'):
        #     cookies = get_cookies(user_agent)
        #     [session.cookies.set(c['name'], c['value']) for c in cookies]
        #     session_headers.update({
        #         'cookie': '; '.join([
        #             item['name'] + "=" + item['value'] for item in cookies
        #         ])
        #     })
        session_headers['User-Agent'] = user_agent
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
    if isinstance(symbols, list):
        return symbols
    if comma_split:
        return [x.strip() for x in symbols.split(',')]
    return re.findall(r"[\w\-.=^&]+", symbols)


def _convert_to_timestamp(date=None, start=True):
    if date is None:
        date = int((-858880800 * start) + (time.time() * (not start)))
    elif isinstance(date, datetime):
        date = int(time.mktime(date.timetuple()))
    else:
        date = int(time.mktime(time.strptime(str(date), '%Y-%m-%d')))
    return date


def _history_dataframe(data, symbol, params, adj_timezone=True):
    df = pd.DataFrame(data[symbol]['indicators']['quote'][0])
    if data[symbol]['indicators'].get('adjclose'):
        df['adjclose'] = \
            data[symbol]['indicators']['adjclose'][0]['adjclose']
    df.index = pd.to_datetime(data[symbol]['timestamp'], unit='s') + \
        pd.Timedelta(
            (data[symbol]['meta']['gmtoffset'] * adj_timezone), 's')
    if params['interval'][-1] not in ['m', 'h']:
        df.index = df.index.date
    df.dropna(inplace=True)
    if data[symbol].get('events'):
        df = pd.merge(
            df, _events_to_dataframe(data, symbol, params, adj_timezone),
            how='left', left_index=True, right_index=True)
    return df


def _events_to_dataframe(data, symbol, params, adj_timezone):
    dataframes = []
    for event in ['dividends', 'splits']:
        try:
            df = pd.DataFrame(data[symbol]['events'][event].values())
            df.set_index('date', inplace=True)
            df.index = pd.to_datetime(df.index, unit='s') + \
                pd.Timedelta(
                    (data[symbol]['meta']['gmtoffset'] * adj_timezone), 's')
            if params['interval'][-1] not in ['m', 'h']:
                df.index = df.index.date
            if event == "dividends":
                df.rename(columns={'amount': 'dividends'}, inplace=True)
            else:
                df['splits'] = df['numerator'] / df['denominator']
                df = df[['splits']]
            dataframes.append(df)
        except KeyError:
            pass
    return pd.merge(
        dataframes[0], dataframes[1], how='left', left_index=True,
        right_index=True) if len(dataframes) > 1 else dataframes[0]
