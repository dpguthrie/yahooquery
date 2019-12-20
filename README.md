# Yahooquery
[![CodeFactor](https://www.codefactor.io/repository/github/dpguthrie/yahooquery/badge/master?s=289f5ed067de511ac29b5e229c1a5ef5c8c1dc83)](https://www.codefactor.io/repository/github/dpguthrie/yahooquery/overview/master)

Python wrapper around an unofficial Yahoo Finance API.

## Install

```bash
pip install python
```

## Ticker

The `Ticker` module is the access point to the Yahoo Finance API.  Pass a ticker symbol to the `Ticker` class.

```python
from yahooquery import Ticker

aapl = Ticker('aapl')
```

Or pass a list of tickers.

```python
tickers = Ticker(['aapl', 'msft'])
```

## Data

Based on the data you'd like, the result will either be accessed through a `dict` or as a `pandas.DataFrame`.  Accessing data is incredibly easy and pythonic.

### Dictionaries

```python
aapl = Ticker('aapl')

# Asset Profile
aapl.asset_profile
{'aapl': {'address1': 'One Apple Park Way', 'city': 'Cupertino', ... }}

# ESG Scores
aapl.esg_scores
{'aapl': {'totalEsg': 72.27, 'environomentScore': 89.81, ... }}

# Financial Data
aapl.financial_data
{'aapl': {'currentPrice': 275.15, 'targetHighPrice': 342.4, ... }}

# Key Statistics
aapl.key_stats
{'aapl': {'priceHint': 2, 'enterpriseValue': 1230054359040, ... }}

# Price Information
aapl.price
{'aapl': {'preMarketChange': {}, 'preMarketPrice': {}, ... }}

# Quote Type
aapl.quote_type
{'aapl': {'exchange': 'NMS', 'quoteType': 'EQUITY', ... }}

# Share Purchase Activity
aapl.share_purchase_activity
{'aapl': {'period': '6m', 'buyInfoCount': 20, ... }}

# Summary Information
aapl.summary_detail
{'aapl': {'priceHint': 2, 'previousClose': 271.46, ... }}
aapl.summary_profile
{'aapl': {'address1': 'One Apple Park Way', 'city': 'Cupertino', ... }}
```

How about more than one ticker?

```python
# Pass a list of tickers to the Ticker class
tickers = Ticker(['aapl', 'msft'])

tickers.asset_profile
{'aapl': {'address1': 'One Apple Park Way', 'city': 'Cupertino', ... }, 'msft': {'address1': 'One Microsoft Way', 'city': 'Redmond', ... }}

tickers.esg_scores
{'aapl': {'totalEsg': 72.27, 'environomentScore': 89.81, ... }, 'msft': {'totalEsg': 74.8, 'environmentScore': 84.17, ... }}

tickers.financial_data
{'aapl': {'currentPrice': 275.15, 'targetHighPrice': 342.4, ... }, 'msft': {'currentPrice': 154.53, 'targetHighPrice': 174.0, ... }}

tickers.key_stats
{'aapl': {'priceHint': 2, 'enterpriseValue': 1230054359040, ... }, 'msft': {'priceHint': 2, 'enterpriseValue': 1127840350208, ... }}

tickers.price
{'aapl': {'preMarketChange': {}, 'preMarketPrice': {}, ... }, 'msft': {'preMarketChange': {}, 'preMarketPrice': {}, ... }}

tickers.quote_type
{'aapl': {'exchange': 'NMS', 'quoteType': 'EQUITY', ... }, 'msft': {'exchange': 'NMS', 'quoteType': 'EQUITY', ... }}

tickers.share_purchase_activity
{'aapl': {'period': '6m', 'buyInfoCount': 20, ... }, 'msft': {'period': '6m', 'buyInfoCount': 30, ... }}

tickers.summary_detail
{'aapl': {'priceHint': 2, 'previousClose': 271.46, ... }, 'msft': {'priceHint': 2, 'previousClose': 153.24, ... }}

tickers.summary_profile
{'aapl': {'address1': 'One Apple Park Way', 'city': 'Cupertino', ... }, 'msft': {'address1': 'One Microsoft Way', 'city': 'Redmond', ... }}

```

### Dataframes

```python
aapl.balance_sheet
aapl.cash_flow
aapl.company_officers
aapl.earning_history
aapl.grading_history
aapl.income_statement
aapl.insider_holders
aapl.insider_transactions
aapl.institution_ownership
aapl.recommendation_trend
aapl.sec_filings
aapl.fund_ownership
aapl.major_holders
aapl.earnings_trend
```

## Fund Specific

Mutual Funds have many of the accessors detailed above as well as the additional ones below:

```python
fund = Ticker('rpbax')

fund.fund_category_holdings  # pandas.DataFrame
fund.fund_bond_ratings  # pandas.DataFrame
fund.fund_sector_weightings  # pandas.DataFrame
fund.fund_performance  # dict
fund.fund_bond_holdings  # dict
fund.fund_equity_holdings  # dict
```

## Options

Retrieve option pricing for every expiration date for given ticker(s)

```python
aapl.option_chain  # returns pandas.DataFrame
```

## Historical Pricing

Historical price data can be retrieved for one or more tickers through the `history` method.

```python
aapl.history()
```

If no arguments are provided, as above, default values will be supplied for both `period` and `interval`, which are `ytd` and `1d`, respectively.  Additional arguments you can provide to the method are `start` and `end`.  Start and end dates can be either strings with a date format of `yyyy-mm-dd` or as a `datetime.datetime` object.

```python

aapl.history(period='max')
aapl.history(start='2019-05-01')  # Default end date is now
aapl.history(end='2018-12-31')  # Default start date is 1900-01-01

# Period options = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
# Interval options = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
```

If trying to retrieve more than one ticker, one dataframe will be returned and the column `ticker` can be used to identify each row appropriately.

```python
tickers = Ticker(['aapl', 'msft'])
tickers.history()
```
| dates               |   volume |    open |    low |   high |   close | ticker   |
|:--------------------|---------:|--------:|-------:|-------:|--------:|:---------|
| 2019-01-02 07:30:00 | 37039700 | 154.89  | 154.23 | 158.85 |  157.92 | AAPL     |
| 2019-01-03 07:30:00 | 91312200 | 143.98  | 142    | 145.72 |  142.19 | AAPL     |
| 2019-12-12 07:30:00 | 24612100 | 151.65  | 151.02 | 153.44 |  153.24 | MSFT     |
| 2019-12-13 14:00:01 | 23850062 | 153.003 | 152.85 | 154.89 |  154.53 | MSFT     |

## Multiple Endpoints

Access more than one endpoint in one call using the `get_multiple_endoints` method of the `Ticker` class.  This method **ONLY** returns dictionaries.

```python
aapl = Ticker('aapl')
endpoints = ['assetProfile', 'esgScores', 'incomeStatementHistory']
aapl.get_multiple_endpoints(endpoints)
{'aapl': {'assetProfile': {...}, 'esgScores', {...}, 'incomeStatementHistory', {...}}}
```

Type `Ticker._ENDPOINTS` to view the list of endpoints supported through this method.

