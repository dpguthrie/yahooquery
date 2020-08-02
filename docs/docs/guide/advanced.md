
!!! info
    **For Yahoo Finance Premium Subscribers**

There might be a use case for combining the functionalities of both the Ticker and Research class. And, ideally, the user wouldn't have to utilize the login functionality in both instances. Here's how you would do that:

```python
from yahooquery import Research, Ticker

r = Research(username='username@yahoo.com', password='password')

# I want to retrieve last week's Bullish Analyst Report's for the Financial Services sector
df = r.reports(sector='Financial Services', report_date='Last Week', investment_rating='Bullish', report_type='Analyst Report')

# But now I want to get the data I find relevant and run my own analysis

# Using aapl as a default symbol (we will change that later).  But, the important part is passing the current session and crumb from our Research instance
tickers = Ticker('aapl', session=r.session, crumb=r.crumb)

# Now, I can loop through the dataframe and retrieve relevant data for each ticker within the dataframe utilizing the Ticker instance
for i, row in df.iterrows():
    tickers.symbols = row['Tickers']
    data = tickers.p_company_360
    # Do something with data
    # ...

# Or, pass all tickers to the Ticker instance
ticker_list = df['Tickers'].tolist()
ticker_list = list(set(_flatten_list(ticker_list)))
tickers = Ticker(ticker_list, session=r.session, crumb=r.crumb)
data = tickers.p_company_360
# Do something with data
# ...
```