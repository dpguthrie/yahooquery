import pytest

from yahooquery import Ticker
from yahooquery.utils.countries import COUNTRIES


TICKERS = [
    Ticker('aapl', country='brazil')
]


@pytest.fixture(params=TICKERS)
def ticker(request):
    return request.param


def test_country_change(ticker):
    ticker.country = 'hong kong'
    assert ticker.country == 'hong kong'


def test_bad_country():
    with pytest.raises(ValueError):
        assert Ticker('aapl', country='china')


def test_default_query_param(ticker):
    assert ticker.default_query_params == \
        COUNTRIES[ticker.country]
