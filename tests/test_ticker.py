import pytest
import pandas as pd
from yahooquery import Ticker


def test_number_symbols():
    ticker = Ticker(['aapl', 'msft', 'fb'])
    assert len(ticker.symbols) == 3
    assert len(ticker.asset_profile.keys()) == 3


def test_asset_profile():
    ticker = Ticker('aapl')
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


def test_dataframe():
    ticker = Ticker('aapl')
    assert isinstance(ticker.history(), pd.DataFrame)
    ticker = Ticker('aaapl')
    assert isinstance(ticker.history(), dict)
    tickers = Ticker(['aapl', 'aaapl'])
    assert isinstance(tickers.history(), dict)
    assert isinstance(tickers.history()['aapl'], pd.DataFrame)
    tickers = Ticker(['aapl', 'fb'])
    assert isinstance(tickers.history(), pd.DataFrame)
    tickers.combine_dataframes = False
    assert isinstance(tickers.history(), dict)
    assert isinstance(tickers.history()['aapl'], pd.DataFrame)
    assert isinstance(tickers.history()['fb'], pd.DataFrame)


def test_missing_symbol():
    with pytest.raises(TypeError):
        Ticker()
