from datetime import datetime
from typing import List

import pandas as pd
import requests

from .utils.countries import COUNTRIES
from .utils import _init_session


BASE_URL = "https://query2.finance.yahoo.com"


def _make_request(
    url, response_field=None, country=None, method="get", params={}, data=None, **kwargs
):
    if country:
        country = country.lower()
        try:
            params.update(COUNTRIES[country])
        except KeyError:
            raise KeyError(
                "{} is not a valid option.  Valid options include {}".format(
                    country, ", ".join(sorted(COUNTRIES.keys()))
                )
            )
    session = _init_session(**kwargs)
    r = getattr(session, method)(url, params=params, json=data)
    json = r.json()
    if response_field:
        try:
            return json[response_field]["result"]
        except (TypeError, KeyError):
            return json[response_field]
    return json


def search(
    query,
    country="United States",
    quotes_count=10,
    news_count=10,
    first_quote=False,
) -> dict:
    """Search Yahoo Finance for anything

    Parameters
    ----------
    query: str
        What to search for
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    quotes_count: int, default 10, optional
        Maximum amount of quotes to return
    news_count: int, default 0, optional
        Maximum amount of news items to return
    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": query, "quotes_count": quotes_count, "news_count": news_count}
    data = _make_request(url, country=country, params=params)
    if first_quote:
        return data["quotes"][0] if len(data["quotes"]) > 0 else data
    return data


def get_currencies():
    """Get a list of currencies"""
    url = "{}/v1/finance/currencies".format(BASE_URL)
    return _make_request(url, response_field="currencies", country="United States")


def get_exchanges():
    """Get a list of available exchanges and their suffixes"""
    url = "https://help.yahoo.com/kb/finance-for-web/SLN2310.html?impressions=true"
    dataframes = pd.read_html(url)
    return dataframes[0]


def get_market_summary(country="United States"):
    """Get a market summary

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.

    Returns
    -------

    """
    url = "{}/v6/finance/quote/marketSummary".format(BASE_URL)
    return _make_request(url, response_field="marketSummaryResponse", country=country)


def get_trending(country="United States"):
    """Get trending stocks for a specific region

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    """
    try:
        region = COUNTRIES[country.lower()]["region"]
    except KeyError:
        raise KeyError(
            "{} is not a valid option.  Valid options include {}".format(
                country, ", ".join(COUNTRIES.keys())
            )
        )
    url = "{}/v1/finance/trending/{}".format(BASE_URL, region)
    return _make_request(url, response_field="finance", country=country)[0]


def currency_converter(from_currency, to_currency, period="week"):
    """Currency conversion given two currencies

    Parameters
    ----------
    from_currency: str
        Currency to convert from, example: 'USD'
    to_currency: str
        Currency to convert to, example: 'EUR'
    period: str, default 'week', optional
        Amount of historical data to return
        Options: day, week, month, 6month, year, allTime

    Notes
    -----
    You can use the get_currencies function to view a list of currencies.  The
    'shortName' key for each currency is the one you would pass to from_currency or
    to_currency
    """
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "content-length": "79",
        "content-type": "application/json; charset=UTF-8",
        "host": "adsynth-ofx-quotewidget-prod.herokuapp.com",
        "origin": "https://widget-yahoo.ofx.com",
        "pragma": "no-cache",
        "referer": "https://widget-yahoo.ofx.com/",
        "sec-fetch-site": "cross-site",
    }
    payload = {
        "method": "spotRateHistory",
        "data": {"base": from_currency, "term": to_currency, "period": period},
    }
    url = "https://adsynth-ofx-quotewidget-prod.herokuapp.com/api/1"
    data = _make_request(
        url, response_field="data", data=payload, headers=headers, method="post"
    )
    if "HistoricalPoints" in data:
        data["HistoricalPoints"] = [
            dict(
                item,
                **{
                    "PointInTime": datetime.fromtimestamp(
                        item["PointInTime"] / 1000
                    ).strftime("%Y-%m-%d %H:%M:%S")
                }
            )
            for item in data["HistoricalPoints"]
        ]
    return data
