import os
import pytest

from yahooquery import Research


RESEARCH = [
    Research(
        username=os.getenv('YF_USERNAME'), password=os.getenv('YF_PASSWORD'))
]


@pytest.fixture(params=RESEARCH)
def research(request):
    return request.param


def test_reports(research):
    assert research.reports() is not None


def test_reports_one_arg(research):
    assert research.reports(report_date='Last Week') is not None


def test_reports_multiple_filters(research):
    assert research.reports(
        investment_rating='Bearish,Bullish',
        report_date='Last Week',
        sector=['Basic Materials', 'Real Estate'],
        report_type='Analyst Report'
    ) is not None


def test_reports_bad_arg(research):
    with pytest.raises(ValueError):
        assert research.reports(investment_type='Bearish')


def test_reports_bad_option(research):
    with pytest.raises(ValueError):
        assert research.reports(report_type='Bad Report Type')


def test_reports_bad_multiple(research):
    with pytest.raises(ValueError):
        assert research.reports(report_date=['Last Week', 'Last Year'])


def test_trades(research):
    assert research.trades() is not None


def test_trades_size(research):
    assert research.trades(300) is not None
