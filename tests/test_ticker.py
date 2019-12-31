import pytest
import itertools
from yahooquery import Ticker


TICKERS = [
    Ticker('aapl'), Ticker(['aapl', 'msft']), Ticker(['aapl', 'aaapl']),
    Ticker('hasgx')
]

FINANCIALS = ['cash_flow', 'income_statement', 'balance_sheet']

SEPERATE_ENDPOINTS = FINANCIALS + [
    'option_chain', 'history', 'earnings_trend', 'params',
    'get_multiple_endpoints', 'option_expiration_dates']


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_' and i not in SEPERATE_ENDPOINTS]


@pytest.fixture(params=TICKERS)
def ticker(request):
    return request.param


# def test_option_chain(ticker):
#     assert ticker.option_chain is not None

def test_bad_multiple_endpoints_no_list(ticker):
    with pytest.raises(ValueError):
        assert ticker.get_multiple_endpoints("assetProfile summaryProfile")


def test_bad_multiple_endpoints_wrong(ticker):
    with pytest.raises(ValueError):
        assert ticker.get_multiple_endpoints(["asetProfile", "summaryProfile"])


def test_multiple_endpoints(ticker):
    assert ticker.get_multiple_endpoints(["assetProfile", "summaryProfile"]) is not None


@pytest.mark.parametrize("endpoint", props(Ticker))
def test_endpoints(ticker, endpoint):
    assert getattr(ticker, endpoint) is not None


@pytest.mark.parametrize("endpoint, frequency", [
    el for el in itertools.product(FINANCIALS, ['q', 'a'])])
def test_financials(ticker, frequency, endpoint):
    assert getattr(ticker, endpoint)(frequency) is not None


@pytest.mark.parametrize("period, interval", [
    (p, i) for p, i in zip([
        '1d', '5d', '1y', '5y', 'max'], [
        '1m', '2m', '1d', '1wk', '3mo'])])
def test_history(ticker, period, interval):
    assert ticker.history(period, interval) is not None


@pytest.mark.parametrize("period, interval", [
    (p, i) for p, i in zip([
        '2d', '1mo'], [
        '1m', '3m'])])
def test_history_bad_args(ticker, period, interval):
    with pytest.raises(ValueError):
        assert ticker.history(period, interval)
