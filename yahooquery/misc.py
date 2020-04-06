import requests
import pandas as pd


BASE_URL = 'https://query2.finance.yahoo.com'


def _make_request(url, response_field, **kwargs):
    params = {
        'lang': kwargs.get('lang', 'en-US'),
        'region': kwargs.get('region', 'US'),
        'corsDomain': kwargs.get('corsDomain', 'finance.yahoo.com')
    }
    r = requests.get(url, params=params)
    json = r.json()
    return json[response_field]['result']


def get_currencies():
    """Get a list of currencies
    """
    url = '{}/v1/finance/currencies'.format(BASE_URL)
    return _make_request(url, 'currencies')


def get_exchanges():
    """Get a list of available exchanges and their suffixes
    """
    url = 'https://help.yahoo.com/kb/finance-for-web/SLN2310.html?impressions=true'
    dataframes = pd.read_html(url)
    return dataframes[0]


def get_market_summary(**kwargs):
    """Get a market summary
    """
    url = '{}/v6/finance/quote/marketSummary'.format(BASE_URL)
    return _make_request(url, 'marketSummaryResponse', **kwargs)


def get_trending(region='US', **kwargs):
    """Get trending stocks for a specific region
    """
    url = '{}/v1/finance/trending/{}'.format(BASE_URL, region)
    return _make_request(url, 'finance')[0]
