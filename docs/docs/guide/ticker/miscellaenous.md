
### **corporate_events**

=== "Details"

    - *Description*:  Significant events related to a given symbol(s)
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    df = aapl.corporate_events
    df.head()
    ```

=== "Data"

    |    | date                |   significance | headline                                                                                                      | parentTopics       |
    |---:|:--------------------|---------------:|:--------------------------------------------------------------------------------------------------------------|:-------------------|
    |  0 | 2012-03-19 00:00:00 |              1 | Apple Inc. Announces Plans To Initiate Dividend And Share Repurchase Program                                  | Performance        |
    |  1 | 2012-10-25 00:00:00 |              3 | Apple Inc Declares Cash Dividend                                                                              | Performance        |
    |  2 | 2013-01-23 00:00:00 |              1 | Apple Inc Issues Q2 2013 Revenue Guidance Below Analysts' Estimates; Declares Cash Dividend                   | Corporate Guidance |
    |  3 | 2013-04-23 00:00:00 |              1 | Apple Inc Increases Repurchase Authorization To $60 Billion From The $10 Billion; Approves Quarterly Dividend | Ownership/Control  |
    |  4 | 2013-07-23 00:00:00 |              3 | Apple Inc Declares Cash Dividend                                                                              | Performance        |

### **earnings_calendar**

=== "Details"

    - *Description*:  Upcoming and historical earnings information for given symbol(s)
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    df = aapl.earnings_calendar
    df.head()
    ```

=== "Data"

    |    | Symbol   | Company    | Earnings Date          | EPS Estimate   | Reported EPS   | Surprise(%)   |
    |---:|:---------|:-----------|:-----------------------|:---------------|:---------------|:--------------|
    |  0 | AAPL     | Apple Inc  | Apr 28, 2021, 6 AMEDT  | -              | -              | -             |
    |  1 | AAPL     | Apple Inc  | Jan 26, 2021, 6 AMEDT  | -              | -              | -             |
    |  2 | AAPL     | Apple Inc  | Oct 28, 2020, 6 AMEDT  | 2.78           | -              | -             |
    |  3 | AAPL     | Apple Inc. | Jul 30, 2020, 12 AMEDT | 2.04           | 2.58           | +26.22        |
    |  4 | AAPL     | Apple Inc. | Apr 30, 2020, 12 AMEDT | 2.26           | 2.55           | +12.78        |


### **news**

=== "Details"

    - *Description*:  Get news headline and summary information for given symbol(s)
    - *Return*:  `list`
    - *Arguments*:

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | count      | `int` | `25`    |  optional   |              |
    | start  | `str` or `datetime.datetime`  | `None`       | optional   | If a `str` is used, the format should be YYYY-MM-DD |

    !!! warning
        It's recommended to use one symbol when utilizing this method as there's no discernible way to group resulting news items to the symbols they belong to.

    !!! tip
        If multiple symbols are used, only one request will be made regardless of the number of symbols

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.news(5)
    ```

=== "Data"

    ```python
    [{
        'rank': 0,
        'id': '3a3b4532-38fb-3fcb-85b3-3cdc4d5bbabe',
        'tag': 'news',
        'title': 'Big Tech’s CEOs Got the Last Word. Here’s Why Tech Earnings Were So Important.',
        'summary': 'Amazon’s sales were up 40% in the June quarter, which one analyst referred to as shocking levels of growth. Meanwhile, Apple couldn’t keep up with demand for Macs and iPads.',
        'url': 'https://www.barrons.com/articles/heres-why-amazon-apple-and-facebook-earnings-were-so-important-51596232561?siteid=yhoof2&yptr=yahoo',
        'author_name': 'Eric J. Savitz',
        'provider_publish_time': 1596232560,
        'provider_name': 'Barrons.com',
        'hosted': False,
        'tickers': [],
        'featured': False,
        'timeZoneShortName': 'EDT',
        'timeZoneFullName': 'America/New_York',
        'gmtOffSetMilliseconds': -14400000,
        'imageSet': {}
    }, {
        'rank': 1,
        'id': 'e0ea15cf-9cd4-33fa-b8ef-87ea7ee40c32',
        'tag': 'news',
        'title': 'Microsoft Is in Talks to Buy TikTok in U.S.',
        'summary': '(Bloomberg) -- Microsoft Corp. is exploring an acquisition of TikTok’s operations in the U.S., according to a people familiar with the matter. A deal would give the software company a popular social-media service and relieve U.S. government pressure on the Chinese owner of the video-sharing app.The Trump administration has been weighing whether to direct China-based ByteDance Ltd. to divest its stake in TikTok’s U.S. operations, according to several people familiar with the issue. The U.S. has been investigating potential national security risks due to the Chinese company’s control of the app.While the administration was prepared to announce an order as soon as Friday, according to three people familiar with the matter, another person said later that the decision was on hold, pending further review by President Donald Trump. All of the people asked not to be identified because the deliberations are private.Spokespeople for Microsoft and TikTok declined to comment on any potential talks. The software company’s interest in the app was reported earlier by Fox Business Network.“We are looking at TikTok. We may be banning TikTok,” Trump told reporters Friday at the White House. “We are looking at a lot of alternatives with respect to TikTok.”Any transaction could face regulatory hurdles. ByteDance bought Musical.ly Inc. in 2017 and merged it with TikTok, creating a social-media hit in the U.S -- the first Chinese app to make such inroads. As TikTok became more popular, U.S. officials grew concerned about the potential for the Chinese government to use the app to gain data on U.S. citizens.The Committee on Foreign Investment in the U.S. began a review in 2019 of the Musical.ly purchase. In recent years, CFIUS, which investigates overseas acquisitions of U.S. businesses, has taken a much more aggressive role in reviewing and approving deals that may threaten national security. It can recommend that the president block or unwind transactions.It’s also possible that other potential buyers could come forward, said another person familiar with the discussions. Microsoft’s industry peers -- Facebook Inc., Apple Inc., Amazon.com Inc. and Alphabet Inc. -- fit the profile of potential suitors, though all are under antitrust scrutiny from U.S. regulators, which would likely complicate a deal.A purchase of TikTok would represent a huge coup for Microsoft, which would gain a popular consumer app that has won over young people with a steady diet of dance videos, lip-syncing clips and viral memes. The company has dabbled in social-media investments in the past, but hasn’t developed a popular service of its own in the lucrative sector. Microsoft acquired the LinkedIn job-hunting and corporate networking company for $26.2 billion in 2016.Microsoft can point to one acquisition that came with a massive existing community of users that has increased under its ownership -- the 2014 deal for Minecraft, the best-selling video game ever.Other purchases of popular services have gone less well. The 2011 pickup of Skype led to several years of stagnation for the voice-calling service and Microsoft fell behind newer products in the category. Outside of Xbox, the company hasn’t focused on younger consumers. A TikTok deal could change that, though, and give Microsoft “a crown jewel on the consumer social media front,” Dan Ives, an analyst at Wedbush Securities, wrote in a note to investors Friday.TikTok has repeatedly rejected accusations that it feeds user data to China or is beholden to Beijing, even though ByteDance is based there. TikTok now has a U.S.-based chief executive officer and ByteDance has considered making other organizational changes to satisfy U.S. authorities.“Hundreds of millions of people come to TikTok for entertainment and connection, including our community of creators and artists who are building livelihoods from the platform,” a TikTok spokeswoman said Friday. “We’re motivated by their passion and creativity, and committed to protecting their privacy and safety as we continue working to bring joy to families and meaningful careers to those who create on our platform.”The mechanics of separating the TikTok app in the U.S. from the rest of its operations won’t come without complications. Unlike many tech companies in the U.S. where engineers for, say, Google, work on particular products like YouTube or Google Maps, many of ByteDance’s engineers work across its different platforms and services and continue to work on TikTok globally.On Thursday, U.S. Senators Josh Hawley, a Missouri Republican, and Richard Blumenthal, a Connecticut Democrat, wrote the Justice Department asking for an investigation of whether TikTok has violated the constitutional rights of Americans by sharing private information with the Chinese government.A deal with Microsoft could potentially help extract ByteDance from the political war between the U.S. and China.U.S. Senator Marco Rubio, a Florida Republican and member of the Senate’s Select Committee on Intelligence, applauded the idea of a TikTok sale. “In its current form, TikTok represents a potential threat to personal privacy and our national security,” Rubio said in a statement. “We must do more than simply remove ByteDance from the equation. Moving forward, we must establish a framework of standards that must be met before a high-risk, foreign-based app is allowed to operate on American telecommunications networks and devices.”(Updates with details of TikTok’s operations in the 14th paragraph.)For more articles like this, please visit us at bloomberg.comSubscribe now to stay ahead with the most trusted business news source.©2020 Bloomberg L.P.',
        'url': 'https://finance.yahoo.com/news/microsoft-said-talks-buy-tiktok-185221680.html',
        'author_name': 'Kurt Wagner, Jennifer Jacobs, Saleha Mohsin and Jenny Leonard',
        'provider_publish_time': 1596232267,
        'provider_name': 'Bloomberg',
        'hosted': True,
        'tickers': [],
        'thumbnail': 'https://media.zenfs.com/en/bloomberg_technology_68/d998c0ffe5e9a652dce2e465c5d6d8a3',
        'featured': False,
        'timeZoneShortName': 'EDT',
        'timeZoneFullName': 'America/New_York',
        'gmtOffSetMilliseconds': -14400000,
        'imageSet': {}
    }, {
        'rank': 2,
        'id': '8cc7e7d9-87ec-3aaf-8a51-24f8ae1f6eca',
        'tag': 'news',
        'title': 'Bitcoin Is Rising Again. Asking Why Takes You Down the Financial Rabbit Hole.',
        'summary': 'How to explain Bitcoin’s reversal of fortune? In search of an answer our columnist explores the dollar, the euro, gold, stocks, inflation, and more.',
        'url': 'https://www.barrons.com/articles/bitcoin-is-rising-again-asking-why-takes-you-down-a-financial-rabbit-hole-51596231804?siteid=yhoof2&yptr=yahoo',
        'author_name': 'Jack Hough',
        'provider_publish_time': 1596231780,
        'provider_name': 'Barrons.com',
        'hosted': False,
        'tickers': [],
        'featured': False,
        'timeZoneShortName': 'EDT',
        'timeZoneFullName': 'America/New_York',
        'gmtOffSetMilliseconds': -14400000,
        'imageSet': {}
    }, {
        'rank': 3,
        'id': '14ba64e7-a900-3e30-b513-94a5efce0dd7',
        'tag': 'news',
        'title': 'Apple Stock Rallied 10% Friday. Here’s Why.',
        'summary': 'One day after reporting June quarter results, Apple (ticker: AAPL) stock surged 10.5% to $425.04, the stock’s first-ever close above $400.  The stock won’t stay there for long, though: The company Thursday declared a 4-for-1 stock split, effective August 31.  A big revenue beat: Apple had $59.7 billion in sales in the quarter, up 11% from a year ago, and beating consensus by $7.6 billion.',
        'url': 'https://www.barrons.com/articles/apple-stock-hits-new-highs-earnings-51596215820?siteid=yhoof2&yptr=yahoo',
        'author_name': 'Eric J. Savitz',
        'provider_publish_time': 1596231300,
        'provider_name': 'Barrons.com',
        'hosted': False,
        'tickers': [],
        'featured': False,
        'timeZoneShortName': 'EDT',
        'timeZoneFullName': 'America/New_York',
        'gmtOffSetMilliseconds': -14400000,
        'imageSet': {}
    }, {
        'rank': 4,
        'id': '5894f228-5bad-3eda-8a48-d8fc0bdced0c',
        'tag': 'news',
        'title': 'Apple Tops Saudi Aramco as World’s Most Valuable Company',
        'summary': '(Bloomberg) -- Apple Inc. became the world’s most valuable company with its market value overtaking Saudi Aramco in the wake of better-than-expected earnings.Apple jumped 10% on Friday, ending the day with a record market capitalization of $1.817 trillion. It’s the first time the company’s valuation has surpassed that of Saudi Arabia’s national oil company, which made its market debut in Riyadh in December, and is valued at $1.76 trillion. Before that, Apple had vied with Microsoft Corp. for the title of the U.S.’s largest public company.The dethroning of Aramco comes after a tumultuous period for the Saudi company. Its initial public offering fell short of Crown Price Mohammed bin Salman’s expectations. The kingdom’s de facto ruler initially wanted a valuation of $2 trillion and to raise $100 billion. But after foreign investors balked at the pricing, the government settled on a smaller domestic offering and raised about $30 billion, still the largest IPO ever.Then came this year’s plunge in crude prices as energy demand crashed with the spread of the virus. Aramco’s second-quarter revenue probably dropped to about $37 billion from $76 billion a year earlier, according to analyst estimates compiled by Bloomberg. That’s less than the $59.7 billion in sales that Apple reported for its most recent period.Aramco’s stock is down 6.4% since the end of December, though that’s far less than the fall of other oil majors. Exxon Mobil Corp. has declined 40% and Royal Dutch Shell Plc has dropped 50%.Apple, meanwhile, has benefited as the pandemic has strengthened the market positions of the world’s biggest technology companies, which boast strong balance sheets and fast-growing businesses thanks to an acceleration in the shift to digital services. The iPhone maker’s shares have gained 45% so far this year.(Adds closing share values throughout. A previous version of this story corrected the market cap gain.)For more articles like this, please visit us at bloomberg.comSubscribe now to stay ahead with the most trusted business news source.©2020 Bloomberg L.P.',
        'url': 'https://finance.yahoo.com/news/apple-briefly-tops-saudi-aramco-153503708.html',
        'author_name': 'Jeran Wittenstein and Matthew Martin',
        'provider_publish_time': 1596229879,
        'provider_name': 'Bloomberg',
        'hosted': True,
        'tickers': [],
        'thumbnail': 'https://media.zenfs.com/en/bloomberg_markets_842/8a17157f40b14e617bb6ed1b8e2774f5',
        'featured': False,
        'timeZoneShortName': 'EDT',
        'timeZoneFullName': 'America/New_York',
        'gmtOffSetMilliseconds': -14400000,
        'imageSet': {}
    }]
    ```

### **quotes**

=== "Details"

    - *Description*:  Get real-time quote information for given symbol(s)
    - *Return*:  `list`

    !!! tip
        If multiple symbols are used, only one request will be made regardless of the number of symbols

=== "Example"

    ```python hl_lines="2"
    tickers = Ticker('fb aapl amzn nflx goog')
    tickers.quotes
    ```

=== "Data"

    ```python
    [{
        'language': 'en-US',
        'region': 'US',
        'quoteType': 'EQUITY',
        'quoteSourceName': 'Nasdaq Real Time Price',
        'triggerable': True,
        'currency': 'USD',
        'tradeable': False,
        'firstTradeDateMilliseconds': 1337347800000,
        'priceHint': 2,
        'postMarketChangePercent': -0.067015484,
        'postMarketTime': 1596233013,
        'postMarketPrice': 253.5,
        'postMarketChange': -0.16999817,
        'regularMarketChange': 19.169998,
        'regularMarketChangePercent': 8.17484,
        'regularMarketTime': 1596225602,
        'regularMarketPrice': 253.67,
        'regularMarketDayHigh': 255.85,
        'regularMarketDayRange': '249.0 - 255.85',
        'regularMarketDayLow': 249.0,
        'regularMarketVolume': 52105898,
        'regularMarketPreviousClose': 234.5,
        'bid': 253.31,
        'ask': 253.7,
        'bidSize': 11,
        'askSize': 12,
        'fullExchangeName': 'NasdaqGS',
        'financialCurrency': 'USD',
        'regularMarketOpen': 255.82,
        'averageDailyVolume3Month': 24501318,
        'averageDailyVolume10Day': 17021500,
        'fiftyTwoWeekLowChange': 116.56999,
        'fiftyTwoWeekLowChangePercent': 0.8502552,
        'fiftyTwoWeekRange': '137.1 - 255.85',
        'fiftyTwoWeekHighChange': -2.180008,
        'fiftyTwoWeekHighChangePercent': -0.008520649,
        'fiftyTwoWeekLow': 137.1,
        'fiftyTwoWeekHigh': 255.85,
        'earningsTimestamp': 1596124800,
        'earningsTimestampStart': 1603868340,
        'earningsTimestampEnd': 1604304000,
        'trailingPE': 34.80653,
        'epsTrailingTwelveMonths': 7.288,
        'epsForward': 9.74,
        'sharesOutstanding': 2408470016,
        'bookValue': 36.936,
        'fiftyDayAverage': 235.86743,
        'fiftyDayAverageChange': 17.802567,
        'fiftyDayAverageChangePercent': 0.075477004,
        'twoHundredDayAverage': 207.2297,
        'twoHundredDayAverageChange': 46.440292,
        'twoHundredDayAverageChangePercent': 0.22410056,
        'marketCap': 723725582336,
        'forwardPE': 26.044147,
        'priceToBook': 6.867825,
        'sourceInterval': 15,
        'exchangeDataDelayedBy': 0,
        'marketState': 'POST',
        'exchange': 'NMS',
        'shortName': 'Facebook, Inc.',
        'longName': 'Facebook, Inc.',
        'messageBoardId': 'finmb_20765463',
        'exchangeTimezoneName': 'America/New_York',
        'exchangeTimezoneShortName': 'EDT',
        'gmtOffSetMilliseconds': -14400000,
        'market': 'us_market',
        'esgPopulated': False,
        'displayName': 'Facebook',
        'symbol': 'FB'
    }, {
        'language': 'en-US',
        'region': 'US',
        'quoteType': 'EQUITY',
        'quoteSourceName': 'Delayed Quote',
        'triggerable': True,
        'currency': 'USD',
        'tradeable': False,
        'firstTradeDateMilliseconds': 345479400000,
        'priceHint': 2,
        'postMarketChangePercent': 0.519949,
        'postMarketTime': 1596233031,
        'postMarketPrice': 427.25,
        'postMarketChange': 2.2099915,
        'regularMarketChange': 40.28,
        'regularMarketChangePercent': 10.468863,
        'regularMarketTime': 1596225602,
        'regularMarketPrice': 425.04,
        'regularMarketDayHigh': 425.66,
        'regularMarketDayRange': '403.36 - 425.66',
        'regularMarketDayLow': 403.36,
        'regularMarketVolume': 91201476,
        'regularMarketPreviousClose': 384.76,
        'bid': 427.26,
        'ask': 426.2,
        'bidSize': 30,
        'askSize': 31,
        'fullExchangeName': 'NasdaqGS',
        'financialCurrency': 'USD',
        'regularMarketOpen': 411.535,
        'averageDailyVolume3Month': 34664412,
        'averageDailyVolume10Day': 32670312,
        'fiftyTwoWeekLowChange': 232.46,
        'fiftyTwoWeekLowChangePercent': 1.2070827,
        'fiftyTwoWeekRange': '192.58 - 425.66',
        'fiftyTwoWeekHighChange': -0.6199951,
        'fiftyTwoWeekHighChangePercent': -0.0014565501,
        'fiftyTwoWeekLow': 192.58,
        'fiftyTwoWeekHigh': 425.66,
        'dividendDate': 1589414400,
        'earningsTimestamp': 1596124800,
        'earningsTimestampStart': 1603868340,
        'earningsTimestampEnd': 1604304000,
        'trailingAnnualDividendRate': 3.08,
        'trailingPE': 32.236633,
        'trailingAnnualDividendYield': 0.0080049895,
        'epsTrailingTwelveMonths': 13.185,
        'epsForward': 14.97,
        'sharesOutstanding': 4334329856,
        'bookValue': 16.761,
        'fiftyDayAverage': 369.66028,
        'fiftyDayAverageChange': 55.37973,
        'fiftyDayAverageChangePercent': 0.1498125,
        'twoHundredDayAverage': 313.8948,
        'twoHundredDayAverageChange': 111.1452,
        'twoHundredDayAverageChangePercent': 0.35408422,
        'marketCap': 1842263621632,
        'forwardPE': 28.392786,
        'priceToBook': 25.35887,
        'sourceInterval': 15,
        'exchangeDataDelayedBy': 0,
        'marketState': 'POST',
        'exchange': 'NMS',
        'shortName': 'Apple Inc.',
        'longName': 'Apple Inc.',
        'messageBoardId': 'finmb_24937',
        'exchangeTimezoneName': 'America/New_York',
        'exchangeTimezoneShortName': 'EDT',
        'gmtOffSetMilliseconds': -14400000,
        'market': 'us_market',
        'esgPopulated': False,
        'displayName': 'Apple',
        'symbol': 'AAPL'
    }, {
        'language': 'en-US',
        'region': 'US',
        'quoteType': 'EQUITY',
        'quoteSourceName': 'Nasdaq Real Time Price',
        'triggerable': True,
        'currency': 'USD',
        'tradeable': False,
        'firstTradeDateMilliseconds': 863703000000,
        'priceHint': 2,
        'postMarketChangePercent': -0.2673244,
        'postMarketTime': 1596232724,
        'postMarketPrice': 3156.22,
        'postMarketChange': -8.459961,
        'regularMarketChange': 112.80005,
        'regularMarketChangePercent': 3.696084,
        'regularMarketTime': 1596225602,
        'regularMarketPrice': 3164.68,
        'regularMarketDayHigh': 3244.5,
        'regularMarketDayRange': '3151.02 - 3244.5',
        'regularMarketDayLow': 3151.02,
        'regularMarketVolume': 7862360,
        'regularMarketPreviousClose': 3051.88,
        'bid': 3160.52,
        'ask': 3160.0,
        'bidSize': 8,
        'askSize': 14,
        'fullExchangeName': 'NasdaqGS',
        'financialCurrency': 'USD',
        'regularMarketOpen': 3244.0,
        'averageDailyVolume3Month': 4675034,
        'averageDailyVolume10Day': 4733650,
        'fiftyTwoWeekLowChange': 1538.6499,
        'fiftyTwoWeekLowChangePercent': 0.9462617,
        'fiftyTwoWeekRange': '1626.03 - 3344.29',
        'fiftyTwoWeekHighChange': -179.6101,
        'fiftyTwoWeekHighChangePercent': -0.053706497,
        'fiftyTwoWeekLow': 1626.03,
        'fiftyTwoWeekHigh': 3344.29,
        'earningsTimestamp': 1596124800,
        'earningsTimestampStart': 1603382400,
        'earningsTimestampEnd': 1603728000,
        'trailingPE': 151.15971,
        'epsTrailingTwelveMonths': 20.936,
        'epsForward': 37.79,
        'sharesOutstanding': 498776000,
        'bookValue': 130.806,
        'fiftyDayAverage': 2896.579,
        'fiftyDayAverageChange': 268.10083,
        'fiftyDayAverageChangePercent': 0.09255774,
        'twoHundredDayAverage': 2323.4736,
        'twoHundredDayAverageChange': 841.2063,
        'twoHundredDayAverageChangePercent': 0.36204684,
        'marketCap': 1578466410496,
        'forwardPE': 83.74384,
        'priceToBook': 24.193691,
        'sourceInterval': 15,
        'exchangeDataDelayedBy': 0,
        'marketState': 'POST',
        'exchange': 'NMS',
        'shortName': 'Amazon.com, Inc.',
        'longName': 'Amazon.com, Inc.',
        'messageBoardId': 'finmb_18749',
        'exchangeTimezoneName': 'America/New_York',
        'exchangeTimezoneShortName': 'EDT',
        'gmtOffSetMilliseconds': -14400000,
        'market': 'us_market',
        'esgPopulated': False,
        'displayName': 'Amazon.com',
        'symbol': 'AMZN'
    }, {
        'language': 'en-US',
        'region': 'US',
        'quoteType': 'EQUITY',
        'quoteSourceName': 'Nasdaq Real Time Price',
        'triggerable': True,
        'currency': 'USD',
        'tradeable': False,
        'firstTradeDateMilliseconds': 1022160600000,
        'priceHint': 2,
        'postMarketChangePercent': -0.5584215,
        'postMarketTime': 1596232099,
        'postMarketPrice': 486.15,
        'postMarketChange': -2.730011,
        'regularMarketChange': 3.080017,
        'regularMarketChangePercent': 0.6340093,
        'regularMarketTime': 1596225602,
        'regularMarketPrice': 488.88,
        'regularMarketDayHigh': 494.795,
        'regularMarketDayRange': '484.5 - 494.795',
        'regularMarketDayLow': 484.5,
        'regularMarketVolume': 5797772,
        'regularMarketPreviousClose': 485.8,
        'bid': 487.3,
        'ask': 488.56,
        'bidSize': 9,
        'askSize': 40,
        'fullExchangeName': 'NasdaqGS',
        'financialCurrency': 'USD',
        'regularMarketOpen': 488.29,
        'averageDailyVolume3Month': 7602690,
        'averageDailyVolume10Day': 7325312,
        'fiftyTwoWeekLowChange': 236.6,
        'fiftyTwoWeekLowChangePercent': 0.93784684,
        'fiftyTwoWeekRange': '252.28 - 575.37',
        'fiftyTwoWeekHighChange': -86.48999,
        'fiftyTwoWeekHighChangePercent': -0.15032065,
        'fiftyTwoWeekLow': 252.28,
        'fiftyTwoWeekHigh': 575.37,
        'earningsTimestamp': 1594900801,
        'earningsTimestampStart': 1602676800,
        'earningsTimestampEnd': 1603123200,
        'trailingPE': 82.55319,
        'epsTrailingTwelveMonths': 5.922,
        'epsForward': 8.78,
        'sharesOutstanding': 441015008,
        'bookValue': 21.166,
        'fiftyDayAverage': 478.79858,
        'fiftyDayAverageChange': 10.081421,
        'fiftyDayAverageChangePercent': 0.021055661,
        'twoHundredDayAverage': 409.49237,
        'twoHundredDayAverageChange': 79.387634,
        'twoHundredDayAverageChangePercent': 0.19386841,
        'marketCap': 215603412992,
        'forwardPE': 55.681095,
        'priceToBook': 23.09742,
        'sourceInterval': 15,
        'exchangeDataDelayedBy': 0,
        'marketState': 'POST',
        'exchange': 'NMS',
        'shortName': 'Netflix, Inc.',
        'longName': 'Netflix, Inc.',
        'messageBoardId': 'finmb_32012',
        'exchangeTimezoneName': 'America/New_York',
        'exchangeTimezoneShortName': 'EDT',
        'gmtOffSetMilliseconds': -14400000,
        'market': 'us_market',
        'esgPopulated': False,
        'displayName': 'Netflix',
        'symbol': 'NFLX'
    }, {
        'language': 'en-US',
        'region': 'US',
        'quoteType': 'EQUITY',
        'quoteSourceName': 'Delayed Quote',
        'triggerable': True,
        'currency': 'USD',
        'tradeable': False,
        'firstTradeDateMilliseconds': 1092922200000,
        'priceHint': 2,
        'postMarketChangePercent': 0.0026999423,
        'postMarketTime': 1596231815,
        'postMarketPrice': 1483.0,
        'postMarketChange': 0.040039062,
        'regularMarketChange': -48.48999,
        'regularMarketChangePercent': -3.16628,
        'regularMarketTime': 1596225602,
        'regularMarketPrice': 1482.96,
        'regularMarketDayHigh': 1508.95,
        'regularMarketDayRange': '1454.04 - 1508.95',
        'regularMarketDayLow': 1454.04,
        'regularMarketVolume': 3368287,
        'regularMarketPreviousClose': 1531.45,
        'bid': 1483.0,
        'ask': 1484.0,
        'bidSize': 12,
        'askSize': 8,
        'fullExchangeName': 'NasdaqGS',
        'financialCurrency': 'USD',
        'regularMarketOpen': 1505.01,
        'averageDailyVolume3Month': 1643406,
        'averageDailyVolume10Day': 1380212,
        'fiftyTwoWeekLowChange': 469.42395,
        'fiftyTwoWeekLowChangePercent': 0.46315467,
        'fiftyTwoWeekRange': '1013.536 - 1586.99',
        'fiftyTwoWeekHighChange': -104.03003,
        'fiftyTwoWeekHighChangePercent': -0.06555179,
        'fiftyTwoWeekLow': 1013.536,
        'fiftyTwoWeekHigh': 1586.99,
        'trailingPE': 29.915276,
        'epsTrailingTwelveMonths': 49.572,
        'epsForward': 55.06,
        'sharesOutstanding': 336161984,
        'bookValue': 297.759,
        'fiftyDayAverage': 1479.2025,
        'fiftyDayAverageChange': 3.7574463,
        'fiftyDayAverageChangePercent': 0.0025401837,
        'twoHundredDayAverage': 1375.5465,
        'twoHundredDayAverageChange': 107.41345,
        'twoHundredDayAverageChangePercent': 0.07808784,
        'marketCap': 1014620422144,
        'forwardPE': 26.933525,
        'priceToBook': 4.9804034,
        'sourceInterval': 15,
        'exchangeDataDelayedBy': 0,
        'marketState': 'POST',
        'exchange': 'NMS',
        'shortName': 'Alphabet Inc.',
        'longName': 'Alphabet Inc.',
        'messageBoardId': 'finmb_29096',
        'exchangeTimezoneName': 'America/New_York',
        'exchangeTimezoneShortName': 'EDT',
        'gmtOffSetMilliseconds': -14400000,
        'market': 'us_market',
        'esgPopulated': False,
        'displayName': 'Alphabet',
        'symbol': 'GOOG'
    }]
    ```

### **recommendations**

=== "Details"

    - *Description*:  Get real-time quote information for given symbol(s)
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    tickers = Ticker('aapl gs hasgx ^GSPC ezu')
    tickers.recommendations
    ```

=== "Data"
    
    ```python
    {
        'aapl': {
            'symbol': 'AAPL',
            'recommendedSymbols': [{
                'symbol': 'GOOG',
                'score': 0.279041
            }, {
                'symbol': 'AMZN',
                'score': 0.278376
            }, {
                'symbol': 'FB',
                'score': 0.274481
            }, {
                'symbol': 'TSLA',
                'score': 0.225957
            }, {
                'symbol': 'NFLX',
                'score': 0.207756
            }]
        },
        'gs': {
            'symbol': 'GS',
            'recommendedSymbols': [{
                'symbol': 'MS',
                'score': 0.195796
            }, {
                'symbol': 'JPM',
                'score': 0.160104
            }, {
                'symbol': 'WFC',
                'score': 0.139129
            }, {
                'symbol': 'C',
                'score': 0.137378
            }, {
                'symbol': 'BAC',
                'score': 0.125276
            }]
        },
        'hasgx': {
            'symbol': 'HASGX',
            'recommendedSymbols': [{
                'symbol': 'HAVLX',
                'score': 0.020499
            }, {
                'symbol': 'HAMGX',
                'score': 0.016157
            }, {
                'symbol': 'HASCX',
                'score': 0.014594
            }, {
                'symbol': 'HAIGX',
                'score': 0.012841
            }, {
                'symbol': 'HAMVX',
                'score': 0.012294
            }]
        },
        '^GSPC': {
            'symbol': '^GSPC',
            'recommendedSymbols': [{
                'symbol': '^TYX',
                'score': 0.187618
            }, {
                'symbol': '^IXIC',
                'score': 0.157791
            }, {
                'symbol': '^DJI',
                'score': 0.134881
            }, {
                'symbol': 'GE',
                'score': 0.10353
            }, {
                'symbol': 'MCD',
                'score': 0.102003
            }]
        },
        'ezu': {
            'symbol': 'EZU',
            'recommendedSymbols': [{
                'symbol': 'EWQ',
                'score': 0.152994
            }, {
                'symbol': 'EWU',
                'score': 0.146443
            }, {
                'symbol': 'EWN',
                'score': 0.145267
            }, {
                'symbol': 'IEV',
                'score': 0.143627
            }, {
                'symbol': 'EWD',
                'score': 0.141428
            }]
        }
    }
    ```

### **technical_insights**

=== "Details"

    - *Description*:  Technical indicators for given symbol(s)
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.technical_insights
    ```

=== "Data"

    ```python
    {
        'aapl': {
            'symbol': 'aapl',
            'instrumentInfo': {
                'technicalEvents': {
                    'provider': 'Trading Central',
                    'sector': 'Technology',
                    'shortTermOutlook': {
                        'stateDescription': 'Recent bearish events outweigh bullish events.',
                        'direction': 'Bearish',
                        'score': 3,
                        'scoreDescription': 'Strong Bearish Evidence',
                        'sectorDirection': 'Bullish',
                        'sectorScore': 2,
                        'sectorScoreDescription': 'Bullish Evidence',
                        'indexDirection': 'Bearish',
                        'indexScore': 2,
                        'indexScoreDescription': 'Bearish Evidence'
                    },
                    'intermediateTermOutlook': {
                        'stateDescription': 'Bullish events outweigh bearish events.',
                        'direction': 'Bullish',
                        'score': 1,
                        'scoreDescription': 'Weak Bullish Evidence',
                        'sectorDirection': 'Bullish',
                        'sectorScore': 2,
                        'sectorScoreDescription': 'Bullish Evidence',
                        'indexDirection': 'Bullish',
                        'indexScore': 2,
                        'indexScoreDescription': 'Bullish Evidence'
                    },
                    'longTermOutlook': {
                        'stateDescription': 'All events are bullish.',
                        'direction': 'Bullish',
                        'score': 2,
                        'scoreDescription': 'Bullish Evidence',
                        'sectorDirection': 'Bullish',
                        'sectorScore': 2,
                        'sectorScoreDescription': 'Bullish Evidence',
                        'indexDirection': 'Bullish',
                        'indexScore': 3,
                        'indexScoreDescription': 'Strong Bullish Evidence'
                    }
                },
                'keyTechnicals': {
                    'provider': 'Trading Central',
                    'support': 203.77,
                    'resistance': 388.23,
                    'stopLoss': 355.460616
                },
                'valuation': {
                    'color': 0.0,
                    'description': 'Overvalued',
                    'discount': '-8%',
                    'relativeValue': 'Premium',
                    'provider': 'Trading Central'
                }
            },
            'companySnapshot': {
                'sectorInfo': 'Technology',
                'company': {
                    'innovativeness': 0.9983,
                    'hiring': 0.9795,
                    'sustainability': 0.8240000000000001,
                    'insiderSentiments': 0.2217,
                    'earningsReports': 0.8340000000000001,
                    'dividends': 0.25
                },
                'sector': {
                    'innovativeness': 0.5,
                    'hiring': 0.5,
                    'sustainability': 0.5,
                    'insiderSentiments': 0.5,
                    'earningsReports': 0.5,
                    'dividends': 0.5
                }
            },
            'recommendation': {
                'targetPrice': 450.0,
                'provider': 'Argus Research',
                'rating': 'BUY'
            },
            'sigDevs': [{
                'headline': 'Apple Reports Q3 Earnings Of $2.58 Per Share',
                'date': '2020-07-30'
            }]
        }
    }
    ```