# Options

### **option_chain**

=== "Details"

    - *Description*:  View option chain data for all expiration dates for a given symbol(s)
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python
    faang = Ticker('fb aapl amzn nflx goog')
    df = faang.option_chain
    df.head()
    ```

=== "Data"

    |                                                     | contractSymbol      |   strike | currency   |   lastPrice |   change |   percentChange |   volume |   openInterest |    bid |   ask | contractSize   | lastTradeDate       |   impliedVolatility | inTheMoney   |
    |:----------------------------------------------------|:--------------------|---------:|:-----------|------------:|---------:|----------------:|---------:|---------------:|-------:|------:|:---------------|:--------------------|--------------------:|:-------------|
    | ('aapl', Timestamp('2020-07-31 00:00:00'), 'calls') | AAPL200731C00170000 |      170 | USD        |      237.49 |    28.78 |         13.7895 |        1 |              4 | 239.8  | 244.1 | REGULAR        | 2020-07-31 13:32:22 |             9.42383 | True         |
    | ('aapl', Timestamp('2020-07-31 00:00:00'), 'calls') | AAPL200731C00175000 |      175 | USD        |      206.7  |     0    |          0      |        1 |              1 | 235.15 | 239.1 | REGULAR        | 2020-07-30 16:14:43 |             9.14454 | True         |
    | ('aapl', Timestamp('2020-07-31 00:00:00'), 'calls') | AAPL200731C00180000 |      180 | USD        |      191.6  |     0    |          0      |        0 |              1 | 229.8  | 234   | REGULAR        | 2020-07-23 18:23:16 |             8.78321 | True         |
    | ('aapl', Timestamp('2020-07-31 00:00:00'), 'calls') | AAPL200731C00185000 |      185 | USD        |      188.38 |     0    |          0      |        1 |              0 | 224.9  | 229.1 | REGULAR        | 2020-07-06 19:30:06 |             8.60938 | True         |
    | ('aapl', Timestamp('2020-07-31 00:00:00'), 'calls') | AAPL200731C00190000 |      190 | USD        |      173.7  |     0    |          0      |        0 |              1 | 178.4  | 182.9 | REGULAR        | 2020-06-24 13:58:56 |             1e-05   | True         |

=== "Filtering Examples"

    ```python
    faang = Ticker('fb aapl amzn nflx goog')
    df = faang.option_chain

    # The dataframe contains a MultiIndex
    df.index.names
    FrozenList(['symbol', 'expiration', 'optionType'])

    # Get specific expiration date for specified symbol
    df.loc['aapl', '2022-07-31']

    # Get specific option type for expiration date for specified symbol
    df.loc['aapl', '2022-07-31', 'calls']

    # Retrieve only calls for all symbols
    df.xs('calls', level=2)

    # Only include Apple in the money options
    df.loc[df['inTheMoney'] == True].xs('aapl')
    ```