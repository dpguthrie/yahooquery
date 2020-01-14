import requests
from requests_futures.sessions import FuturesSession
from datetime import datetime
import time


def _init_session(session):
    if session is None:
        session = requests.session()
        future_session = FuturesSession(session=session)
    return future_session


def _convert_to_timestamp(date=None, start=True):
    if date is None:
        date = int((-2208988800 * start) + (time.time() * (not start)))
    elif isinstance(date, datetime):
        date = int(time.mktime(date.timetuple()))
    else:
        date = int(time.mktime(time.strptime(str(date), '%Y-%m-%d')))
    return date
