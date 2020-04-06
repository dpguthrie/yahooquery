from datetime import datetime
import time
import pandas as pd
import re
from requests import Session
from requests_futures.sessions import FuturesSession


def _init_session(session, **kwargs):
    if session is None:
        if kwargs.get('asynchronous'):
            session = FuturesSession(max_workers=kwargs.get('max_workers', 8))
        else:
            session = Session()
        if kwargs.get('proxies'):
            session.proxies = kwargs.get('proxies')
    return session


def _flatten_list(ls):
    return [item for sublist in ls for item in sublist]


def _convert_to_list(symbols):
    if isinstance(symbols, list):
        return symbols
    else:
        return re.findall(r"[\w\-.=^]+", symbols)


def _convert_to_timestamp(date=None, start=True):
    if date is None:
        date = int((-2208988800 * start) + (time.time() * (not start)))
    elif isinstance(date, datetime):
        date = int(time.mktime(date.timetuple()))
    else:
        date = int(time.mktime(time.strptime(str(date), '%Y-%m-%d')))
    return date


def _history_dataframe(data, symbol):
    df = pd.DataFrame(data[symbol]['indicators']['quote'][0])
    if data[symbol]['indicators'].get('adjclose'):
        df['adjclose'] = \
            data[symbol]['indicators']['adjclose'][0]['adjclose']
    df.index = pd.to_datetime(data[symbol]['timestamp'], unit='s')
    if data[symbol].get('events'):
        df = pd.merge(
            df, _events_to_dataframe(data, symbol), how='left',
            left_index=True, right_index=True)
    return df


def _events_to_dataframe(data, symbol):
    dataframes = []
    for event in ['dividends', 'splits']:
        try:
            df = pd.DataFrame(data[symbol]['events'][event].values())
            df.set_index('date', inplace=True)
            df.index = pd.to_datetime(df.index, unit='s')
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
