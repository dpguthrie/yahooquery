import pandas as pd
import requests

from .utils.countries import COUNTRIES


BASE_URL = 'https://query2.finance.yahoo.com'


def _make_request(url, response_field, country):
    country = country.lower()
    try:
        params = COUNTRIES[country]
    except KeyError:
        raise KeyError(
            "{} is not a valid option.  Valid options include {}".format(
                country,
                ', '.join(COUNTRIES.keys())
            ))
    r = requests.get(url, params=params)
    json = r.json()
    return json[response_field]['result']


def get_currencies():
    """Get a list of currencies
    """
    url = '{}/v1/finance/currencies'.format(BASE_URL)
    return _make_request(url, 'currencies', 'United States')


def get_exchanges():
    """Get a list of available exchanges and their suffixes
    """
    url = 'https://help.yahoo.com/kb/finance-for-web/SLN2310.html?impressions=true'
    dataframes = pd.read_html(url)
    return dataframes[0]


def get_market_summary(country='United States'):
    """Get a market summary
    """
    url = '{}/v6/finance/quote/marketSummary'.format(BASE_URL)
    return _make_request(url, 'marketSummaryResponse', country)


def get_trending(country='United States'):
    """Get trending stocks for a specific region
    """
    try:
        region = COUNTRIES[country.lower()]['region']
    except KeyError:
        raise KeyError(
            "{} is not a valid option.  Valid options include {}".format(
                country,
                ', '.join(COUNTRIES.keys())
            ))
    url = '{}/v1/finance/trending/{}'.format(BASE_URL, region)
    print(url)
    return _make_request(url, 'finance', country)[0]
