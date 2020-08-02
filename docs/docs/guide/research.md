
The Research class is the access point to retrieve either research reports or trade ideas from Yahoo Finance. **You must be a subscriber to Yahoo Finance Premium to utilize this class.**

## Import

```python
from yahooquery import Research
```

## Create Instance

```python
r = Research(username='username@yahoo.com', password=password)
```

## Research

### **reports**

=== "Details"

    - *Description*:  Retrieve research reports from Yahoo Finance
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | size  | Number of trades to return | `int`  | `100`       | optional   | |
    | investment_rating   | Type of investment rating |`str` or `list` | None   | optional   | See below     |
    | sector   | Sector | `str` or `list` | None   | optional   | See below     |
    | report_type   | Report types | `str` or `list` | None   | optional   | See below     |
    | report_date   | Date range | `str` | None   | optional   | See below     |

    === "trend"

        ```python
        {
            'options': ['Bearish', 'Bullish'],
            'multiple': True
        }
        ```

    === "sector"

        ```python
        {
            'options': [
                'Basic Materials', 'Communication Services', 'Consumer Cyclical',
                'Consumer Defensive', 'Energy', 'Financial Services', 'Healthcare',
                'Industrial', 'Real Estate', 'Technology', 'Utilities'],
            'multiple': True
        }
        ```

    === "report_type"

        ```python
        {
            'options': [
                'Analyst Report', 'Insider Activity', 'Market Outlook', 'Market Summary',
                'Market Update', 'Portfolio Ideas', 'Quantitative Report', 'Sector Watch',
                'Stock Picks', 'Technical Analysis', 'Thematic Portfolio', 'Top/Bottom Insider Activity'
            ],
            'multiple': True
        }
        ```

    === "report_date"

        ```python
        {
            'options': {
                'Last Week': 7,
                'Last Month': 30,
                'Last Year': 365
            },
            'multiple': False
        }
        ```
    
    !!! warning
        If using a `str` for the arguments that can either be a `str` or `list`, they have to be comma separated, i.e. `sector='Financial Services, Technology'`.

=== "Example"

    ```python hl_lines="2 3 4 5"
    r = Research(username='username@yahoo.com', password=password)
    r.reports(
        report_type='Analyst Report, Insider Activity',
        report_date='Last Week'
    )
    ```

=== "Data"

    |    | Report Date              | Report type    | Report title                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Tickers   | Sector                 | Rating     | Investment Rating   | Target Price   | Earnings Estimates   |
    |---:|:-------------------------|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|:-----------------------|:-----------|:--------------------|:---------------|:---------------------|
    |  0 | 2020-07-31T00:00:00.000Z | Analyst Report | CME Group is a futures and derivatives exchange and clearing company. It operates exchanges such as the Chicago Mercantile Exchange (CME), Chicago Board of Trade (CBOT), New York Mercantile Exchange (NYMEX), Commodity Exchange (COMEX) and the Kansas City Board of Trade (KCBT). In addition, CME offers a range of market data and information services. CME shares are a component of the S&P 500.                                                                        | ['CME']   | ['Financial Services'] | Maintained | Bullish             | Decreased      | Decreased            |
    |  1 | 2020-07-31T00:00:00.000Z | Analyst Report | Mastercard operates the world's second-largest electronic payments network, providing processing services and payment product platforms, including credit, debit, ATM, prepaid and commercial payments under the Mastercard, Maestro, and Cirrus brands. Mastercard went public in 2006 and is a member of the S&P 500.                                                                                                                                                          | ['MA']    | ['Financial Services'] | Maintained | Bullish             | Increased      | Decreased            |
    |  2 | 2020-07-31T00:00:00.000Z | Analyst Report | Blackstone Group is one of the world's leading managers of alternative assets, including private equity, real estate, hedge funds, credit-oriented funds, and closed-end mutual funds. In recent years, Blackstone has rapidly grown its fee-earning assets under management, and its assets are relatively well balanced among private equity, real estate, hedge funds, and credit. The company converted from a publicly traded partnership to a corporation on July 1, 2019. | ['BX']    | ['Financial Services'] | Maintained | Bullish             | Maintained     | Decreased            |
    |  3 | 2020-07-31T00:00:00.000Z | Analyst Report | Northrop Grumman is a leading global defense contractor, providing systems integration, defense electronics, information technology, and advanced aircraft and space technology. The shares are a component of the S&P 500. The company has 90,000 employees.                                                                                                                                                                                                                    | ['NOC']   | ['Industrials']        | Maintained | Bullish             | Maintained     | Increased            |
    |  4 | 2020-07-31T00:00:00.000Z | Analyst Report | Starbucks is a leading retailer of fresh-brewed coffee and branded merchandise. Its brands include Starbucks, Tazo Tea, and Frappuccino. With a market cap of more than $90 billion, SBUX shares are generally considered large-cap growth.                                                                                                                                                                                                                                      | ['SBUX']  | ['Consumer Cyclical']  | Maintained | Bullish             | Maintained     | Decreased            |


### **trades**

=== "Details"

    - *Description*:  Retrieve trade ideas from Yahoo Finance
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   |  Description  | Type   | Default   | Required   | Options                       |
    |:-----------|:-----------|:-------|:----------|:-----------|:------------------------------|
    | size  | Number of trades to return | `int`  | `100`       | optional   | |
    | trend   | Type of investment rating |`str` or `list` | None   | optional   | See below     |
    | sector   | Sector | `str` or `list` | None   | optional   | See below     |
    | term   | Term length (short, mid, long) | `str` or `list` | None   | optional   | See below     |
    | startdatetime   | Date range | `str` | None   | optional   | See below     |

    === "trend"

        ```python
        {
            'options': ['Bearish', 'Bullish'],
            'multiple': True
        }
        ```

    === "sector"

        ```python
        {
            'options': [
                'Basic Materials', 'Communication Services', 'Consumer Cyclical',
                'Consumer Defensive', 'Energy', 'Financial Services', 'Healthcare',
                'Industrial', 'Real Estate', 'Technology', 'Utilities'],
            'multiple': True
        }
        ```

    === "term"

        ```python
        {
            'options': ['Short term', 'Mid term', 'Long term'],
            'multiple': True
        }
        ```

    === "startdatetime"

        ```python
        {
            'options': {
                'Last Week': 7,
                'Last Month': 30,
                'Last Year': 365
            },
            'multiple': False
        }
        ```

    !!! warning
        If using a `str` for the arguments that can either be a `str` or `list`, they have to be comma separated, i.e. `sector='Financial Services, Technology'`.


=== "Example"

    ```python hl_lines="2 3 4 5 6"
    r = Research(username='username@yahoo.com', password=password)
    r.trades(
        sector=['Financial Services', 'Technology'],
        term='Short term',
        startdatetime='Last Week'
    )
    ```

=== "Data"

    |    | Idea Date                | Term       | Ticker   | Rating   |   Price Target |   Rate of Return | ID                              | Image URL                                                    | Company Name                  |   Price Timestamp |   Current Price | Title                                                                             | Highlights   | Description                                                                                                                                                                                                                                               |
    |---:|:-------------------------|:-----------|:---------|:---------|---------------:|-----------------:|:--------------------------------|:-------------------------------------------------------------|:------------------------------|------------------:|----------------:|:----------------------------------------------------------------------------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |  0 | 2020-07-30T00:00:00.000Z | Short term | BHLB     | Sell     |           8.3  |        -0.177134 | tc_USvyP6AAPGJwApgABAACAAAD6CIg | https://s.yimg.com/uc/fin/img/bearish-continuation-wedge.svg | Berkshire Hills Bancorp, Inc. |     1596225965000 |            9.96 | Berkshire Hills Bancorp, Inc. - BHLB forms a Continuation Wedge (Bearish) pattern |              | ['This stock has formed a pattern called Continuation Wedge (Bearish), providing a target price for the short-term in the range of 8.10 to 8.50.', 'The price recently crossed below its moving average signaling a new downtrend has been established.'] |
    |  1 | 2020-07-30T00:00:00.000Z | Short term | FISV     | Buy      |         107.82 |         0.070492 | tc_USvyO_AAPKkQAGgABAACAAAD6CJg | https://s.yimg.com/uc/fin/img/bullish-double-bottom.svg      | Fiserv, Inc.                  |     1596225601000 |           99.79 | Fiserv, Inc. - FISV forms a Double Bottom pattern                                 |              | ['This stock has formed a pattern called Double Bottom, providing a target price for the short-term in the range of 107.00 to 108.50.', 'The Intermediate-Term KST indicator has triggered a bullish signal by rising above its moving average.']         |

