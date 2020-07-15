from yahooquery import (get_currencies, get_exchanges, get_market_summary,
                        get_trending)


def test_get_currencies():
    assert get_currencies() is not None


def test_get_exchanges():
    assert get_exchanges() is not None


def test_get_market_summary():
    assert get_market_summary() is not None


def test_get_trending():
    assert get_trending() is not None
