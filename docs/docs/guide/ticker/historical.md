# Historical Prices

### **history**

=== "Details"

    - *Description*:  Retreives historical pricing data (OHLC) for given symbol(s)
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | period     | Length of time                           | `str`                        | `ytd`     | optional   | `['1d', '5d', '7d', '60d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']` |
    | interval   | Time between data points                 | `str`                        | `1d`        | optional   | `['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']` |
    | start      | Specific starting date to pull data from | `str` or `datetime.datetime` |           | optional   | If a string is passed, use the format `YYYY-MM-DD`                                                                                      |
    | end      | Specific ending date                     | `str` or `datetime.datetime` |           | optional   | If a string is passed, use the format `YYYY-MM-DD`
    | adj_timezone      | Adjust datetime to the specific symbol's timezone                     | `bool` | `True`       | optional   | `True`<br>`False`
    | adj_ohlc      | Calculates an adjusted open, high, low and close prices according to split and dividend information             | `bool` | `False`       | optional   | `True`<br>`False`
    | prepost | Include Pre and Post market data | `bool` | `False`       | optional   | `True`<br>`False`

    !!! tip "One Minute Interval Data"
        The Yahoo Finance API restricts the amount of one minute interval data to seven days per request.  However, the data availability extends to 30 days.  The following will allow the user to retrieve the last 30 days of one minute interval data, with the one caveat that **4 requests are made in 7 day ranges to retrieve the desired data**:

        ```python
        tickers = Ticker('fb aapl nflx', asynchronous=True)

        df = tickers.history(period='1mo', interval='1m')
        ```

        Thanks to [@rodrigobercini](https://github.com/rodrigobercini) for finding [this](https://github.com/dpguthrie/yahooquery/issues/32).
          

=== "Example"

    ```python
    tickers = Ticker('fb aapl nflx', asynchronous=True)
    
    # Default period = ytd, interval = 1d
    df = tickers.history()
    df.head()
    ```

=== "Data"

    |                                   |   high |      volume |   close |    low |   open |   adjclose |   dividends |
    |:----------------------------------|-------:|------------:|--------:|-------:|-------:|-----------:|------------:|
    | ('fb', datetime.date(2020, 1, 2)) | 209.79 | 1.20771e+07 |  209.78 | 206.27 | 206.75 |     209.78 |           0 |
    | ('fb', datetime.date(2020, 1, 3)) | 210.4  | 1.11884e+07 |  208.67 | 206.95 | 207.21 |     208.67 |           0 |
    | ('fb', datetime.date(2020, 1, 6)) | 212.78 | 1.70589e+07 |  212.6  | 206.52 | 206.7  |     212.6  |           0 |
    | ('fb', datetime.date(2020, 1, 7)) | 214.58 | 1.49124e+07 |  213.06 | 211.75 | 212.82 |     213.06 |           0 |
    | ('fb', datetime.date(2020, 1, 8)) | 216.24 | 1.3475e+07  |  215.22 | 212.61 | 213    |     215.22 |           0 |

    ![Chart](../../img/stock-chart.png "YTD Daily Data")