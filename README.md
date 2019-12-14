# Yahooquery
[![CodeFactor](https://www.codefactor.io/repository/github/dpguthrie/yahooquery/badge/master?s=289f5ed067de511ac29b5e229c1a5ef5c8c1dc83)](https://www.codefactor.io/repository/github/dpguthrie/yahooquery/overview/master)

Python wrapper around an unofficial Yahoo Finance API.  

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

Based on the data you'd like, the result will either be accessed through a dictionary or as a `pandas.DataFrame`.  Accessing data is incredibly easy and pythonic.

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
aapl = Ticker('aapl')

# Balance Sheet
aapl.balance_sheet
```
|    | endDate    |        cash |   shortTermInvestments |   netReceivables |   inventory |   otherCurrentAssets |   totalCurrentAssets |   longTermInvestments |   propertyPlantEquipment |   otherAssets |   totalAssets |   accountsPayable |   shortLongTermDebt |   otherCurrentLiab |   longTermDebt |   otherLiab |   totalCurrentLiabilities |    totalLiab |   commonStock |   retainedEarnings |   treasuryStock |   otherStockholderEquity |   totalStockholderEquity |   netTangibleAssets |    goodWill |   intangibleAssets | ticker   |
|---:|:-----------|------------:|-----------------------:|-----------------:|------------:|---------------------:|---------------------:|----------------------:|-------------------------:|--------------:|--------------:|------------------:|--------------------:|-------------------:|---------------:|------------:|--------------------------:|-------------:|--------------:|-------------------:|----------------:|-------------------------:|-------------------------:|--------------------:|------------:|-------------------:|:---------|
|  0 | 2019-09-28 | 48844000000 |            51713000000 |      45804000000 |  4106000000 |          12352000000 |         162819000000 |          105341000000 |              37378000000 |   32978000000 |  338516000000 |       46236000000 |         10260000000 |        43242000000 |    91807000000 | 50503000000 |              105718000000 | 248028000000 |   45174000000 |        45898000000 |      -584000000 |               -584000000 |              90488000000 |         90488000000 | nan         |        nan         | AAPL     |
|  1 | 2018-09-29 | 25913000000 |            40388000000 |      48995000000 |  3956000000 |          12087000000 |         131339000000 |          170799000000 |              41304000000 |   22283000000 |  365725000000 |       55888000000 |          8784000000 |        39293000000 |    93735000000 | 48914000000 |              115929000000 | 258578000000 |   40201000000 |        70400000000 |     -3454000000 |              -3454000000 |             107147000000 |        107147000000 | nan         |        nan         | AAPL     |
|  2 | 2017-09-30 | 20289000000 |            53892000000 |      35673000000 |  4855000000 |          13936000000 |         128645000000 |          194714000000 |              33783000000 |   18177000000 |  375319000000 |       44242000000 |          6496000000 |        38099000000 |    97207000000 | 43251000000 |              100814000000 | 241272000000 |   35867000000 |        98330000000 |      -150000000 |               -150000000 |             134047000000 |        134047000000 | nan         |        nan         | AAPL     |
|  3 | 2016-09-24 | 20484000000 |            46671000000 |      29299000000 |  2132000000 |           8283000000 |         106869000000 |          170430000000 |              27010000000 |    8757000000 |  321686000000 |       37294000000 |          3500000000 |         8243000000 |    75427000000 | 39004000000 |               79006000000 | 193437000000 |   31251000000 |        96364000000 |       634000000 |                634000000 |             128249000000 |        119629000000 |   5.414e+09 |          3.206e+09 | AAPL     |

```python
# Cash Flow
aapl.cash_flow
```
|    | endDate    |   netIncome |   depreciation |   changeToNetincome |   changeToAccountReceivables |   changeToLiabilities |   changeToInventory |   changeToOperatingActivities |   totalCashFromOperatingActivities |   capitalExpenditures |   investments |   otherCashflowsFromInvestingActivities |   totalCashflowsFromInvestingActivities |   dividendsPaid |   netBorrowings |   otherCashflowsFromFinancingActivities |   totalCashFromFinancingActivities |   changeInCash |   repurchaseOfStock |   issuanceOfStock | ticker   |
|---:|:-----------|------------:|---------------:|--------------------:|-----------------------------:|----------------------:|--------------------:|------------------------------:|-----------------------------------:|----------------------:|--------------:|----------------------------------------:|----------------------------------------:|----------------:|----------------:|----------------------------------------:|-----------------------------------:|---------------:|--------------------:|------------------:|:---------|
|  0 | 2019-09-28 | 55256000000 |    12547000000 |          5076000000 |                    245000000 |           -2548000000 |          -289000000 |                    -896000000 |                        69391000000 |          -10495000000 |   58093000000 |                             -1078000000 |                             45896000000 |    -14119000000 |     -7819000000 |                              -105000000 |                       -90976000000 |    24311000000 |        -69714000000 |         781000000 | AAPL     |
|  1 | 2018-09-29 | 59531000000 |    10903000000 |        -27694000000 |                  -5322000000 |            9172000000 |           828000000 |                   30016000000 |                        77434000000 |          -13313000000 |   30845000000 |                              -745000000 |                             16066000000 |    -13712000000 |       432000000 |                              -105000000 |                       -87876000000 |     5624000000 |        -75265000000 |         669000000 | AAPL     |
|  2 | 2017-09-30 | 48351000000 |    10157000000 |         10640000000 |                  -2093000000 |            8373000000 |         -2723000000 |                   -8480000000 |                        64225000000 |          -12451000000 |  -33542000000 |                              -124000000 |                            -46446000000 |    -12769000000 |     29014000000 |                              -105000000 |                       -17974000000 |     -195000000 |        -34774000000 |         555000000 | AAPL     |
|  3 | 2016-09-24 | 45687000000 |    10505000000 |          9634000000 |                    527000000 |             563000000 |           217000000 |                    -902000000 |                        66231000000 |          -12734000000 |  -32022000000 |                              -924000000 |                            -45977000000 |    -12150000000 |     22057000000 |                              -105000000 |                       -20890000000 |     -636000000 |        -31292000000 |         495000000 | AAPL     |

```python
# Income Statement
aapl.income_statement
```
|    | endDate    |   totalRevenue |   costOfRevenue |   grossProfit |   researchDevelopment |   sellingGeneralAdministrative | nonRecurring   | otherOperatingExpenses   |   totalOperatingExpenses |   operatingIncome |   totalOtherIncomeExpenseNet |        ebit |   interestExpense |   incomeBeforeTax |   incomeTaxExpense | minorityInterest   |   netIncomeFromContinuingOps | discontinuedOperations   | extraordinaryItems   | effectOfAccountingCharges   | otherItems   |   netIncome |   netIncomeApplicableToCommonShares | ticker   |
|---:|:-----------|---------------:|----------------:|--------------:|----------------------:|-------------------------------:|:---------------|:-------------------------|-------------------------:|------------------:|-----------------------------:|------------:|------------------:|------------------:|-------------------:|:-------------------|-----------------------------:|:-------------------------|:---------------------|:----------------------------|:-------------|------------:|------------------------------------:|:---------|
|  0 | 2019-09-28 |   260174000000 |    161782000000 |   98392000000 |           16217000000 |                    18245000000 |                |                          |             196244000000 |       63930000000 |                   1807000000 | 63930000000 |       -3576000000 |       65737000000 |        10481000000 |                    |                  55256000000 |                          |                      |                             |              | 55256000000 |                         55256000000 | AAPL     |
|  1 | 2018-09-29 |   265595000000 |    163756000000 |  101839000000 |           14236000000 |                    16705000000 |                |                          |             194697000000 |       70898000000 |                   2005000000 | 70898000000 |       -3240000000 |       72903000000 |        13372000000 |                    |                  59531000000 |                          |                      |                             |              | 59531000000 |                         59531000000 | AAPL     |
|  2 | 2017-09-30 |   229234000000 |    141048000000 |   88186000000 |           11581000000 |                    15261000000 |                |                          |             167890000000 |       61344000000 |                   2745000000 | 61344000000 |       -2323000000 |       64089000000 |        15738000000 |                    |                  48351000000 |                          |                      |                             |              | 48351000000 |                         48351000000 | AAPL     |
|  3 | 2016-09-24 |   215639000000 |    131376000000 |   84263000000 |           10045000000 |                    14194000000 |                |                          |             155615000000 |       60024000000 |                   1348000000 | 60024000000 |       -1456000000 |       61372000000 |        15685000000 |                    |                  45687000000 |                          |                      |                             |              | 45687000000 |                         45687000000 | AAPL     |




