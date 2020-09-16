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


def get_symbol_search(company, region='US', lang='en-US'):
    """Uses the yahoo finance symbol lookup suggestions list.
    Takes the first suggestion. Returns None if none.
    """
    #urlbase = 'http://d.yimg.com/aq/autoc?query=%s&region=US&lang=en-US'
    urlbase = 'http://d.yimg.com/aq/autoc?query=%s&region=%s&lang=%s'
    # note as of September 2020:
    # This will error 400 if the region and lang params are missing. 
    # however it seems to give the same results regardless of what region and lang are set to
    # even if they are nonsense
    c = company.replace('.','').replace('~', '').replace(',', '').lower()
    #cq = urllib.parse.quote(c)
    cq = requests.utils.requote_uri(c)
    url = urlbase % (cq, region, lang)
    response = requests.get(url)
    responseJson = response.json()
    result = responseJson['ResultSet']['Result']
    if len(result):
        symbol = result[0]['symbol']
    else:
        symbol = None
    return symbol
