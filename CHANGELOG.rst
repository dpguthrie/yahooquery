Change Log
==========

1.0.14
------
- Add asynchronous requests with the requests-futures library
- Add "events" to the history dataframe (dividends and splits)

1.0.13
------
- Add `adjclose` column to dataframe returned from `yahooquery.Ticker.history`

1.0.12
------
- Changed private Ticker variables (_ENDPOINTS, _PERIODS, and _INTERVALS) to public
- Updated README for new multiple endpoint methods as well as a comparison to yfinance
- Forced dictionary return when formatted = False.

1.0.11
------
- Bug fix related to accessing the multiple endpoint methods
  (get_endpoints, all_endpoints).  Error would occur during
  formatting, specifically for the earningsTrend endpoint
- Bug fix related to passing one endpoint to the get_endpoints
  method.

1.0.10
------
- Added docstrings to each property / method
- Changed get_multiple_endpoints method to get_endpoints
- Added all known endpoints into Ticker class.  Missing
  endpoints were earnings, earnings_trend, and index_trend

1.0.9
-----
- Removed combine_dataframes kwarg.  This is just the default behavior now.
- Removed ticker column in history method.  `symbol` is now part of
  a MultiIndex in the returned DataFrame

1.0.8
-----
- Updated option_chain method for bugs as well as MultiIndex indexing
  to allow the user an easier way to make cross-sections of the
  resulting data.

1.0.7
-----
- Made the symbols argument to the `Ticker` class a required argument
- Fixed bug related to the `fund_category_holdings` property.
- Fixed bug related to the `history` method.
- Added tests and initial attempt at Travis CI

1.0.6
-----
- Added frequency arguments to `balance_sheet`, `cash_flow`, and
  `income_statement` methods.  They will default to annual, but can
  return quarterly statements with "q" or "Q" arguments.
- Added a `calendar_events` property to the `Ticker` class.
  Shows next earnings date, previous dividend date, and other metrics.

1.0.5
-----
- Fixed bug related to formatting empty lists

1.0.4
-------
- Add `fund_performance` property to the `Ticker` class.  Shows
  historical fund performance as well as category performance.
