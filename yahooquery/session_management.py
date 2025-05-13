# stdlib
import logging
import random

# third party
from bs4 import BeautifulSoup
from curl_cffi import requests
from requests.exceptions import ConnectionError, RetryError, SSLError
from requests_futures.sessions import FuturesSession

# first party
from yahooquery.constants import BROWSERS

logger = logging.getLogger(__name__)


DEFAULT_TIMEOUT = 5
DEFAULT_SESSION_URL = "https://finance.yahoo.com"
CRUMB_FAILURE = (
    "Failed to obtain crumb.  Ability to retrieve data will be significantly limited."
)
DEFAULT_SETUP_RETRIES = 5


def get_crumb(session):
    try:
        response = session.get("https://query2.finance.yahoo.com/v1/test/getcrumb")

    except (ConnectionError, RetryError):
        logger.critical(CRUMB_FAILURE)
        # Cookies most likely not set in previous request
        return None

    if isinstance(session, FuturesSession):
        crumb = response.result().text
    else:
        crumb = response.text

    if crumb is None or crumb == "" or "<html>" in crumb:
        logger.critical(CRUMB_FAILURE)
        return None

    return crumb


def setup_session(session: requests.Session, url: str = None):
    url = url or DEFAULT_SESSION_URL
    try:
        response = session.get(url, allow_redirects=True)
    except SSLError:
        counter = 0
        while counter < DEFAULT_SETUP_RETRIES:
            try:
                response = session.get(url, verify=False)
                break
            except SSLError:
                counter += 1

    if isinstance(session, FuturesSession):
        response = response.result()

    # check for and handle consent page:w
    if response.url.find("consent") >= 0:
        logger.debug(f'Redirected to consent page: "{response.url}"')

        soup = BeautifulSoup(response.content, "html.parser")

        params = {}
        for param in ["csrfToken", "sessionId"]:
            try:
                params[param] = soup.find("input", attrs={"name": param})["value"]
            except Exception as exc:
                logger.critical(
                    f'Failed to find or extract "{param}" from response. Exception={exc}'
                )
                return session

        logger.debug(f"params: {params}")

        response = session.post(
            "https://consent.yahoo.com/v2/collectConsent",
            data={
                "agree": ["agree", "agree"],
                "consentUUID": "default",
                "sessionId": params["sessionId"],
                "csrfToken": params["csrfToken"],
                "originalDoneUrl": url,
                "namespace": "yahoo",
            },
        )

    return session


def initialize_session(session=None, **kwargs):
    if session is None:
        max_workers = kwargs.pop("max_workers", 8)
        is_async = kwargs.pop("asynchronous", False)
        impersonate = random.choice(list(BROWSERS.keys()))
        headers = BROWSERS[impersonate]
        session = requests.Session(**kwargs, headers=headers, impersonate=impersonate)
        if is_async:
            session = FuturesSession(max_workers=max_workers, session=session)
        session = setup_session(session)
    return session
