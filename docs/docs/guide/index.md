# Introduction

## Classes

The majority of the data available through the unofficial API can be obtained through the use of three classes:

- [Ticker](ticker/intro.md) - Retrieve company-specific data
- [Screener](screener.md) - Retrieve lists of stocks based on certain criteria
- [Research](research.md) - Retrieve proprietary research reports and trade ideas (**REQUIRES YAHOO FINANCE PREMIUM SUBSCRIPTION**).

Each class inherits functionality from a base class, `_YahooFinance`. As such, each class will accept the same [keyword arguments](keyword_arguments.md), which allows the user to make asynchronous requests, validate ticker symbols, retry failed requests, and much more.

## Functions

The functions below allow for additional data retrieval:

- [currency_converter](misc.md#currency_converter) - Retrieve current / historical conversion rate between two currencies
- [get_currencies](misc.md#get_currencies) - Retrieve list of currencies
- [get_exchanges](misc.md#get_exchanges) - Retrieve list of exchanges
- [get_market_summary](misc.md#get_market_summary) - Retrieve summary data relevant to a country
- [get_trending](misc.md#get_trending) - Retrieve trending securities relevant to a country
- [search](misc.md#search) - Query Yahoo Finance for anything
