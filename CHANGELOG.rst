Change Log
==========

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
