import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _init_session(session):
    if session is None:
        session = requests.session()
    return session
