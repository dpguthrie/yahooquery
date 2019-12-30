import pytest
import pandas as pd
from yahooquery import Ticker


@pytest.fixture
def ticker():
    return Ticker('aapl')


@pytest.fixture
def mutual_fund():
    return Ticker('hasgx')


@pytest.fixture
def multiple_tickers():
    return Ticker(['aapl', 'msft', 'fb'])


def test_asset_profile(ticker):
    assert 'address1' in ticker.asset_profile['aapl']


def test_quote_not_found():
    ticker = Ticker('aaapl')
    assert "Quote not found" in ticker.income_statement()["aaapl"]
    tickers = Ticker(['aapl', 'aaapl'])
    assert len(tickers.income_statement().keys()) == 2
    assert "Quote not found" in tickers.income_statement()['aaapl']


def test_not_fund():
    ticker = Ticker('aapl')
    assert "No fundamentals data" in ticker.fund_profile['aapl']
    assert "No fundamentals data" in ticker.fund_performance['aapl']
    assert "No fundamentals data" in ticker.fund_holding_info['aapl']


def test_dicts(ticker, multiple_tickers):
    for attr in [
            'asset_profile', 'calendar_events', 'esg_scores', 'financial_data',
            'key_stats', 'major_holders', 'price', 'quote_type',
            'share_purchase_activity', 'summary_detail']:
        assert isinstance(getattr(ticker, attr), dict)
        assert isinstance(getattr(multiple_tickers, attr), dict)
        assert len(getattr(multiple_tickers, attr).keys()) == len(
            multiple_tickers.symbols)


def test_dataframe(ticker, multiple_tickers):
    for attr in [
            'company_officers', 'earning_history', 'grading_history',
            'insider_holders', 'insider_transactions', 'institution_ownership',
            'recommendation_trend', 'sec_filings']:
        assert isinstance(getattr(ticker, attr), pd.DataFrame)
        assert isinstance(getattr(multiple_tickers, attr), pd.DataFrame)
    for method in ['income_statement', 'balance_sheet', 'cash_flow']:
        assert isinstance(getattr(ticker, method)(), pd.DataFrame)
        assert isinstance(getattr(ticker, method)("q"), pd.DataFrame)
        assert isinstance(getattr(multiple_tickers, method)(), pd.DataFrame)
        assert isinstance(getattr(multiple_tickers, method)("q"), pd.DataFrame)
    assert isinstance(ticker.history(), pd.DataFrame)


def test_missing_symbol():
    with pytest.raises(TypeError):
        Ticker()
