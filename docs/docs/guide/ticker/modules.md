The following data accessors, or **modules**, are grouped together because they're all retrieved from the same endpoint. The modules are given as query parameters to the API endpoint and as such can be combined to create convenient interfaces to retrieve your desired data with a single request.

## Single Module

### **asset_profile**

=== "Details"

    - *Description*:  Information related to the company's location, operations, and officers.
    - *Module*:  `assetProfile`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.asset_profile
    ```

=== "Data"

    ```python
    {'aapl': {'address1': 'One Apple Park Way',
            'auditRisk': 1,
            'boardRisk': 1,
            'city': 'Cupertino',
            'companyOfficers': [{'age': 58,
                                'exercisedValue': 0,
                                'fiscalYear': 2019,
                                'maxAge': 1,
                                'name': 'Mr. Timothy D. Cook',
                                'title': 'CEO & Director',
                                'totalPay': 11555466,
                                'unexercisedValue': 0,
                                'yearBorn': 1961},
                                {'age': 55,
                                'exercisedValue': 0,
                                'fiscalYear': 2019,
                                'maxAge': 1,
                                'name': 'Mr. Luca  Maestri',
                                'title': 'CFO & Sr. VP',
                                'totalPay': 3576221,
                                'unexercisedValue': 0,
                                'yearBorn': 1964},
                                {'age': 55,
                                'exercisedValue': 0,
                                'fiscalYear': 2019,
                                'maxAge': 1,
                                'name': 'Mr. Jeffrey E. Williams',
                                'title': 'Chief Operating Officer',
                                'totalPay': 3574503,
                                'unexercisedValue': 0,
                                'yearBorn': 1964},
                                {'age': 55,
                                'exercisedValue': 0,
                                'fiscalYear': 2019,
                                'maxAge': 1,
                                'name': 'Ms. Katherine L. Adams',
                                'title': 'Sr. VP, Gen. Counsel & Sec.',
                                'totalPay': 3598384,
                                'unexercisedValue': 0,
                                'yearBorn': 1964},
                                {'age': 52,
                                'exercisedValue': 0,
                                'fiscalYear': 2019,
                                'maxAge': 1,
                                'name': "Ms. Deirdre  O'Brien",
                                'title': 'Sr. VP of People & Retail',
                                'totalPay': 2690253,
                                'unexercisedValue': 0,
                                'yearBorn': 1967}],
            'compensationAsOfEpochDate': '2019-12-30 17:00:00',
            'compensationRisk': 3,
            'country': 'United States',
            'fullTimeEmployees': 137000,
            'governanceEpochDate': '2019-12-06 17:00:00',
            'industry': 'Consumer Electronics',
            'longBusinessSummary': 'Apple Inc. designs, manufactures, and '
                                    'markets smartphones, personal computers, '
                                    'tablets, wearables, and accessories '
                                    'worldwide. It also sells various related '
                                    'services. The company offers iPhone, a line '
                                    'of smartphones; Mac, a line of personal '
                                    'computers; iPad, a line of multi-purpose '
                                    'tablets; and wearables, home, and '
                                    'accessories comprising AirPods, Apple TV, '
                                    'Apple Watch, Beats products, HomePod, iPod '
                                    'touch, and other Apple-branded and '
                                    'third-party accessories. It also provides '
                                    'digital content stores and streaming '
                                    'services; AppleCare support services; and '
                                    'iCloud, a cloud service, which stores music, '
                                    'photos, contacts, calendars, mail, '
                                    'documents, and others. In addition, the '
                                    'company offers various service, such as '
                                    'Apple Arcade, a game subscription service; '
                                    'Apple Card, a co-branded credit card; Apple '
                                    'News+, a subscription news and magazine '
                                    'service; and Apple Pay, a cashless payment '
                                    'service, as well as licenses its '
                                    'intellectual property, and provides other '
                                    'related services. The company serves '
                                    'consumers, and small and mid-sized '
                                    'businesses; and the education, enterprise, '
                                    'and government markets. It sells and '
                                    'delivers third-party applications for its '
                                    'products through the App Store, Mac App '
                                    'Store, and Watch App Store. The company also '
                                    'sells its products through its retail and '
                                    'online stores, and direct sales force; and '
                                    'third-party cellular network carriers, '
                                    'wholesalers, retailers, and resellers. Apple '
                                    'Inc. has a collaboration with Google to '
                                    'develop COVID-19 tracking system for Android '
                                    'and iOS devices. Apple Inc. was founded in '
                                    '1977 and is headquartered in Cupertino, '
                                    'California.',
            'maxAge': 86400,
            'overallRisk': 1,
            'phone': '408-996-1010',
            'sector': 'Technology',
            'shareHolderRightsRisk': 1,
            'state': 'CA',
            'website': 'http://www.apple.com',
            'zip': '95014'}}
    ```

### **calendar_events**

=== "Details"

    - *Description*:  Earnings and Revenue expectations for upcoming earnings date for given symbol(s)
    - *Module*:  `calendarEvents`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.calendar_events
    ```

=== "Data"

    ```python
    {
        'aapl': {
            'dividendDate': '2020-05-13 18:00:00',
            'earnings': {
                'earningsAverage': 2.04,
                'earningsDate': [1596067200],
                'earningsHigh': 2.47,
                'earningsLow': 1.67,
                'revenueAverage': 52247700000,
                'revenueHigh': 55838000000,
                'revenueLow': 48955000000
            },
            'exDividendDate': '2020-05-07 18:00:00',
            'maxAge': 1
        }
    }
    ```

### **company_officers**

=== "Details"

    - *Description*:  Retrieves top executives for given symbol(s) and their total pay package.
    - *Module*:  `assetProfile`
    - *Return*:  `pandas.DataFrame`

    !!! info
        This is a subset of the data returned from the `assetProfile` module

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.company_officers
    ```

=== "Data"

    |    | name                    |   age | title                       |   yearBorn |   fiscalYear |   totalPay |   exercisedValue |   unexercisedValue |
    |---:|:------------------------|------:|:----------------------------|-----------:|-------------:|-----------:|-----------------:|-------------------:|
    |  0 | Mr. Timothy D. Cook     |    58 | CEO & Director              |       1961 |         2019 |   11555466 |                0 |                  0 |
    |  1 | Mr. Luca  Maestri       |    55 | CFO & Sr. VP                |       1964 |         2019 |    3576221 |                0 |                  0 |
    |  2 | Mr. Jeffrey E. Williams |    55 | Chief Operating Officer     |       1964 |         2019 |    3574503 |                0 |                  0 |
    |  3 | Ms. Katherine L. Adams  |    55 | Sr. VP, Gen. Counsel & Sec. |       1964 |         2019 |    3598384 |                0 |                  0 |
    |  4 | Ms. Deirdre  O'Brien    |    52 | Sr. VP of People & Retail   |       1967 |         2019 |    2690253 |                0 |                  0 |

### **earning_history**

=== "Details"

    - *Description*:  Data related to historical earnings (actual vs. estimate) for given symbol(s)
    - *Module*:  `earningsHistory`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.earning_history
    ```

=== "Data"

    |    | symbol   |   row |   maxAge |   epsActual |   epsEstimate |   epsDifference |   surprisePercent | quarter    | period   |
    |---:|:---------|------:|---------:|------------:|--------------:|----------------:|------------------:|:-----------|:---------|
    |  0 | aapl     |     0 |        1 |        2.18 |          2.1  |            0.08 |             0.038 | 2019-06-30 | -4q      |
    |  1 | aapl     |     1 |        1 |        3.03 |          2.84 |            0.19 |             0.067 | 2019-09-30 | -3q      |
    |  2 | aapl     |     2 |        1 |        4.99 |          4.55 |            0.44 |             0.097 | 2019-12-31 | -2q      |
    |  3 | aapl     |     3 |        1 |        2.55 |          2.26 |            0.29 |             0.128 | 2020-03-31 | -1q      |

### **earnings**

=== "Details"

    - *Description*:  Historical earnings data for given symbol(s)
    - *Module*:  `earnings`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.earnings
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 86400,
            "earningsChart": {
                "quarterly": [{
                        "date": "2Q2019",
                        "actual": 2.18,
                        "estimate": 2.1
                    },
                    {
                        "date": "3Q2019",
                        "actual": 3.03,
                        "estimate": 2.84
                    },
                    {
                        "date": "4Q2019",
                        "actual": 4.99,
                        "estimate": 4.55
                    },
                    {
                        "date": "1Q2020",
                        "actual": 2.55,
                        "estimate": 2.26
                    }
                ],
                "currentQuarterEstimate": 2.04,
                "currentQuarterEstimateDate": "2Q",
                "currentQuarterEstimateYear": 2020,
                "earningsDate": [
                    1596067200
                ]
            },
            "financialsChart": {
                "yearly": [{
                        "date": 2016,
                        "revenue": 215639000000,
                        "earnings": 45687000000
                    },
                    {
                        "date": 2017,
                        "revenue": 229234000000,
                        "earnings": 48351000000
                    },
                    {
                        "date": 2018,
                        "revenue": 265595000000,
                        "earnings": 59531000000
                    },
                    {
                        "date": 2019,
                        "revenue": 260174000000,
                        "earnings": 55256000000
                    }
                ],
                "quarterly": [{
                        "date": "2Q2019",
                        "revenue": 53809000000,
                        "earnings": 10044000000
                    },
                    {
                        "date": "3Q2019",
                        "revenue": 64040000000,
                        "earnings": 13686000000
                    },
                    {
                        "date": "4Q2019",
                        "revenue": 91819000000,
                        "earnings": 22236000000
                    },
                    {
                        "date": "1Q2020",
                        "revenue": 58313000000,
                        "earnings": 11249000000
                    }
                ]
            },
            "financialCurrency": "USD"
        }
    }
    ```

### **earnings_trend**

=== "Details"

    - *Description*:  Historical trend data for earnings and revenue estimations for given symbol(s)
    - *Module*:  `earningsTrend `
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.earnings_trend
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "trend": [{
                    "maxAge": 1,
                    "period": "0q",
                    "endDate": "2020-06-30",
                    "growth": -0.064,
                    "earningsEstimate": {
                        "avg": 2.04,
                        "low": 1.67,
                        "high": 2.47,
                        "yearAgoEps": 2.18,
                        "numberOfAnalysts": 31,
                        "growth": -0.064
                    },
                    "revenueEstimate": {
                        "avg": 52247700000,
                        "low": 48955000000,
                        "high": 55838000000,
                        "numberOfAnalysts": 27,
                        "yearAgoRevenue": 53809000000,
                        "growth": -0.029000001
                    },
                    "epsTrend": {
                        "current": 2.04,
                        "7daysAgo": 2.02,
                        "30daysAgo": 2,
                        "60daysAgo": 2,
                        "90daysAgo": 2.07
                    },
                    "epsRevisions": {
                        "upLast7days": 4,
                        "upLast30days": 10,
                        "downLast30days": 0,
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+1q",
                    "endDate": "2020-09-30",
                    "growth": -0.083000004,
                    "earningsEstimate": {
                        "avg": 2.78,
                        "low": 2.09,
                        "high": 3.64,
                        "yearAgoEps": 3.03,
                        "numberOfAnalysts": 30,
                        "growth": -0.083000004
                    },
                    "revenueEstimate": {
                        "avg": 61536000000,
                        "low": 50471000000,
                        "high": 73554000000,
                        "numberOfAnalysts": 28,
                        "yearAgoRevenue": 64040000000,
                        "growth": -0.039
                    },
                    "epsTrend": {
                        "current": 2.78,
                        "7daysAgo": 2.81,
                        "30daysAgo": 2.83,
                        "60daysAgo": 2.8,
                        "90daysAgo": 2.91
                    },
                    "epsRevisions": {
                        "upLast7days": 3,
                        "upLast30days": 5,
                        "downLast30days": 1,
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "0y",
                    "endDate": "2020-09-30",
                    "growth": 0.045,
                    "earningsEstimate": {
                        "avg": 12.43,
                        "low": 11.89,
                        "high": 13.69,
                        "yearAgoEps": 11.89,
                        "numberOfAnalysts": 37,
                        "growth": 0.045
                    },
                    "revenueEstimate": {
                        "avg": 264098000000,
                        "low": 254618000000,
                        "high": 279524000000,
                        "numberOfAnalysts": 35,
                        "yearAgoRevenue": 260174000000,
                        "growth": 0.015
                    },
                    "epsTrend": {
                        "current": 12.43,
                        "7daysAgo": 12.42,
                        "30daysAgo": 12.4,
                        "60daysAgo": 12.32,
                        "90daysAgo": 12.23
                    },
                    "epsRevisions": {
                        "upLast7days": 3,
                        "upLast30days": 9,
                        "downLast30days": 1,
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+1y",
                    "endDate": "2021-09-30",
                    "growth": 0.204,
                    "earningsEstimate": {
                        "avg": 14.97,
                        "low": 12.59,
                        "high": 16.95,
                        "yearAgoEps": 12.43,
                        "numberOfAnalysts": 37,
                        "growth": 0.204
                    },
                    "revenueEstimate": {
                        "avg": 297911000000,
                        "low": 271687000000,
                        "high": 323720000000,
                        "numberOfAnalysts": 35,
                        "yearAgoRevenue": 264098000000,
                        "growth": 0.128
                    },
                    "epsTrend": {
                        "current": 14.97,
                        "7daysAgo": 14.94,
                        "30daysAgo": 14.85,
                        "60daysAgo": 14.73,
                        "90daysAgo": 14.79
                    },
                    "epsRevisions": {
                        "upLast7days": 3,
                        "upLast30days": 11,
                        "downLast30days": 1,
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+5y",
                    "endDate": null,
                    "growth": 0.1099,
                    "earningsEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "yearAgoEps": {},
                        "numberOfAnalysts": {},
                        "growth": {}
                    },
                    "revenueEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "numberOfAnalysts": {},
                        "yearAgoRevenue": {},
                        "growth": {}
                    },
                    "epsTrend": {
                        "current": {},
                        "7daysAgo": {},
                        "30daysAgo": {},
                        "60daysAgo": {},
                        "90daysAgo": {}
                    },
                    "epsRevisions": {
                        "upLast7days": {},
                        "upLast30days": {},
                        "downLast30days": {},
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "-5y",
                    "endDate": null,
                    "growth": 0.08415,
                    "earningsEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "yearAgoEps": {},
                        "numberOfAnalysts": {},
                        "growth": {}
                    },
                    "revenueEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "numberOfAnalysts": {},
                        "yearAgoRevenue": {},
                        "growth": {}
                    },
                    "epsTrend": {
                        "current": {},
                        "7daysAgo": {},
                        "30daysAgo": {},
                        "60daysAgo": {},
                        "90daysAgo": {}
                    },
                    "epsRevisions": {
                        "upLast7days": {},
                        "upLast30days": {},
                        "downLast30days": {},
                        "downLast90days": {}
                    }
                }
            ],
            "maxAge": 1
        }
    }
    ```

### **esg_scores**

=== "Details"

    - *Description*:  Data related to a given symbol(s) environmental, social, and governance metrics
    - *Module*:  `esgScores`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.esg_scores
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 86400,
            "totalEsg": 23.62,
            "environmentScore": 0.49,
            "socialScore": 12.98,
            "governanceScore": 10.15,
            "ratingYear": 2020,
            "ratingMonth": 7,
            "highestControversy": 3,
            "esgPerformance": "AVG_PERF",
            "peerCount": 57,
            "peerGroup": "Technology Hardware",
            "relatedControversy": [
                "Social Supply Chain Incidents",
                "Customer Incidents",
                "Business Ethics Incidents"
            ],
            "peerEsgScorePerformance": {
                "min": 8.59,
                "avg": 17.345438596491228,
                "max": 26.24
            },
            "peerGovernancePerformance": {
                "min": 3.89,
                "avg": 7.5931578947368426,
                "max": 13.36
            },
            "peerSocialPerformance": {
                "min": 2.69,
                "avg": 6.5699999999999985,
                "max": 12.98
            },
            "peerEnvironmentPerformance": {
                "min": 0.1,
                "avg": 3.1815789473684215,
                "max": 10.02
            },
            "peerHighestControversyPerformance": {
                "min": 0,
                "avg": 1.543859649122807,
                "max": 4
            },
            "percentile": 33.02,
            "environmentPercentile": 0,
            "socialPercentile": 0,
            "governancePercentile": 0,
            "adult": false,
            "alcoholic": false,
            "animalTesting": false,
            "catholic": false,
            "controversialWeapons": false,
            "smallArms": false,
            "furLeather": false,
            "gambling": false,
            "gmo": false,
            "militaryContract": false,
            "nuclear": false,
            "pesticides": false,
            "palmOil": false,
            "coal": false,
            "tobacco": false
        }
    }
    ```

### **financial_data**

=== "Details"

    - *Description*:  Financial KPIs for given symbol(s)
    - *Module*:  `financialData `
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.financial_data
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 86400,
            "currentPrice": 380.16,
            "targetHighPrice": 450,
            "targetLowPrice": 195.43,
            "targetMeanPrice": 371.96,
            "targetMedianPrice": 400,
            "recommendationMean": 2.1,
            "recommendationKey": "buy",
            "numberOfAnalystOpinions": 38,
            "totalCash": 94051000320,
            "totalCashPerShare": 21.699,
            "ebitda": 77305004032,
            "totalDebt": 118760996864,
            "quickRatio": 1.298,
            "currentRatio": 1.496,
            "totalRevenue": 267980996608,
            "debtToEquity": 151.433,
            "revenuePerShare": 60.097,
            "returnOnAssets": 0.12377,
            "returnOnEquity": 0.62094,
            "grossProfits": 98392000000,
            "freeCashflow": 45040123904,
            "operatingCashflow": 75373002752,
            "earningsGrowth": 0.037,
            "revenueGrowth": 0.005,
            "grossMargins": 0.3811,
            "ebitdaMargins": 0.28847,
            "operatingMargins": 0.24475999,
            "profitMargins": 0.21350001,
            "financialCurrency": "USD"
        }
    }
    ```

### **fund_bond_holdings**

=== "Details"

    - *Description*:  Retrieves aggregated maturity and duration information for a given symbol(s)
    - *Module*:  `topHoldings`
    - *Return*:  `pandas.DataFrame`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('vbmfx')
    fund.fund_bond_holdings
    ```

=== "Data"

    ```python
    {
        "vbmfx": {
            "maturity": 8.1,
            "duration": 6.21,
            "maturityCat": 7.48,
            "durationCat": 5.34
        }
    }
    ```

### **fund_bond_ratings**

=== "Details"

    - *Description*:  Retrieves aggregated maturity and duration information for a given symbol(s)
    - *Module*:  `topHoldings`
    - *Return*:  `pandas.DataFrame`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    funds = Ticker('vbmfx vicbx vstbx vwehx')
    funds.fund_bond_holdings
    ```

=== "Data"

    |               |   vbmfx |   vicbx |   vstbx |   vwehx |
    |:--------------|--------:|--------:|--------:|--------:|
    | bb            |  0      |  0      |  0      |  0.4992 |
    | aa            |  0.0343 |  0.055  |  0.1114 | -0.0002 |
    | aaa           |  0.6755 |  0.0134 |  0.0146 |  0.0372 |
    | a             |  0.1137 |  0.3697 |  0.4214 |  0      |
    | other         |  0      |  0      |  0      |  0.0346 |
    | b             |  0      |  0      |  0      |  0.3291 |
    | bbb           |  0.1765 |  0.5619 |  0.4526 |  0.0448 |
    | below_b       |  0      |  0      |  0      |  0.0553 |
    | us_government |  0      |  0      |  0      |  0      |

### **fund_equity_holdings**

=== "Details"

    - *Description*:  Retrieves aggregated priceTo____ data for a given symbol(s)
    - *Module*:  `topHoldings`
    - *Return*:  `dict`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('hasgx')
    fund.fund_equity_holdings
    ```

=== "Data"

    ```python
    {
        "hasgx": {
            "priceToEarnings": 25.46,
            "priceToBook": 3.67,
            "priceToSales": 1.82,
            "priceToCashflow": 15.61,
            "medianMarketCap": 4411.09,
            "threeYearEarningsGrowth": 19.57,
            "priceToEarningsCat": 29.37,
            "priceToBookCat": 4.16,
            "priceToSalesCat": 2.65,
            "priceToCashflowCat": 19.68,
            "medianMarketCapCat": 4485.81,
            "threeYearEarningsGrowthCat": 20.39
        }
    }
    ```

### **fund_holding_info**

=== "Details"

    - *Description*:  Contains information for a funds top holdings, bond ratings, bond holdings, equity holdings, sector weightings, and category breakdown
    - *Module*:  `topHoldings`
    - *Return*:  `dict`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('hasgx')
    fund.fund_holding_info
    ```

=== "Data"

    ```python
    {
        "hasgx": {
            "maxAge": 1,
            "cashPosition": 0.0301,
            "stockPosition": 0.96989995,
            "bondPosition": 0,
            "otherPosition": 0,
            "preferredPosition": 0,
            "convertiblePosition": 0,
            "holdings": [{
                    "symbol": "ICLR",
                    "holdingName": "Icon PLC",
                    "holdingPercent": 0.028199999
                },
                {
                    "symbol": "BIO",
                    "holdingName": "Bio-Rad Laboratories Inc",
                    "holdingPercent": 0.0276
                },
                {
                    "symbol": "BLD",
                    "holdingName": "TopBuild Corp",
                    "holdingPercent": 0.0238
                },
                {
                    "symbol": "ASND",
                    "holdingName": "Ascendis Pharma A/S ADR",
                    "holdingPercent": 0.0228
                },
                {
                    "symbol": "TREX",
                    "holdingName": "Trex Co Inc",
                    "holdingPercent": 0.0219
                },
                {
                    "symbol": "TKR",
                    "holdingName": "The Timken Co",
                    "holdingPercent": 0.0215
                },
                {
                    "symbol": "MIME",
                    "holdingName": "Mimecast Ltd",
                    "holdingPercent": 0.020299999
                },
                {
                    "symbol": "TDY",
                    "holdingName": "Teledyne Technologies Inc",
                    "holdingPercent": 0.0198
                },
                {
                    "symbol": "ERI",
                    "holdingName": "Eldorado Resorts Inc",
                    "holdingPercent": 0.0196
                },
                {
                    "symbol": "",
                    "holdingName": "The Medicines Co",
                    "holdingPercent": 0.0194
                }
            ],
            "equityHoldings": {
                "priceToEarnings": 25.46,
                "priceToBook": 3.67,
                "priceToSales": 1.82,
                "priceToCashflow": 15.61,
                "medianMarketCap": 4411.09,
                "threeYearEarningsGrowth": 19.57,
                "priceToEarningsCat": 29.37,
                "priceToBookCat": 4.16,
                "priceToSalesCat": 2.65,
                "priceToCashflowCat": 19.68,
                "medianMarketCapCat": 4485.81,
                "threeYearEarningsGrowthCat": 20.39
            },
            "bondHoldings": {},
            "bondRatings": [{
                    "bb": 0
                },
                {
                    "aa": 0
                },
                {
                    "aaa": 0
                },
                {
                    "a": 0
                },
                {
                    "other": 0
                },
                {
                    "b": 0
                },
                {
                    "bbb": 0
                },
                {
                    "below_b": 0
                },
                {
                    "us_government": 0
                }
            ],
            "sectorWeightings": [{
                    "realestate": 0.0299
                },
                {
                    "consumer_cyclical": 0.105299994
                },
                {
                    "basic_materials": 0
                },
                {
                    "consumer_defensive": 0.0073
                },
                {
                    "technology": 0.24309999
                },
                {
                    "communication_services": 0.0312
                },
                {
                    "financial_services": 0.0889
                },
                {
                    "utilities": 0
                },
                {
                    "industrials": 0.1701
                },
                {
                    "energy": 0.031
                },
                {
                    "healthcare": 0.2933
                }
            ]
        }
    }
    ```

### **fund_ownership**

=== "Details"

    - *Description*:  Top 10 owners of a given symbol(s)
    - *Module*:  `fundOwnership`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.fund_ownership
    ```

=== "Data"

    |    | symbol   |   row |   maxAge | reportDate   | organization                                               |   pctHeld |   position |       value |
    |---:|:---------|------:|---------:|:-------------|:-----------------------------------------------------------|----------:|-----------:|------------:|
    |  0 | aapl     |     0 |        1 | 2020-03-31   | Vanguard Total Stock Market Index Fund                     |    0.0271 |  117298701 | 29827886677 |
    |  1 | aapl     |     1 |        1 | 2020-03-31   | Vanguard 500 Index Fund                                    |    0.0198 |   85980468 | 21863973207 |
    |  2 | aapl     |     2 |        1 | 2020-05-31   | SPDR S&P 500 ETF Trust                                     |    0.0103 |   44553380 | 14165301637 |
    |  3 | aapl     |     3 |        1 | 2020-05-31   | Invesco ETF Tr-Invesco QQQ Tr, Series 1 ETF                |    0.0089 |   38712448 | 12308235717 |
    |  4 | aapl     |     4 |        1 | 2020-03-31   | Vanguard Institutional Index Fund-Institutional Index Fund |    0.0085 |   36959990 |  9398555857 |
    |  5 | aapl     |     5 |        1 | 2020-05-31   | Fidelity 500 Index Fund                                    |    0.0085 |   36919886 | 11738308554 |
    |  6 | aapl     |     6 |        1 | 2020-04-30   | iShares Core S&P 500 ETF                                   |    0.0073 |   31473783 |  9246997445 |
    |  7 | aapl     |     7 |        1 | 2020-03-31   | Vanguard Growth Index Fund                                 |    0.007  |   30336895 |  7714369029 |
    |  8 | aapl     |     8 |        1 | 2020-05-31   | Select Sector SPDR Fund-Technology                         |    0.0043 |   18642268 |  5927122687 |
    |  9 | aapl     |     9 |        1 | 2020-02-29   | Vanguard Information Technology Index Fund                 |    0.0043 |   18504465 |  5058380552 |

### **fund_performance**

=== "Details"

    - *Description*:  Historical return data for a given symbol(s) and symbol(s) specific category
    - *Module*:  `fundPerformance`
    - *Return*:  `dict`

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('hasgx')
    fund.fund_performance
    ```

=== "Data"

    ```python
    {
        "hasgx": {
            "maxAge": 1,
            "performanceOverview": {
                "asOfDate": "2019-02-04 00:00:00",
                "morningStarReturnRating": 3,
                "ytdReturnPct": 0.1441,
                "fiveYrAvgReturnPct": 0.0855,
                "numYearsUp": 14,
                "numYearsDown": 5,
                "bestOneYrTotalReturn": 0.44779998,
                "worstOneYrTotalReturn": -0.4042,
                "bestThreeYrTotalReturn": 0.44779998,
                "worstThreeYrTotalReturn": -0.0912
            },
            "performanceOverviewCat": {
                "ytdReturnPct": -0.001,
                "fiveYrAvgReturnPct": 0.0828
            },
            "loadAdjustedReturns": {
                "oneYear": 0.12060001,
                "threeYear": 0.1249,
                "fiveYear": 0.0877,
                "tenYear": 0.1383
            },
            "trailingReturns": {
                "asOfDate": "2020-06-30 00:00:00",
                "ytd": 0.0064999997,
                "oneMonth": 0.0294,
                "threeMonth": 0.3189,
                "oneYear": 0.12060001,
                "threeYear": 0.1249,
                "fiveYear": 0.0877,
                "tenYear": 0.1383,
                "lastBullMkt": 0.2784,
                "lastBearMkt": -0.2858
            },
            "trailingReturnsNav": {
                "ytd": 0,
                "oneMonth": 0,
                "threeMonth": 0,
                "oneYear": 0,
                "threeYear": 0,
                "fiveYear": 0,
                "tenYear": 0
            },
            "trailingReturnsCat": {
                "ytd": -0.001,
                "oneMonth": 0.038,
                "threeMonth": 0.32189998,
                "oneYear": 0.0446,
                "threeYear": 0.1008,
                "fiveYear": 0.0828,
                "tenYear": 0.1294,
                "lastBullMkt": 0.2792,
                "lastBearMkt": -0.24200001
            },
            "annualTotalReturns": {
                "returns": [{
                        "year": "2020"
                    },
                    {
                        "year": "2019",
                        "annualValue": 0.4233321
                    },
                    {
                        "year": "2018",
                        "annualValue": -0.107390605
                    },
                    {
                        "year": "2017",
                        "annualValue": 0.2460054
                    },
                    {
                        "year": "2016",
                        "annualValue": 0.062196396
                    },
                    {
                        "year": "2015",
                        "annualValue": -0.013101799
                    },
                    {
                        "year": "2014",
                        "annualValue": 0.0828115
                    },
                    {
                        "year": "2013",
                        "annualValue": 0.4478411
                    },
                    {
                        "year": "2012",
                        "annualValue": 0.1447442
                    },
                    {
                        "year": "2011",
                        "annualValue": -0.0766004
                    },
                    {
                        "year": "2010",
                        "annualValue": 0.3168667
                    },
                    {
                        "year": "2009",
                        "annualValue": 0.4008322
                    },
                    {
                        "year": "2008",
                        "annualValue": -0.4041542
                    },
                    {
                        "year": "2007",
                        "annualValue": 0.1363713
                    },
                    {
                        "year": "2006",
                        "annualValue": 0.1087122
                    },
                    {
                        "year": "2005",
                        "annualValue": 0.0564466
                    },
                    {
                        "year": "2004",
                        "annualValue": 0.1115022
                    },
                    {
                        "year": "2003",
                        "annualValue": 0.4439252
                    },
                    {
                        "year": "2002",
                        "annualValue": -0.200747
                    },
                    {
                        "year": "2001",
                        "annualValue": 0.0229226
                    }
                ],
                "returnsCat": [{
                        "year": "2019",
                        "annualValue": 0.27676532
                    },
                    {
                        "year": "2018",
                        "annualValue": -0.0576395
                    },
                    {
                        "year": "2017",
                        "annualValue": 0.2150002
                    },
                    {
                        "year": "2016",
                        "annualValue": 0.111996695
                    },
                    {
                        "year": "2015",
                        "annualValue": -0.0241295
                    },
                    {
                        "year": "2014",
                        "annualValue": 0.024365399
                    },
                    {
                        "year": "2013",
                        "annualValue": 0.40909082
                    },
                    {
                        "year": "2012",
                        "annualValue": 0.1314999
                    },
                    {
                        "year": "2011",
                        "annualValue": -0.0355412
                    },
                    {
                        "year": "2010",
                        "annualValue": 0.2698293
                    },
                    {
                        "year": "2009",
                        "annualValue": 0.3545617
                    },
                    {
                        "year": "2008",
                        "annualValue": -0.41551048
                    },
                    {
                        "year": "2007",
                        "annualValue": 0.075887196
                    },
                    {
                        "year": "2006",
                        "annualValue": 0.1081437
                    },
                    {
                        "year": "2005",
                        "annualValue": 0.060230598
                    },
                    {
                        "year": "2004",
                        "annualValue": 0.12409429
                    },
                    {
                        "year": "2003",
                        "annualValue": 0.45537603
                    },
                    {
                        "year": "2002",
                        "annualValue": -0.2787935
                    },
                    {
                        "year": "2001",
                        "annualValue": -0.0891243
                    },
                    {
                        "year": "2000",
                        "annualValue": -0.0384997
                    },
                    {
                        "year": "1999",
                        "annualValue": 0.64770126
                    },
                    {
                        "year": "1998",
                        "annualValue": 0.0523461
                    },
                    {
                        "year": "1997",
                        "annualValue": 0.1741466
                    },
                    {
                        "year": "1996",
                        "annualValue": 0.18674481
                    },
                    {
                        "year": "1995",
                        "annualValue": 0.3614976
                    },
                    {
                        "year": "1994",
                        "annualValue": -0.0051973998
                    },
                    {
                        "year": "1993",
                        "annualValue": 0.17361571
                    },
                    {
                        "year": "1992",
                        "annualValue": 0.1094542
                    },
                    {
                        "year": "1991",
                        "annualValue": 0.5725298
                    },
                    {
                        "year": "1990",
                        "annualValue": -0.0984044
                    },
                    {
                        "year": "1989",
                        "annualValue": 0.2626742
                    },
                    {
                        "year": "1988",
                        "annualValue": 0.18222731
                    },
                    {
                        "year": "1987",
                        "annualValue": -0.0370497
                    },
                    {
                        "year": "1986",
                        "annualValue": 0.099111795
                    },
                    {
                        "year": "1985",
                        "annualValue": 0.2643012
                    },
                    {
                        "year": "1984",
                        "annualValue": -0.104290105
                    },
                    {
                        "year": "1983",
                        "annualValue": 0.2495246
                    },
                    {
                        "year": "1982",
                        "annualValue": 0.2308341
                    },
                    {
                        "year": "1981",
                        "annualValue": 0.0207251
                    },
                    {
                        "year": "1980",
                        "annualValue": 0.3761657
                    },
                    {
                        "year": "1979",
                        "annualValue": 0.3690657
                    },
                    {
                        "year": "1978",
                        "annualValue": 0.1781299
                    },
                    {
                        "year": "1977",
                        "annualValue": 0.1065682
                    },
                    {
                        "year": "1976",
                        "annualValue": 0.3378357
                    },
                    {
                        "year": "1975",
                        "annualValue": 0.3783118
                    },
                    {
                        "year": "1974",
                        "annualValue": -0.3575943
                    },
                    {
                        "year": "1973",
                        "annualValue": -0.3001683
                    },
                    {
                        "year": "1972",
                        "annualValue": 0.1025676
                    },
                    {
                        "year": "1971",
                        "annualValue": 0.19541731
                    },
                    {
                        "year": "1970",
                        "annualValue": -0.1831704
                    },
                    {
                        "year": "1969",
                        "annualValue": -0.16133231
                    },
                    {
                        "year": "1968",
                        "annualValue": 0.1150183
                    },
                    {
                        "year": "1967",
                        "annualValue": 0.5074166
                    },
                    {
                        "year": "1966",
                        "annualValue": -0.0137236
                    },
                    {
                        "year": "1965",
                        "annualValue": 0.2515068
                    },
                    {
                        "year": "1964",
                        "annualValue": 0.100048
                    },
                    {
                        "year": "1963",
                        "annualValue": 0.1902171
                    },
                    {
                        "year": "1962",
                        "annualValue": -0.2464827
                    },
                    {
                        "year": "1961",
                        "annualValue": 0.35685748
                    },
                    {
                        "year": "1960",
                        "annualValue": 0.0359799
                    },
                    {
                        "year": "1959",
                        "annualValue": 0.1342513
                    },
                    {
                        "year": "1958",
                        "annualValue": 0.47772512
                    },
                    {
                        "year": "1957",
                        "annualValue": -0.17027621
                    },
                    {
                        "year": "1956",
                        "annualValue": 0.0318841
                    },
                    {
                        "year": "1955",
                        "annualValue": 0.1480865
                    },
                    {
                        "year": "1954",
                        "annualValue": 0.2599581
                    },
                    {
                        "year": "1953",
                        "annualValue": -0.0041754004
                    },
                    {
                        "year": "1952",
                        "annualValue": 0.098623894
                    },
                    {
                        "year": "1951",
                        "annualValue": 0.0927318
                    },
                    {
                        "year": "1950",
                        "annualValue": 0.1735294
                    },
                    {
                        "year": "1949",
                        "annualValue": 0.09324761
                    },
                    {
                        "year": "1948",
                        "annualValue": -0.0220126
                    },
                    {
                        "year": "1947",
                        "annualValue": -0.0154799
                    }
                ]
            },
            "pastQuarterlyReturns": {
                "returns": [{
                        "year": "2020",
                        "q1": -0.23689881,
                        "q2": 0.3189087
                    },
                    {
                        "year": "2019",
                        "q1": 0.2161895,
                        "q2": 0.051136397,
                        "q3": -0.0162162,
                        "q4": 0.13173899
                    },
                    {
                        "year": "2018",
                        "q1": 0.0388619,
                        "q2": 0.0394122,
                        "q3": 0.0745501,
                        "q4": -0.23071171
                    },
                    {
                        "year": "2017",
                        "q1": 0.0800628,
                        "q2": 0.0363372,
                        "q3": 0.0406732,
                        "q4": 0.0696838
                    },
                    {
                        "year": "2016",
                        "q1": -0.0721992,
                        "q2": 0.029517,
                        "q3": 0.0834057,
                        "q4": 0.026420701
                    },
                    {
                        "year": "2015",
                        "q1": 0.0832127,
                        "q2": 0.012692099,
                        "q3": -0.14182061,
                        "q4": 0.0483423
                    },
                    {
                        "year": "2014",
                        "q1": 0.0207636,
                        "q2": -0.0013123,
                        "q3": -0.022339001,
                        "q4": 0.0864499
                    },
                    {
                        "year": "2013",
                        "q1": 0.1510549,
                        "q2": 0.043255102,
                        "q3": 0.0843289,
                        "q4": 0.1119194
                    },
                    {
                        "year": "2012",
                        "q1": 0.114889696,
                        "q2": -0.049464103,
                        "q3": 0.0633131,
                        "q4": 0.015890501
                    },
                    {
                        "year": "2011",
                        "q1": 0.0738151,
                        "q2": 0.0028944002,
                        "q3": -0.2590188,
                        "q4": 0.1571717
                    },
                    {
                        "year": "2010",
                        "q1": 0.0960396,
                        "q2": -0.089430906,
                        "q3": 0.140873,
                        "q4": 0.1565525
                    },
                    {
                        "year": "2009",
                        "q1": -0.0790569,
                        "q2": 0.1957831,
                        "q3": 0.1876574,
                        "q4": 0.0710498
                    },
                    {
                        "year": "2008",
                        "q1": -0.1254996,
                        "q2": 0.0585009,
                        "q3": -0.1200345,
                        "q4": -0.2684955
                    },
                    {
                        "year": "2007",
                        "q1": 0.0392465,
                        "q2": 0.0422961,
                        "q3": 0.026087001,
                        "q4": 0.0224132
                    },
                    {
                        "year": "2006",
                        "q1": 0.15329629,
                        "q2": -0.0716253,
                        "q3": -0.0333828,
                        "q4": 0.071273
                    },
                    {
                        "year": "2005",
                        "q1": -0.0541796,
                        "q2": 0.0515548,
                        "q3": 0.0529183,
                        "q4": 0.0088167
                    },
                    {
                        "year": "2004",
                        "q1": 0.0857605,
                        "q2": -0.009687,
                        "q3": -0.0579383,
                        "q4": 0.0972977
                    },
                    {
                        "year": "2003",
                        "q1": -0.029205598,
                        "q2": 0.2154031,
                        "q3": 0.0910891,
                        "q4": 0.1215971
                    },
                    {
                        "year": "2002",
                        "q1": 0.0289449,
                        "q2": -0.0825771,
                        "q3": -0.18397631,
                        "q4": 0.0375758
                    },
                    {
                        "year": "2001",
                        "q1": -0.1203438,
                        "q2": 0.1921824,
                        "q3": -0.1575592,
                        "q4": 0.15783781
                    }
                ]
            },
            "rankInCategory": {
                "ytd": 43,
                "oneMonth": 68,
                "threeMonth": 48,
                "oneYear": 23,
                "threeYear": 36,
                "fiveYear": 46
            },
            "riskOverviewStatistics": {
                "riskRating": 4,
                "riskStatistics": [{
                        "year": "5y",
                        "alpha": -3.56,
                        "beta": 1.27,
                        "meanAnnualReturn": 0.88,
                        "rSquared": 85.23,
                        "stdDev": 20.38,
                        "sharpeRatio": 0.46,
                        "treynorRatio": 5.97
                    },
                    {
                        "year": "3y",
                        "alpha": 0,
                        "beta": 1.28,
                        "meanAnnualReturn": 1.21,
                        "rSquared": 89.76,
                        "stdDev": 22.94,
                        "sharpeRatio": 0.56,
                        "treynorRatio": 8.42
                    },
                    {
                        "year": "10y",
                        "alpha": -3.2,
                        "beta": 1.3,
                        "meanAnnualReturn": 1.24,
                        "rSquared": 82.18,
                        "stdDev": 19.24,
                        "sharpeRatio": 0.74,
                        "treynorRatio": 10.17
                    }
                ]
            },
            "riskOverviewStatisticsCat": {
                "riskStatisticsCat": [{
                        "year": "5y",
                        "alpha": -0.035099998,
                        "beta": 0.012200001,
                        "meanAnnualReturn": 0.0084,
                        "rSquared": 0.78370005,
                        "stdDev": 0.2039,
                        "sharpeRatio": 0.0044,
                        "treynorRatio": 0.059
                    },
                    {
                        "year": "3y",
                        "alpha": -0.0187,
                        "beta": 0.0124,
                        "meanAnnualReturn": 0.010199999,
                        "rSquared": 0.8205,
                        "stdDev": 0.2327,
                        "sharpeRatio": 0.0045,
                        "treynorRatio": 0.0686
                    },
                    {
                        "year": "10y",
                        "alpha": -0.0294,
                        "beta": 0.0121,
                        "meanAnnualReturn": 0.0116,
                        "rSquared": 0.7644,
                        "stdDev": 0.1864,
                        "sharpeRatio": 0.0072000003,
                        "treynorRatio": 0.102299996
                    }
                ]
            }
        }
    }
    ```

### **fund_profile**

=== "Details"

    - *Description*:  Summary level information for a given symbol(s)
    - *Module*:  `fundProfile`
    - *Return*:  `dict`

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('hasgx')
    fund.fund_profile
    ```

=== "Data"

    ```python
    {
        "hasgx": {
            "maxAge": 1,
            "styleBoxUrl": "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq6.gif",
            "family": "Harbor",
            "categoryName": "Small Growth",
            "legalType": null,
            "managementInfo": {
                "managerName": "William A. Muggia",
                "managerBio": "Will joined Westfield Capital Management in April 1994. In addition to his executive duties, he chairs the Investment Committee, serves as Market Strategist and contributes investment ideas primarily within the Health Care and Energy sectors.\n\nIn 2001, Will was promoted to President and Chief Investment Officer and now oversees all of Westfield's US equity and hedge fund strategies. In this role, Will and his team have grown the firm from $2 billion to $13 billion in assets under management.\n\nPrior to joining Westfield, Will worked in the Technology Investment Banking Group at Alex Brown & Sons, where his responsibilities included mergers and acquisitions, restructuring, and spin-offs. Before that, he was a Vice President at Kidder, Peabody & Company.\n\nWill graduated from Middlebury College in 1983 and received a Masters in Business Administration from the Harvard Business School in 1992.\n\nWill and his family are very active in community service, focusing their efforts on education for underprivileged youth. He is a member of the Board of Directors of SquashBusters and the Advisory Board of The Base.",
                "startdate": 973036800
            },
            "feesExpensesInvestment": {
                "annualReportExpenseRatio": 0.0088,
                "netExpRatio": 0.0088,
                "grossExpRatio": 0.0088,
                "projectionValues": {
                    "5y": 488,
                    "3y": 281,
                    "10y": 1084
                }
            },
            "feesExpensesInvestmentCat": {
                "annualReportExpenseRatio": 0.012200001,
                "frontEndSalesLoad": 0.0541,
                "deferredSalesLoad": 0.013200001,
                "projectionValuesCat": {
                    "5y": 815.16,
                    "3y": 503.94,
                    "10y": 1700.96
                }
            },
            "initInvestment": 50000,
            "initIraInvestment": 500,
            "subseqInvestment": 0,
            "brokerages": [
                "TradeStation Securities",
                "Northwestern Mutual Inv Srvc, LLC",
                "Cetera Advisors LLC",
                "Cetera Advisor Networks LLC",
                "Pruco Securities, LLC",
                "Protected Investors of America",
                "Comerica Bank",
                "Mid Atlantic Capital Corp",
                "Morgan Stanley - Brokerage Accounts",
                "Pershing FundCenter",
                "Schwab Institutional",
                "Td Ameritrade, Inc.",
                "TD Ameritrade Institutional Services",
                "Scottrade Load",
                "Shareholders Services Group",
                "JPMorgan",
                "Merrill Lynch",
                "Vanguard",
                "TD Ameritrade Trust Company",
                "CommonWealth PPS",
                "LPL SAM Eligible",
                "Fidelity Retail FundsNetwork",
                "Fidelity Institutional FundsNetwork",
                "Schwab Retail",
                "DATALynx",
                "PruChoice Investments",
                "Ameriprise Brokerage",
                "Federated TrustConnect",
                "Cetera Advisors LLC- PAM, PRIME, Premier",
                "Cetera Advisor Networks LLC- PAM, PRIME, Premier",
                "Schwab RPS SDE",
                "Ameriprise SPS Advantage",
                "SunAmerica Securities Premier / Pinnacle",
                "ETrade No Load Fee",
                "SunGard Transaction Network",
                "Raymond James",
                "Raymond James WRAP Eligible",
                "Bear Stearns No-Load Transaction Fee",
                "Commonwealth Universe",
                "FTJ FundChoice",
                "Robert W. Baird & Co.",
                "TRUSTlynx",
                "JPMorgan INVEST",
                "WFA MF Advisory Updated 7/01/2020",
                "RBC Wealth Management-Network Eligible",
                "DailyAccess Corporation RTC",
                "DailyAccess Corporation FRIAG",
                "WR Hambrecht Co LLC",
                "Sterne, Agee & Leach, Inc.,",
                "Schwab RPS All",
                "ING Financial Ptnrs PAM and PRIME Approv",
                "Firstrade",
                "Scottrade TF",
                "Scottrade NTF",
                "Standard Retirement Services, Inc.",
                "TIAA-CREF Brokerage Services",
                "Thrivent   Advisory Eligible",
                "Matrix Financial Solutions",
                "Trade PMR Transaction Fee",
                "Trade PMR NTF",
                "Morgan Stanley - Ntwk/Rdm Only-Brokerage",
                "TD Ameritrade Retail",
                "TD Ameritrade Institutional",
                "NYLIM 401(k) Complete",
                "Met Life Resources MFSP Alliance List",
                "Mid Atlantic Capital Group",
                "HD Vest - Vest Advisor",
                "Securities America Advisors",
                "Bear Stearns",
                "Securities America Advisors Top Rated",
                "JP MORGAN NO-LOAD NTF",
                "JP MORGAN NO-LOAD TRANSACTION FEE",
                "TD Ameritrade Retail NTF",
                "TD Ameritrade Institutional NTF",
                "MSWM Brokerage",
                "WFA Fdntl Choice/PIM Updated 7/01/2020",
                "ADP Access Open Fund Architecture",
                "DailyAccess Corporation Mid-Atlantic",
                "Waddell & Reed Choice MAP Flex",
                "ING Financial Partners Inc.",
                "Vanguard Load",
                "Jiangsu Akcome Science & Technology Co Ltd",
                "Vanguard TF",
                "DailyAccess Corporation Matrix",
                "DailyAccess Corporation Schwab",
                "DailyAccess Corporation MATC",
                "Cetera Financial Specialists LLC- Premier",
                "LPL SWM",
                "Schwab All (Retail, Instl, Retirement)",
                "Schwab Existing Shareholders Only",
                "Pershing Retirement Plan Network",
                "HD Vest",
                "Commonwealth (NTF)",
                "Commonwealth (PPS/Advisory)"
            ]
        }
    }
    ```

### **fund_sector_weightings**

=== "Details"

    - *Description*:  Retrieves aggregated sector weightings for a given symbol(s)
    - *Module*:  `topHoldings`
    - *Return*:  `pandas.DataFrame`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    funds = Ticker('hasgx dodgx cipnx')
    funds.fund_sector_weightings
    ```

=== "Data"

    |    | sector                 |   hasgx |   dodgx |   cipnx |
    |---:|:-----------------------|--------:|--------:|--------:|
    |  0 | realestate             |  0.0299 |  0      |  0      |
    |  1 | consumer_cyclical      |  0.1053 |  0.0325 |  0.0377 |
    |  2 | basic_materials        |  0      |  0.0083 |  0.0497 |
    |  3 | consumer_defensive     |  0.0073 |  0.0113 |  0.1815 |
    |  4 | technology             |  0.2431 |  0.1928 |  0.2064 |
    |  5 | communication_services |  0.0312 |  0.1311 |  0.0188 |
    |  6 | financial_services     |  0.0889 |  0.2629 |  0.1424 |
    |  7 | utilities              |  0      |  0      |  0      |
    |  8 | industrials            |  0.1701 |  0.0616 |  0.1368 |
    |  9 | energy                 |  0.031  |  0.0656 |  0      |
    | 10 | healthcare             |  0.2933 |  0.2339 |  0.2267 |

### **fund_top_holdings**

=== "Details"

    - *Description*:  Retrieves Top 10 holdings for a given symbol(s)
    - *Module*:  `topHoldings`
    - *Return*:  `pandas.DataFrame`

    !!! info
        This is a subset of the data returned from the `topHoldings` module

    !!! warning
        This endpoint will only return data for specific securities (funds and etfs)

=== "Example"

    ```python hl_lines="2"
    fund = Ticker('hasgx')
    fund.fund_top_holdings
    ```

=== "Data"

    |              | symbol   | holdingName               |   holdingPercent |
    |:-------------|:---------|:--------------------------|-----------------:|
    | ('hasgx', 0) | ICLR     | Icon PLC                  |           0.0282 |
    | ('hasgx', 1) | BIO      | Bio-Rad Laboratories Inc  |           0.0276 |
    | ('hasgx', 2) | BLD      | TopBuild Corp             |           0.0238 |
    | ('hasgx', 3) | ASND     | Ascendis Pharma A/S ADR   |           0.0228 |
    | ('hasgx', 4) | TREX     | Trex Co Inc               |           0.0219 |
    | ('hasgx', 5) | TKR      | The Timken Co             |           0.0215 |
    | ('hasgx', 6) | MIME     | Mimecast Ltd              |           0.0203 |
    | ('hasgx', 7) | TDY      | Teledyne Technologies Inc |           0.0198 |
    | ('hasgx', 8) | ERI      | Eldorado Resorts Inc      |           0.0196 |
    | ('hasgx', 9) |          | The Medicines Co          |           0.0194 |

### **grading_history**

=== "Details"

    - *Description*:  Data related to upgrades / downgrades by companies for a given symbol(s)
    - *Module*:  `upgradeDowngradeHistory `
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    df = aapl.grading_history
    df.head()
    ```

=== "Data"

    |    | symbol   |   row | epochGradeDate      | firm           | toGrade    | fromGrade   | action   |
    |---:|:---------|------:|:--------------------|:---------------|:-----------|:------------|:---------|
    |  0 | aapl     |     0 | 2020-07-29 08:37:18 | Credit Suisse  | Neutral    |             | main     |
    |  1 | aapl     |     1 | 2020-07-15 04:22:07 | Needham        | Buy        |             | main     |
    |  2 | aapl     |     2 | 2020-07-13 06:32:14 | Morgan Stanley | Overweight |             | main     |
    |  3 | aapl     |     3 | 2020-07-13 05:47:09 | Wedbush        | Outperform |             | main     |
    |  4 | aapl     |     4 | 2020-07-07 09:04:24 | Cascend        | Buy        |             | main     |

### **index_trend**

=== "Details"

    - *Description*:  Trend data related given symbol(s) index, specificially PE and PEG ratios
    - *Module*:  `indexTrend`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.index_trend
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 1,
            "symbol": "SP5",
            "peRatio": 39.5608,
            "pegRatio": 5.59807,
            "estimates": [{
                    "period": "0q",
                    "growth": -0.313
                },
                {
                    "period": "+1q",
                    "growth": -0.012999999
                },
                {
                    "period": "0y",
                    "growth": -0.199
                },
                {
                    "period": "+1y",
                    "growth": 0.301
                },
                {
                    "period": "+5y",
                    "growth": 0.0406009
                },
                {
                    "period": "-5y"
                }
            ]
        }
    }
    ```

### **industry_trend**

=== "Details"

    !!! warning
        Appears to no longer be in use

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.industry_trend
    ```

### **insider_holders**

=== "Details"

    - *Description*:  Data related to stock holdings of a given symbol(s) insiders
    - *Module*:  `insiderHolders`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.insider_holders
    ```

=== "Data"

    |    | symbol   |   row |   maxAge | name               | relation                | url   | transactionDescription                        | latestTransDate   |   positionDirect | positionDirectDate   |   positionIndirect |   positionIndirectDate |
    |---:|:---------|------:|---------:|:-------------------|:------------------------|:------|:----------------------------------------------|:------------------|-----------------:|:---------------------|-------------------:|-----------------------:|
    |  0 | aapl     |     0 |        1 | BELL JAMES A       | Director                |       | Conversion of Exercise of derivative security | 2020-01-31        |   7716           | 2020-01-31           |                nan |          nan           |
    |  1 | aapl     |     1 |        1 | GORE ALBERT A JR   | Director                |       | Conversion of Exercise of derivative security | 2020-01-31        | 115014           | 2020-01-31           |                nan |          nan           |
    |  2 | aapl     |     2 |        1 | JUNG ANDREA        | Director                |       | Conversion of Exercise of derivative security | 2020-04-28        |    nan           | nan                  |              33548 |            1.58803e+09 |
    |  3 | aapl     |     3 |        1 | KONDO CHRISTOPHER  | Officer                 |       | Sale                                          | 2020-05-08        |   7370           | 2020-05-08           |                nan |          nan           |
    |  4 | aapl     |     4 |        1 | LEVINSON ARTHUR D  | Director                |       | Sale                                          | 2020-02-03        |      1.14728e+06 | 2020-02-03           |                nan |          nan           |
    |  5 | aapl     |     5 |        1 | MAESTRI LUCA       | Chief Financial Officer |       | Sale                                          | 2020-04-07        |  27568           | 2020-04-07           |                nan |          nan           |
    |  6 | aapl     |     6 |        1 | O'BRIEN DEIRDRE    | Officer                 |       | Sale                                          | 2020-04-16        |  33972           | 2020-04-16           |                nan |          nan           |
    |  7 | aapl     |     7 |        1 | SUGAR RONALD D     | Director                |       | Conversion of Exercise of derivative security | 2020-01-31        |  24714           | 2020-01-31           |                nan |          nan           |
    |  8 | aapl     |     8 |        1 | WAGNER SUSAN L     | Director                |       | Conversion of Exercise of derivative security | 2020-01-31        |  14809           | 2020-01-31           |                nan |          nan           |
    |  9 | aapl     |     9 |        1 | WILLIAMS JEFFREY E | Chief Operating Officer |       | Sale                                          | 2020-04-02        | 122315           | 2020-04-02           |                nan |          nan           |

### **insider_transactions**

=== "Details"

    - *Description*:  Transactions by insiders for a given symbol(s)
    - *Module*:  `insiderTransactions`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    df = aapl.insider_transactions
    df.head()
    ```

=== "Data"

    |    | symbol   |   row |   maxAge |   shares |            value | filerUrl   | transactionText                                                         | filerName         | filerRelation   | moneyText   | startDate   | ownership   |
    |---:|:---------|------:|---------:|---------:|-----------------:|:-----------|:------------------------------------------------------------------------|:------------------|:----------------|:------------|:------------|:------------|
    |  0 | aapl     |     0 |        1 |     4491 |      1.37254e+06 |            | Sale at price 305.62 per share.                                         | KONDO CHRISTOPHER | Officer         |             | 2020-05-08  | D           |
    |  1 | aapl     |     1 |        1 |     9590 | 469389           |            | Conversion of Exercise of derivative security at price 48.95 per share. | JUNG ANDREA       | Director        |             | 2020-04-28  | I           |
    |  2 | aapl     |     2 |        1 |     9137 |      2.60514e+06 |            | Sale at price 283.82 - 286.82 per share.                                | O'BRIEN DEIRDRE   | Officer         |             | 2020-04-16  | D           |
    |  3 | aapl     |     3 |        1 |     5916 |    nan           |            |                                                                         | KONDO CHRISTOPHER | Officer         |             | 2020-04-15  | D           |
    |  4 | aapl     |     4 |        1 |    16634 |    nan           |            |                                                                         | O'BRIEN DEIRDRE   | Officer         |             | 2020-04-15  | D           |

### **institution_ownership**

=== "Details"

    - *Description*: Top 10 owners of a given symbol(s)
    - *Module*: `intitutionOwnership`
    - *Return*: `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.institution_ownership
    ```

=== "Data"

    |    | symbol   |   row |   maxAge | reportDate   | organization                      |   pctHeld |   position |       value |
    |---:|:---------|------:|---------:|:-------------|:----------------------------------|----------:|-----------:|------------:|
    |  0 | aapl     |     0 |        1 | 2020-03-31   | Vanguard Group, Inc. (The)        |    0.0777 |  336728608 | 85626717728 |
    |  1 | aapl     |     1 |        1 | 2020-03-31   | Blackrock Inc.                    |    0.0634 |  274684501 | 69849521759 |
    |  2 | aapl     |     2 |        1 | 2020-03-31   | Berkshire Hathaway, Inc           |    0.0566 |  245155566 | 62340608878 |
    |  3 | aapl     |     3 |        1 | 2020-03-31   | State Street Corporation          |    0.0417 |  180558954 | 45914336412 |
    |  4 | aapl     |     4 |        1 | 2020-03-31   | Advisor Group, Inc.               |    0.0269 |  116768396 | 29693035418 |
    |  5 | aapl     |     5 |        1 | 2020-03-31   | FMR, LLC                          |    0.0215 |   93376233 | 23744642289 |
    |  6 | aapl     |     6 |        1 | 2020-03-31   | Geode Capital Management, LLC     |    0.0148 |   64178586 | 16319972633 |
    |  7 | aapl     |     7 |        1 | 2020-03-31   | Price (T.Rowe) Associates Inc     |    0.013  |   56203762 | 14292054638 |
    |  8 | aapl     |     8 |        1 | 2020-03-31   | Northern Trust Corporation        |    0.0124 |   53859611 | 13695960481 |
    |  9 | aapl     |     9 |        1 | 2019-12-31   | Norges Bank Investment Management |    0.0108 |   46856273 | 13759344566 |

### **key_stats**

=== "Details"

    - *Description*:  KPIs for given symbol(s) (PE, enterprise value, EPS, EBITA, and more)
    - *Module*:  `defaultKeyStatistics `
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.key_stats
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 1,
            "priceHint": 2,
            "enterpriseValue": 1672450801664,
            "forwardPE": 25.70207,
            "profitMargins": 0.21350001,
            "floatShares": 4329740605,
            "sharesOutstanding": 4334329856,
            "sharesShort": 35234606,
            "sharesShortPriorMonth": 34828293,
            "sharesShortPreviousMonthDate": "2020-06-15 00:00:00",
            "dateShortInterest": "2020-07-15 00:00:00",
            "sharesPercentSharesOut": 0.0081,
            "heldPercentInsiders": 0.00066,
            "heldPercentInstitutions": 0.62115,
            "shortRatio": 0.96,
            "shortPercentOfFloat": 0.0081,
            "beta": 1.182072,
            "category": null,
            "bookValue": 18.137,
            "priceToBook": 21.214094,
            "fundFamily": null,
            "legalType": null,
            "lastFiscalYearEnd": "2019-09-28 00:00:00",
            "nextFiscalYearEnd": "2021-09-28 00:00:00",
            "mostRecentQuarter": "2020-03-28 00:00:00",
            "earningsQuarterlyGrowth": -0.027,
            "netIncomeToCommon": 57215000576,
            "trailingEps": 12.728,
            "forwardEps": 14.97,
            "pegRatio": 2.78,
            "lastSplitFactor": "7:1",
            "lastSplitDate": "2014-06-09 00:00:00",
            "enterpriseToRevenue": 6.241,
            "enterpriseToEbitda": 21.634,
            "52WeekChange": 0.8239218,
            "SandP52WeekChange": 0.103224516
        }
    }
    ```

### **major_holders**

=== "Details"

    - *Description*:  Data showing breakdown of owners of given symbol(s), insiders, institutions, etc.
    - *Module*:  `majorHoldersBreakdown `
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.major_holders
    ```

=== "Data"

    ```python
    {
        "maxAge": 1,
        "insidersPercentHeld": 0.00066,
        "institutionsPercentHeld": 0.62115,
        "institutionsFloatPercentHeld": 0.62156,
        "institutionsCount": 4296
    }
    ```

### **page_views**

=== "Details"

    - *Description*:  Short, Mid, and Long-term trend data regarding a symbol(s) page views
    - *Module*:  `pageViews`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.page_views
    ```

=== "Data"

    ```python
    {
        'aapl': {
            'shortTermTrend': 'UP',
            'midTermTrend': 'UP',
            'longTermTrend': 'UP',
            'maxAge': 1
        }
    }
    ```

### **price**

=== "Details"

    - *Description*:  Detailed pricing data for given symbol(s), exchange, quote type, currency, market cap, pre / post market data, etc.
    - *Module*:  `price`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.price
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 1,
            "preMarketChangePercent": -0.0090225,
            "preMarketChange": -3.42999,
            "preMarketTime": "2020-07-30 13:29:59",
            "preMarketPrice": 376.73,
            "preMarketSource": "FREE_REALTIME",
            "postMarketChangePercent": 0.05447549,
            "postMarketChange": 20.959991,
            "postMarketTime": 1596144518,
            "postMarketPrice": 405.72,
            "postMarketSource": "DELAYED",
            "regularMarketChangePercent": 0.012100184,
            "regularMarketChange": 4.600006,
            "regularMarketTime": "2020-07-30 20:00:01",
            "priceHint": 2,
            "regularMarketPrice": 384.76,
            "regularMarketDayHigh": 385.19,
            "regularMarketDayLow": 375.07,
            "regularMarketVolume": 30622619,
            "regularMarketPreviousClose": 380.16,
            "regularMarketSource": "FREE_REALTIME",
            "regularMarketOpen": 376.75,
            "exchange": "NMS",
            "exchangeName": "NasdaqGS",
            "exchangeDataDelayedBy": 0,
            "marketState": "POST",
            "quoteType": "EQUITY",
            "symbol": "AAPL",
            "underlyingSymbol": null,
            "shortName": "Apple Inc.",
            "longName": "Apple Inc.",
            "currency": "USD",
            "quoteSourceName": "Delayed Quote",
            "currencySymbol": "$",
            "fromCurrency": null,
            "toCurrency": null,
            "lastMarket": null,
            "marketCap": 1667676766208
        }
    }
    ```

### **quote_type**

=== "Details"

    - *Description*:  Stock exchange specific data for given symbol(s)
    - *Module*:  `quoteType`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.quote_type
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "exchange": "NMS",
            "quoteType": "EQUITY",
            "symbol": "AAPL",
            "underlyingSymbol": "AAPL",
            "shortName": "Apple Inc.",
            "longName": "Apple Inc.",
            "firstTradeDateEpochUtc": "1980-12-12 14:30:00",
            "timeZoneFullName": "America/New_York",
            "timeZoneShortName": "EDT",
            "uuid": "8b10e4ae-9eeb-3684-921a-9ab27e4d87aa",
            "messageBoardId": "finmb_24937",
            "gmtOffSetMilliseconds": -14400000,
            "maxAge": 1
        }
    }
    ```

### **recommendation_trend**

=== "Details"

    - *Description*:  Data related to historical recommendations (buy, hold, sell) for a given symbol(s)
    - *Module*:  `recommendationTrend`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.recommendation_trend
    ```

=== "Data"

    |             | period   |   strongBuy |   buy |   hold |   sell |   strongSell |
    |:------------|:---------|------------:|------:|-------:|-------:|-------------:|
    | ('aapl', 0) | 0m       |          11 |    21 |      6 |      0 |            0 |
    | ('aapl', 1) | -1m      |          12 |    17 |      8 |      2 |            0 |
    | ('aapl', 2) | -2m      |          12 |    17 |      7 |      3 |            0 |
    | ('aapl', 3) | -3m      |          13 |    10 |     18 |      3 |            0 |

### **sec_filings**

=== "Details"

    - *Description*:  Historical SEC filings for a given symbol(s)
    - *Module*:  `secFilings`
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    df = aapl.sec_filings
    df.head()
    ```

=== "Data"

    |             | date       | epochDate           | type   | title                                                                                       | edgarUrl                                                                                                    |   maxAge |
    |:------------|:-----------|:--------------------|:-------|:--------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|---------:|
    | ('aapl', 0) | 2020-05-11 | 2020-05-11 14:32:39 | 8-K    | Disclosing Other Events, Financial Statements and Exhibits                                  | https://yahoo.brand.edgar-online.com/DisplayFiling.aspx?TabIndex=2&dcn=0001193125-20-139112&nav=1&src=Yahoo |        1 |
    | ('aapl', 1) | 2020-05-01 | 2020-05-01 04:45:45 | 10-Q   | Quarterly Report                                                                            | https://yahoo.brand.edgar-online.com/DisplayFiling.aspx?TabIndex=2&dcn=0000320193-20-000052&nav=1&src=Yahoo |        1 |
    | ('aapl', 2) | 2020-04-30 | 2020-04-30 14:33:15 | 8-K    | Disclosing Results of Operations and Financial Condition, Financial Statements and Exhibits | https://yahoo.brand.edgar-online.com/DisplayFiling.aspx?TabIndex=2&dcn=0000320193-20-000050&nav=1&src=Yahoo |        1 |
    | ('aapl', 3) | 2020-02-18 | 2020-02-18 04:35:28 | 8-K    | Disclosing Regulation FD Disclosure, Financial Statements and Exhibits                      | https://yahoo.brand.edgar-online.com/DisplayFiling.aspx?TabIndex=2&dcn=0001193125-20-039203&nav=1&src=Yahoo |        1 |
    | ('aapl', 4) | 2020-01-29 | 2020-01-29 04:07:08 | 10-Q   | Quarterly Report                                                                            | https://yahoo.brand.edgar-online.com/DisplayFiling.aspx?TabIndex=2&dcn=0000320193-20-000010&nav=1&src=Yahoo |        1 |

### **share_purchase_activity**

=== "Details"

    - *Description*:  High-level buy / sell data for given symbol(s) insiders
    - *Module*:  `netSharePurchaseActivity`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.share_purchase_activity
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "maxAge": 1,
            "period": "6m",
            "buyInfoCount": 11,
            "buyInfoShares": 212070,
            "buyPercentInsiderShares": 0.077,
            "sellInfoCount": 5,
            "sellInfoShares": 97181,
            "sellPercentInsiderShares": 0.035,
            "netInfoCount": 16,
            "netInfoShares": 114889,
            "netPercentInsiderShares": 0.042,
            "totalInsiderShares": 2860661
        }
    }
    ```

### **summary_detail**

=== "Details"

    - *Description*:  Contains information available via the Summary tab in Yahoo Finance for given symbol(s)
    - *Module*:  `summaryDetail`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.summary_detail
    ```

=== "Data"

    ```python
    {
    "aapl": {
        "maxAge": 1,
        "priceHint": 2,
        "previousClose": 380.16,
        "open": 376.75,
        "dayLow": 375.07,
        "dayHigh": 385.19,
        "regularMarketPreviousClose": 380.16,
        "regularMarketOpen": 376.75,
        "regularMarketDayLow": 375.07,
        "regularMarketDayHigh": 385.19,
        "dividendRate": 3.28,
        "dividendYield": 0.0086,
        "exDividendDate": "2020-05-08 00:00:00",
        "payoutRatio": 0.2408,
        "fiveYearAvgDividendYield": 1.57,
        "beta": 1.182072,
        "trailingPE": 30.229418,
        "forwardPE": 25.70207,
        "volume": 30622619,
        "regularMarketVolume": 30622619,
        "averageVolume": 34597506,
        "averageVolume10days": 30632812,
        "averageDailyVolume10Day": 30632812,
        "bid": 384.92,
        "ask": 384.99,
        "bidSize": 800,
        "askSize": 1100,
        "marketCap": 1667676766208,
        "fiftyTwoWeekLow": 192.58,
        "fiftyTwoWeekHigh": 399.82,
        "priceToSalesTrailing12Months": 6.223116,
        "fiftyDayAverage": 368.7483,
        "twoHundredDayAverage": 313.38132,
        "trailingAnnualDividendRate": 3.08,
        "trailingAnnualDividendYield": 0.008101852,
        "currency": "USD",
        "fromCurrency": null,
        "toCurrency": null,
        "lastMarket": null,
        "algorithm": null,
        "tradeable": false
    }
    }
    ```

### **summary_profile**

=== "Details"

    - *Description*:  Data related to given symbol(s) location and business summary
    - *Module*:  `summaryProfile`
    - *Return*:  `dict`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.summary_profile
    ```

=== "Data"

    ```python
    {
        "aapl": {
            "address1": "One Apple Park Way",
            "city": "Cupertino",
            "state": "CA",
            "zip": "95014",
            "country": "United States",
            "phone": "408-996-1010",
            "website": "http://www.apple.com",
            "industry": "Consumer Electronics",
            "sector": "Technology",
            "longBusinessSummary": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, iPod touch, and other Apple-branded and third-party accessories. It also provides digital content stores and streaming services; AppleCare support services; and iCloud, a cloud service, which stores music, photos, contacts, calendars, mail, documents, and others. In addition, the company offers various service, such as Apple Arcade, a game subscription service; Apple Card, a co-branded credit card; Apple News+, a subscription news and magazine service; and Apple Pay, a cashless payment service, as well as licenses its intellectual property, and provides other related services. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It sells and delivers third-party applications for its products through the App Store, Mac App Store, and Watch App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. has a collaboration with Google to develop COVID-19 tracking system for Android and iOS devices. Apple Inc. was founded in 1977 and is headquartered in Cupertino, California.",
            "fullTimeEmployees": 137000,
            "companyOfficers": [],
            "maxAge": 86400
        }
    }
    ```

## Multiple Modules

### **all_modules**

=== "Details"

    - *Description*:  Returns all **modules** from above
    - *Return*:  `dict`

    !!! info
        Each module will be a key in the dictionary returned

    !!! success "Number of Requests"
        The call to `all_modules` represents only **1** request per symbol

    !!! warning
        Data for symbols external to the United States will be inaccurate for the following modules:  `cashFlowStatementHistory`, `cashFlowStatementHistoryQuarterly`, `incomeStatementHistory`, `incomeStatementHistoryQuarterly`, `balanceSheetHistory`, `balanceSheetHistoryQuarterly`.

        !!! tip
            See [Financials](financials.md) for a better way to retrieve accurate data

=== "Example"

    ```python hl_lines="2"
    >>> aapl = Ticker('aapl')
    >>> data = aapl.all_modules
    >>> data.keys()
    dict_keys(['aapl'])
    >>> data['aapl'].keys()
    dict_keys([
        'assetProfile', 'recommendationTrend', 'cashflowStatementHistory', 'indexTrend',
        'defaultKeyStatistics', 'industryTrend', 'quoteType', 'incomeStatementHistory',
        'fundOwnership', 'summaryDetail', 'insiderHolders', 'calendarEvents',
        'upgradeDowngradeHistory', 'price', 'balanceSheetHistory', 'earningsTrend',
        'secFilings', 'institutionOwnership', 'majorHoldersBreakdown', 'balanceSheetHistoryQuarterly',
        'earningsHistory', 'esgScores', 'summaryProfile', 'netSharePurchaseActivity',
        'insiderTransactions', 'sectorTrend', 'incomeStatementHistoryQuarterly',
        'cashflowStatementHistoryQuarterly', 'earnings', 'pageViews', 'financialData'
    ])
    ```

### **get_modules**

=== "Details"

    - *Description*:  Obtain specific modules for given symbol(s)
    - *Arguments*: `list` or `str` of desired modules
    - *Return*:  `dict`
    - *Raises*: `ValueError` is raised if invalid module is given

    ???+ example "View Available Modules"

        ```python
        [
            'assetProfile', 'recommendationTrend', 'cashflowStatementHistory',
            'indexTrend', 'defaultKeyStatistics', 'industryTrend', 'quoteType',
            'incomeStatementHistory', 'fundOwnership', 'summaryDetail', 'insiderHolders',
            'calendarEvents', 'upgradeDowngradeHistory', 'price', 'balanceSheetHistory',
            'earningsTrend', 'secFilings', 'institutionOwnership', 'majorHoldersBreakdown',
            'balanceSheetHistoryQuarterly', 'earningsHistory', 'esgScores', 'summaryProfile',
            'netSharePurchaseActivity', 'insiderTransactions', 'sectorTrend',
            'incomeStatementHistoryQuarterly', 'cashflowStatementHistoryQuarterly', 'earnings',
            'pageViews', 'financialData'
        ]
        ```

=== "Example"

    ```python hl_lines="2 3"
    aapl = Ticker('aapl')
    modules = 'assetProfile earnings defaultKeyStatistics'
    aapl.get_modules(modules)
    ```

=== "Data"

    ```python hl_lines="2 3 80 118"
    {
        "aapl": {
            "assetProfile": {
                "address1": "One Apple Park Way",
                "city": "Cupertino",
                "state": "CA",
                "zip": "95014",
                "country": "United States",
                "phone": "408-996-1010",
                "website": "http://www.apple.com",
                "industry": "Consumer Electronics",
                "sector": "Technology",
                "longBusinessSummary": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, iPod touch, and other Apple-branded and third-party accessories. It also provides digital content stores and streaming services; AppleCare support services; and iCloud, a cloud service, which stores music, photos, contacts, calendars, mail, documents, and others. In addition, the company offers various service, such as Apple Arcade, a game subscription service; Apple Card, a co-branded credit card; Apple News+, a subscription news and magazine service; and Apple Pay, a cashless payment service, as well as licenses its intellectual property, and provides other related services. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It sells and delivers third-party applications for its products through the App Store, Mac App Store, and Watch App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. has a collaboration with Google to develop COVID-19 tracking system for Android and iOS devices. Apple Inc. was founded in 1977 and is headquartered in Cupertino, California.",
                "fullTimeEmployees": 137000,
                "companyOfficers": [{
                        "maxAge": 1,
                        "name": "Mr. Timothy D. Cook",
                        "age": 58,
                        "title": "CEO & Director",
                        "yearBorn": 1961,
                        "fiscalYear": 2019,
                        "totalPay": 11555466,
                        "exercisedValue": 0,
                        "unexercisedValue": 0
                    },
                    {
                        "maxAge": 1,
                        "name": "Mr. Luca  Maestri",
                        "age": 55,
                        "title": "CFO & Sr. VP",
                        "yearBorn": 1964,
                        "fiscalYear": 2019,
                        "totalPay": 3576221,
                        "exercisedValue": 0,
                        "unexercisedValue": 0
                    },
                    {
                        "maxAge": 1,
                        "name": "Mr. Jeffrey E. Williams",
                        "age": 55,
                        "title": "Chief Operating Officer",
                        "yearBorn": 1964,
                        "fiscalYear": 2019,
                        "totalPay": 3574503,
                        "exercisedValue": 0,
                        "unexercisedValue": 0
                    },
                    {
                        "maxAge": 1,
                        "name": "Ms. Katherine L. Adams",
                        "age": 55,
                        "title": "Sr. VP, Gen. Counsel & Sec.",
                        "yearBorn": 1964,
                        "fiscalYear": 2019,
                        "totalPay": 3598384,
                        "exercisedValue": 0,
                        "unexercisedValue": 0
                    },
                    {
                        "maxAge": 1,
                        "name": "Ms. Deirdre  O'Brien",
                        "age": 52,
                        "title": "Sr. VP of People & Retail",
                        "yearBorn": 1967,
                        "fiscalYear": 2019,
                        "totalPay": 2690253,
                        "exercisedValue": 0,
                        "unexercisedValue": 0
                    }
                ],
                "auditRisk": 1,
                "boardRisk": 1,
                "compensationRisk": 3,
                "shareHolderRightsRisk": 1,
                "overallRisk": 1,
                "governanceEpochDate": "2019-12-07 00:00:00",
                "compensationAsOfEpochDate": "2019-12-31 00:00:00",
                "maxAge": 86400
            },
            "defaultKeyStatistics": {
                "maxAge": 1,
                "priceHint": 2,
                "enterpriseValue": 1672450801664,
                "forwardPE": 25.70207,
                "profitMargins": 0.21350001,
                "floatShares": 4329740605,
                "sharesOutstanding": 4334329856,
                "sharesShort": 35234606,
                "sharesShortPriorMonth": 34828293,
                "sharesShortPreviousMonthDate": "2020-06-15 00:00:00",
                "dateShortInterest": "2020-07-15 00:00:00",
                "sharesPercentSharesOut": 0.0081,
                "heldPercentInsiders": 0.00066,
                "heldPercentInstitutions": 0.62115,
                "shortRatio": 0.96,
                "shortPercentOfFloat": 0.0081,
                "beta": 1.182072,
                "category": null,
                "bookValue": 18.137,
                "priceToBook": 21.214094,
                "fundFamily": null,
                "legalType": null,
                "lastFiscalYearEnd": "2019-09-28 00:00:00",
                "nextFiscalYearEnd": "2021-09-28 00:00:00",
                "mostRecentQuarter": "2020-03-28 00:00:00",
                "earningsQuarterlyGrowth": -0.027,
                "netIncomeToCommon": 57215000576,
                "trailingEps": 12.728,
                "forwardEps": 14.97,
                "pegRatio": 2.78,
                "lastSplitFactor": "7:1",
                "lastSplitDate": "2014-06-09 00:00:00",
                "enterpriseToRevenue": 6.241,
                "enterpriseToEbitda": 21.634,
                "52WeekChange": 0.8239218,
                "SandP52WeekChange": 0.103224516
            },
            "earnings": {
                "maxAge": 86400,
                "earningsChart": {
                    "quarterly": [{
                            "date": "2Q2019",
                            "actual": 2.18,
                            "estimate": 2.1
                        },
                        {
                            "date": "3Q2019",
                            "actual": 3.03,
                            "estimate": 2.84
                        },
                        {
                            "date": "4Q2019",
                            "actual": 4.99,
                            "estimate": 4.55
                        },
                        {
                            "date": "1Q2020",
                            "actual": 2.55,
                            "estimate": 2.26
                        }
                    ],
                    "currentQuarterEstimate": 2.04,
                    "currentQuarterEstimateDate": "2Q",
                    "currentQuarterEstimateYear": 2020,
                    "earningsDate": [
                        1596067200
                    ]
                },
                "financialsChart": {
                    "yearly": [{
                            "date": 2016,
                            "revenue": 215639000000,
                            "earnings": 45687000000
                        },
                        {
                            "date": 2017,
                            "revenue": 229234000000,
                            "earnings": 48351000000
                        },
                        {
                            "date": 2018,
                            "revenue": 265595000000,
                            "earnings": 59531000000
                        },
                        {
                            "date": 2019,
                            "revenue": 260174000000,
                            "earnings": 55256000000
                        }
                    ],
                    "quarterly": [{
                            "date": "2Q2019",
                            "revenue": 53809000000,
                            "earnings": 10044000000
                        },
                        {
                            "date": "3Q2019",
                            "revenue": 64040000000,
                            "earnings": 13686000000
                        },
                        {
                            "date": "4Q2019",
                            "revenue": 91819000000,
                            "earnings": 22236000000
                        },
                        {
                            "date": "1Q2020",
                            "revenue": 58313000000,
                            "earnings": 11249000000
                        }
                    ]
                },
                "financialCurrency": "USD"
            }
        }
    }
    ```
