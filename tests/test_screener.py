import pytest

from yahooquery import Screener


def test_screener():
    s = Screener()
    assert s.get_screeners('most_actives') is not None


def test_available_screeners():
    s = Screener()
    assert s.available_screeners is not None


def test_bad_screener():
    with pytest.raises(ValueError):
        s = Screener()
        assert s.get_screeners('most_active')
