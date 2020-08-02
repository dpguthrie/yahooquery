# Ticker - Intro

## Import Ticker

```python
from yahooquery import Ticker
```

## Create Instance

To retrieve data from Yahoo Finance for a single stock, create an instance of the `Ticker` class by passing the company's ticker symbol as an argument:

```python
aapl = Ticker('aapl')
```

Or, pass in multiple symbols to retrieve data for multiple companies.  Symbols can be passed in as a list:

```python
symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']
tickers = Ticker(symbols)
```

They can also be passed in as a string:

```python
symbols = 'fb aapl amzn nflx goog'

tickers = Ticker(symbols)
```

!!! note
    Outside of a few properties / methods, each symbol will represent one request.

For example:

```python
from yahooquery import Ticker

symbols = 'fb aapl amzn nflx goog'

tickers = Ticker(symbols)

# Retrieve each company's profile information
data = tickers.asset_profile
```

By calling the `asset_profile` property on the `tickers` instance, we're making 5 separate calls to Yahoo Finance (determined by the number of symbols).
