# stdlib
import datetime
import logging
import random
import re

# third party
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError, RetryError, SSLError
from requests.packages.urllib3.util.retry import Retry
from requests_futures.sessions import FuturesSession
from urllib3.exceptions import MaxRetryError

logger = logging.getLogger(__name__)


DEFAULT_TIMEOUT = 5
DEFAULT_SESSION_URL = "https://finance.yahoo.com"
CRUMB_FAILURE = (
    "Failed to obtain crumb.  Ability to retrieve data will be significantly limited."
)

HEADERS = [
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,es;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,it;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1x",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="72", "Chromium";v="72", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="85", "Chromium";v="85", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,es;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,de;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,es;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,es;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,de;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="63", "Chromium";v="63", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="80", "Chromium";v="80", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,fr;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,de;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="70", "Chromium";v="70", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="80", "Chromium";v="80", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="80", "Chromium";v="80", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,es;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,it;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,de;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="85", "Chromium";v="85", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="55", "Chromium";v="55", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="85", "Chromium";v="85", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,it;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,it;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,de;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104", "Opera";v="90"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,fr;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="80", "Chromium";v="80", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,de;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="79", "Chromium";v="79", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,de;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="85", "Chromium";v="85", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9,de;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="88", "Chromium";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.6",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,de;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,it;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="85", "Chromium";v="85", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="73", "Chromium";v="73", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,es;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="90", "Chromium";v="90", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.9",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Microsoft Edge;v="86", "Chromium";v="86", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,fr;q=0.5",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-ch-ua": 'Microsoft Edge;v="84", "Chromium";v="84", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,fr;q=0.8",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="72", "Chromium";v="72", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,it;q=0.7",
    },
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-ch-ua": 'Google Chrome;v="81", "Chromium";v="81", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-site": "none",
        "sec-fetch-mod": "",
        "sec-fetch-user": "?1",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.7",
    },
]


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


def initialize_session(session=None, **kwargs):
    if session is None:
        if kwargs.get("asynchronous"):
            session = FuturesSession(max_workers=kwargs.get("max_workers", 8))
        else:
            session = requests.Session()
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
        session.headers = random.choice(HEADERS)
    return session


def setup_session(session: requests.Session, url: str = None):
    url = url or DEFAULT_SESSION_URL
    try:
        response = session.get(url, allow_redirects=True)
    except SSLError:
        counter = 0
        while counter < 5:
            try:
                session.headers = random.choice(HEADERS)
                response = session.get(url, verify=False)
                break
            except SSLError:
                counter += 1

    if isinstance(session, FuturesSession):
        response = response.result()

    # check for and handle consent page:w
    if response.url.find("consent"):
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
                return

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


def flatten_list(ls):
    return [item for sublist in ls for item in sublist]


def convert_to_list(symbols, comma_split=False):
    if isinstance(symbols, str):
        if comma_split:
            return [x.strip() for x in symbols.split(",")]
        else:
            return re.findall(r"[\w\-.=^&]+", symbols)
    return symbols


def convert_to_timestamp(date=None, start=True):
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
        last_trade = pd.Timestamp.fromtimestamp(timestamp, tz="UTC")
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
            d["numerator"] / d["denominator"] if d["denominator"] else float("inf")
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

    if "events" in data:
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
