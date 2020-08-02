## Individual

### **balance_sheet**

=== "Details"

    - *Description*:  Retrieves balance sheet data for most recent four quarters or most recent four years as well as trailing 12 months.
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.balance_sheet()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   AccountsPayable |   AccountsReceivable |   AccumulatedDepreciation |   AllowanceForDoubtfulAccountsReceivable |   AvailableForSaleSecurities |   CapitalStock |   CashAndCashEquivalents |   CashCashEquivalentsAndShortTermInvestments |   CashEquivalents |   CashFinancial |   CommercialPaper |   CommonStock |   CommonStockEquity |   CurrentAccruedExpenses |   CurrentAssets |   CurrentDebt |   CurrentDebtAndCapitalLeaseObligation |   CurrentDeferredLiabilities |   CurrentDeferredRevenue |   CurrentLiabilities |   GainsLossesNotAffectingRetainedEarnings |    Goodwill |   GoodwillAndOtherIntangibleAssets |   GrossAccountsReceivable |   GrossPPE |   Inventory |   InvestedCapital |   InvestmentinFinancialAssets |   InvestmentsAndAdvances |   LandAndImprovements |    Leases |   LongTermDebt |   LongTermDebtAndCapitalLeaseObligation |   MachineryFurnitureEquipment |    NetDebt |     NetPPE |   NetTangibleAssets |   NonCurrentDeferredLiabilities |   NonCurrentDeferredRevenue |   NonCurrentDeferredTaxesLiabilities |   OrdinarySharesNumber |   OtherCurrentAssets |   OtherCurrentBorrowings |   OtherCurrentLiabilities |   OtherIntangibleAssets |   OtherNonCurrentAssets |   OtherNonCurrentLiabilities |   OtherReceivables |   OtherShortTermInvestments |   Payables |   PayablesAndAccruedExpenses |   Properties |   Receivables |   RetainedEarnings |   ShareIssued |   StockholdersEquity |   TangibleBookValue |   TotalAssets |   TotalCapitalization |   TotalDebt |   TotalEquityGrossMinorityInterest |   TotalLiabilitiesNetMinorityInterest |   TotalNonCurrentAssets |   TotalNonCurrentLiabilitiesNetMinorityInterest |   TradeandOtherPayablesNonCurrent |   WorkingCapital |
    |:---------|:--------------------|:-------------|------------------:|---------------------:|--------------------------:|-----------------------------------------:|-----------------------------:|---------------:|-------------------------:|---------------------------------------------:|------------------:|----------------:|------------------:|--------------:|--------------------:|-------------------------:|----------------:|--------------:|---------------------------------------:|-----------------------------:|-------------------------:|---------------------:|------------------------------------------:|------------:|-----------------------------------:|--------------------------:|-----------:|------------:|------------------:|------------------------------:|-------------------------:|----------------------:|----------:|---------------:|----------------------------------------:|------------------------------:|-----------:|-----------:|--------------------:|--------------------------------:|----------------------------:|-------------------------------------:|-----------------------:|---------------------:|-------------------------:|--------------------------:|------------------------:|------------------------:|-----------------------------:|-------------------:|----------------------------:|-----------:|-----------------------------:|-------------:|--------------:|-------------------:|--------------:|---------------------:|--------------------:|--------------:|----------------------:|------------:|-----------------------------------:|--------------------------------------:|------------------------:|------------------------------------------------:|----------------------------------:|-----------------:|
    | aapl     | 2016-09-30 00:00:00 | 12M          |        3.7294e+10 |           1.5754e+10 |               -3.4235e+10 |                                 -5.3e+07 |                  1.7043e+11  |     3.1251e+10 |               2.0484e+10 |                                  6.7155e+10  |        1.1883e+10 |      8.601e+09  |        8.105e+09  |    3.1251e+10 |         1.28249e+11 |               2.2027e+10 |     1.06869e+11 |    1.1605e+10 |                             1.1605e+10 |                    8.08e+09  |                8.08e+09  |          7.9006e+10  |                                 6.34e+08  |   5.414e+09 |                          8.62e+09  |                1.5807e+10 | 6.1245e+10 |   2.132e+09 |       2.15281e+11 |                   1.7043e+11  |              1.7043e+11  |            1.0185e+10 | 6.517e+09 |     7.5427e+10 |                              7.5427e+10 |                    4.4543e+10 | 6.6548e+10 | 2.701e+10  |         1.19629e+11 |                      2.8949e+10 |                   2.93e+09  |                           2.6019e+10 |            5.33617e+09 |           8.283e+09  |                3.5e+09   |              nan          |               3.206e+09 |              8.757e+09  |                   1.0055e+10 |         1.3545e+10 |                  4.6671e+10 | 3.7294e+10 |                   5.9321e+10 |            0 |    2.9299e+10 |         9.6364e+10 |   5.33617e+09 |          1.28249e+11 |         1.19629e+11 |   3.21686e+11 |           2.03676e+11 | 8.7032e+10  |                        1.28249e+11 |                           1.93437e+11 |             2.14817e+11 |                                     1.14431e+11 |                      nan          |       2.7863e+10 |
    | aapl     | 2017-09-30 00:00:00 | 12M          |        4.9049e+10 |           1.7874e+10 |               -4.1293e+10 |                                 -5.8e+07 |                  1.94714e+11 |     3.5867e+10 |               2.0289e+10 |                                  7.4181e+10  |        1.2307e+10 |      7.982e+09  |        1.1977e+10 |    3.5867e+10 |         1.34047e+11 |               2.5744e+10 |     1.28645e+11 |    1.8473e+10 |                             1.8473e+10 |                    7.548e+09 |                7.548e+09 |          1.00814e+11 |                                -1.5e+08   |   5.717e+09 |                          8.015e+09 |                1.7932e+10 | 7.5076e+10 |   4.855e+09 |       2.49727e+11 |                   1.94714e+11 |              1.94714e+11 |            1.3587e+10 | 7.279e+09 |     9.7207e+10 |                              9.7207e+10 |                    5.421e+10  | 9.5391e+10 | 3.3783e+10 |         1.26032e+11 |                      3.434e+10  |                   2.836e+09 |                           3.1504e+10 |            5.1262e+09  |           1.3936e+10 |                6.496e+09 |              nan          |               2.298e+09 |              1.0162e+10 |                   8.911e+09  |         1.7799e+10 |                  5.3892e+10 | 4.9049e+10 |                   7.4793e+10 |            0 |    3.5673e+10 |         9.833e+10  |   5.1262e+09  |          1.34047e+11 |         1.26032e+11 |   3.75319e+11 |           2.31254e+11 | 1.1568e+11  |                        1.34047e+11 |                           2.41272e+11 |             2.46674e+11 |                                     1.40458e+11 |                      nan          |       2.7831e+10 |
    | aapl     | 2018-09-30 00:00:00 | 12M          |        5.5888e+10 |           2.3186e+10 |               -4.9099e+10 |                                nan       |                  1.70799e+11 |     4.0201e+10 |               2.5913e+10 |                                  6.6301e+10  |        1.4338e+10 |      1.1575e+10 |        1.1964e+10 |    4.0201e+10 |         1.07147e+11 |             nan          |     1.31339e+11 |    2.0748e+10 |                             2.0748e+10 |                    7.543e+09 |                7.543e+09 |          1.16866e+11 |                                -3.454e+09 | nan         |                        nan         |              nan          | 9.0403e+10 |   3.956e+09 |       2.2163e+11  |                   1.70799e+11 |              1.70799e+11 |            1.6216e+10 | 8.205e+09 |     9.3735e+10 |                              9.3735e+10 |                    6.5982e+10 | 8.857e+10  | 4.1304e+10 |         1.07147e+11 |                      3.223e+09  |                   2.797e+09 |                           4.26e+08   |            4.75499e+09 |           1.2087e+10 |                8.784e+09 |                3.2687e+10 |             nan         |              2.2283e+10 |                   1.1165e+10 |         2.5809e+10 |                  4.0388e+10 | 5.5888e+10 |                   5.5888e+10 |            0 |    4.8995e+10 |         7.04e+10   |   4.75499e+09 |          1.07147e+11 |         1.07147e+11 |   3.65725e+11 |           2.00882e+11 | 1.14483e+11 |                        1.07147e+11 |                           2.58578e+11 |             2.34386e+11 |                                     1.41712e+11 |                        3.3589e+10 |       1.4473e+10 |
    | aapl     | 2019-09-30 00:00:00 | 12M          |        4.6236e+10 |           2.2926e+10 |               -5.8579e+10 |                                nan       |                  1.05341e+11 |     4.5174e+10 |               4.8844e+10 |                                  1.00557e+11 |        3.664e+10  |      1.2204e+10 |        5.98e+09   |    4.5174e+10 |         9.0488e+10  |             nan          |     1.62819e+11 |    1.624e+10  |                             1.624e+10  |                    5.522e+09 |                5.522e+09 |          1.05718e+11 |                                -5.84e+08  | nan         |                        nan         |              nan          | 9.5957e+10 |   4.106e+09 |       1.98535e+11 |                   1.05341e+11 |              1.05341e+11 |            1.7085e+10 | 9.075e+09 |     9.1807e+10 |                              9.1807e+10 |                    6.9797e+10 | 5.9203e+10 | 3.7378e+10 |         9.0488e+10  |                    nan          |                 nan         |                         nan          |            4.44324e+09 |           1.2352e+10 |                1.026e+10 |                3.772e+10  |             nan         |              3.2978e+10 |                   2.0958e+10 |         2.2878e+10 |                  5.1713e+10 | 4.6236e+10 |                   4.6236e+10 |            0 |    4.5804e+10 |         4.5898e+10 |   4.44324e+09 |          9.0488e+10  |         9.0488e+10  |   3.38516e+11 |           1.82295e+11 | 1.08047e+11 |                        9.0488e+10  |                           2.48028e+11 |             1.75697e+11 |                                     1.4231e+11  |                        2.9545e+10 |       5.7101e+10 |

### **cash_flow**

=== "Details"

    - *Description*:  Retrieves cash flow data for most recent four quarters or most recent four years as well as the trailing 12 months
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.cash_flow(trailing=False)
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   BeginningCashPosition |   CapitalExpenditure |   CashDividendsPaid |   CashFlowFromContinuingFinancingActivities |   ChangeInAccountPayable |   ChangeInCashSupplementalAsReported |   ChangeInInventory |   ChangeInWorkingCapital |   ChangesInAccountReceivables |   CommonStockIssuance |   DeferredIncomeTax |   DepreciationAndAmortization |   EndCashPosition |   FreeCashFlow |   InvestingCashFlow |   NetIncome |   NetOtherFinancingCharges |   NetOtherInvestingChanges |   OperatingCashFlow |   OtherNonCashItems |   PurchaseOfBusiness |   PurchaseOfInvestment |   RepaymentOfDebt |   RepurchaseOfCapitalStock |   SaleOfInvestment |   StockBasedCompensation |
    |:---------|:--------------------|:-------------|------------------------:|---------------------:|--------------------:|--------------------------------------------:|-------------------------:|-------------------------------------:|--------------------:|-------------------------:|------------------------------:|----------------------:|--------------------:|------------------------------:|------------------:|---------------:|--------------------:|------------:|---------------------------:|---------------------------:|--------------------:|--------------------:|---------------------:|-----------------------:|------------------:|---------------------------:|-------------------:|-------------------------:|
    | aapl     | 2016-09-30 00:00:00 | 12M          |              2.112e+10  |          -1.3548e+10 |         -1.215e+10  |                                 -2.0483e+10 |                1.791e+09 |                          -6.36e+08   |           2.17e+08  |               4.84e+08   |                     1.095e+09 |              4.95e+08 |           4.938e+09 |                    1.0505e+10 |        2.0484e+10 |     5.2276e+10 |         -4.5977e+10 |  4.5687e+10 |                 -1.163e+09 |                 -1.1e+08   |          6.5824e+10 |          nan        |            -2.97e+08 |           -1.43816e+11 |        -2.5e+09   |                -2.9722e+10 |        1.11794e+11 |                4.21e+09  |
    | aapl     | 2017-09-30 00:00:00 | 12M          |              2.0484e+10 |          -1.2795e+10 |         -1.2769e+10 |                                 -1.7347e+10 |                9.618e+09 |                          -1.95e+08   |          -2.723e+09 |              -5.55e+09   |                    -2.093e+09 |              5.55e+08 |           5.966e+09 |                    1.0157e+10 |        2.0289e+10 |     5.0803e+10 |         -4.6446e+10 |  4.8351e+10 |                 -1.247e+09 |                  2.2e+08   |          6.3598e+10 |           -1.66e+08 |            -3.29e+08 |           -1.59881e+11 |        -3.5e+09   |                -3.29e+10   |        1.26339e+11 |                4.84e+09  |
    | aapl     | 2018-09-30 00:00:00 | 12M          |              2.0289e+10 |          -1.3313e+10 |         -1.3712e+10 |                                 -8.7876e+10 |                9.175e+09 |                           5.624e+09  |           8.28e+08  |               3.4694e+10 |                    -5.322e+09 |              6.69e+08 |          -3.259e+10 |                    1.0903e+10 |        2.5913e+10 |     6.4121e+10 |          1.6066e+10 |  5.9531e+10 |                 -2.527e+09 |                 -7.45e+08  |          7.7434e+10 |           -4.44e+08 |            -7.21e+08 |           -7.3227e+10  |        -6.5e+09   |                -7.2738e+10 |        1.04072e+11 |                5.34e+09  |
    | aapl     | 2019-09-30 00:00:00 | 12M          |              2.5913e+10 |          -1.0495e+10 |         -1.4119e+10 |                                 -9.0976e+10 |               -1.923e+09 |                           2.4311e+10 |          -2.89e+08  |              -3.488e+09  |                     2.45e+08  |              7.81e+08 |          -3.4e+08   |                    1.2547e+10 |        5.0224e+10 |     5.8896e+10 |          4.5896e+10 |  5.5256e+10 |                 -2.922e+09 |                 -1.078e+09 |          6.9391e+10 |           -6.52e+08 |            -6.24e+08 |           -4.0631e+10  |        -8.805e+09 |                -6.6897e+10 |        9.8724e+10  |                6.068e+09 |

### **income_statement**

=== "Details"

    - *Description*:  Retrieves income statement data for most recent four quarters or most recent four years as well as trailing 12 months.
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.income_statement()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   BasicAverageShares |   BasicEPS |   CostOfRevenue |   DilutedAverageShares |   DilutedEPS |   DilutedNIAvailtoComStockholders |       EBIT |       EBITDA |   GrossProfit |   InterestExpense |   InterestExpenseNonOperating |   InterestIncome |   InterestIncomeNonOperating |   NetIncome |   NetIncomeCommonStockholders |   NetIncomeContinuousOperations |   NetIncomeFromContinuingAndDiscontinuedOperation |   NetIncomeFromContinuingOperationNetMinorityInterest |   NetIncomeIncludingNoncontrollingInterests |   NetInterestIncome |   NetNonOperatingInterestIncomeExpense |   NormalizedEBITDA |   NormalizedIncome |   OperatingExpense |   OperatingIncome |   OperatingRevenue |   OtherIncomeExpense |   OtherNonOperatingIncomeExpenses |   PretaxIncome |   ReconciledCostOfRevenue |   ReconciledDepreciation |   ResearchAndDevelopment |   SellingGeneralAndAdministration |   TaxEffectOfUnusualItems |   TaxProvision |   TaxRateForCalcs |   TotalExpenses |   TotalOperatingIncomeAsReported |   TotalRevenue |
    |:---------|:--------------------|:-------------|---------------------:|-----------:|----------------:|-----------------------:|-------------:|----------------------------------:|-----------:|-------------:|--------------:|------------------:|------------------------------:|-----------------:|-----------------------------:|------------:|------------------------------:|--------------------------------:|--------------------------------------------------:|------------------------------------------------------:|--------------------------------------------:|--------------------:|---------------------------------------:|-------------------:|-------------------:|-------------------:|------------------:|-------------------:|---------------------:|----------------------------------:|---------------:|--------------------------:|-------------------------:|-------------------------:|----------------------------------:|--------------------------:|---------------:|------------------:|----------------:|---------------------------------:|---------------:|
    | aapl     | 2016-09-30 00:00:00 | 12M          |          5.47082e+09 |       8.35 |     1.31376e+11 |            5.50028e+09 |         8.31 |                        4.5687e+10 | 6.2828e+10 | nan          |   8.4263e+10  |         1.456e+09 |                     1.456e+09 |        3.999e+09 |                    3.999e+09 |  4.5687e+10 |                    4.5687e+10 |                      4.5687e+10 |                                        4.5687e+10 |                                            4.5687e+10 |                                  4.5687e+10 |           2.543e+09 |                              2.543e+09 |         7.3333e+10 |         4.5687e+10 |         2.4239e+10 |        6.0024e+10 |        2.15639e+11 |           -1.195e+09 |                        -1.195e+09 |     6.1372e+10 |               1.31376e+11 |               1.0505e+10 |               1.0045e+10 |                        1.4194e+10 |                         0 |     1.5685e+10 |          0.256    |     1.55615e+11 |                       6.0024e+10 |    2.15639e+11 |
    | aapl     | 2017-09-30 00:00:00 | 12M          |          5.21724e+09 |       9.27 |     1.41048e+11 |            5.25169e+09 |         9.21 |                        4.8351e+10 | 6.6412e+10 | nan          |   8.8186e+10  |         2.323e+09 |                     2.323e+09 |        5.201e+09 |                    5.201e+09 |  4.8351e+10 |                    4.8351e+10 |                      4.8351e+10 |                                        4.8351e+10 |                                            4.8351e+10 |                                  4.8351e+10 |           2.878e+09 |                              2.878e+09 |         7.6569e+10 |         4.8351e+10 |         2.6842e+10 |        6.1344e+10 |        2.29234e+11 |           -1.33e+08  |                        -1.33e+08  |     6.4089e+10 |               1.41048e+11 |               1.0157e+10 |               1.1581e+10 |                        1.5261e+10 |                         0 |     1.5738e+10 |          0.246    |     1.6789e+11  |                       6.1344e+10 |    2.29234e+11 |
    | aapl     | 2018-09-30 00:00:00 | 12M          |          4.95538e+09 |      12.01 |     1.63756e+11 |            5.00011e+09 |        11.91 |                        5.9531e+10 | 7.6143e+10 | nan          |   1.01839e+11 |         3.24e+09  |                     3.24e+09  |        5.686e+09 |                    5.686e+09 |  5.9531e+10 |                    5.9531e+10 |                      5.9531e+10 |                                        5.9531e+10 |                                            5.9531e+10 |                                  5.9531e+10 |           2.446e+09 |                              2.446e+09 |         8.7046e+10 |         5.9531e+10 |         3.0941e+10 |        7.0898e+10 |        2.65595e+11 |           -4.41e+08  |                        -4.41e+08  |     7.2903e+10 |               1.63756e+11 |               1.0903e+10 |               1.4236e+10 |                        1.6705e+10 |                         0 |     1.3372e+10 |          0.183    |     1.94697e+11 |                       7.0898e+10 |    2.65595e+11 |
    | aapl     | 2019-09-30 00:00:00 | 12M          |          4.61783e+09 |      11.97 |     1.61782e+11 |            4.64891e+09 |        11.89 |                        5.5256e+10 | 6.9313e+10 | nan          |   9.8392e+10  |         3.576e+09 |                     3.576e+09 |        4.961e+09 |                    4.961e+09 |  5.5256e+10 |                    5.5256e+10 |                      5.5256e+10 |                                        5.5256e+10 |                                            5.5256e+10 |                                  5.5256e+10 |           1.385e+09 |                              1.385e+09 |         8.186e+10  |         5.5256e+10 |         3.4462e+10 |        6.393e+10  |        2.60174e+11 |            4.22e+08  |                         4.22e+08  |     6.5737e+10 |               1.61782e+11 |               1.2547e+10 |               1.6217e+10 |                        1.8245e+10 |                         0 |     1.0481e+10 |          0.159    |     1.96244e+11 |                       6.393e+10  |    2.60174e+11 |
    | aapl     | 2020-03-31 00:00:00 | TTM          |        nan           |     nan    |     1.65854e+11 |          nan           |       nan    |                        5.7215e+10 | 7.0309e+10 |   8.2023e+10 |   1.02127e+11 |         3.218e+09 |                     3.218e+09 |        4.39e+09  |                    4.39e+09  |  5.7215e+10 |                    5.7215e+10 |                      5.7215e+10 |                                        5.7215e+10 |                                            5.7215e+10 |                                  5.7215e+10 |           1.172e+09 |                              1.172e+09 |         8.2023e+10 |         5.7215e+10 |         3.6536e+10 |        6.5591e+10 |        2.67981e+11 |            3.28e+08  |                         3.28e+08  |     6.7091e+10 |               1.65854e+11 |               1.1714e+10 |               1.7383e+10 |                        1.9153e+10 |                         0 |     9.876e+09  |          0.147203 |     2.0239e+11  |                       6.5591e+10 |    2.67981e+11 |

### **valuation_measures**

=== "Details"

    - *Description*:  Retrieves valuation measures for most recent four quarters as well as the most recent date
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    aapl.valuation_measures
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   EnterpriseValue |   EnterprisesValueEBITDARatio |   EnterprisesValueRevenueRatio |   ForwardPeRatio |     MarketCap |   PbRatio |   PeRatio |   PegRatio |   PsRatio |
    |:---------|:--------------------|:-------------|------------------:|------------------------------:|-------------------------------:|-----------------:|--------------:|----------:|----------:|-----------:|----------:|
    | aapl     | 2019-06-30 00:00:00 | 3M           |       9.43183e+11 |                       60.0371 |                       17.5283  |          15.9744 |   9.10645e+11 |   8.47207 |   16.5762 |     1.4501 |   3.68445 |
    | aapl     | 2019-09-30 00:00:00 | 3M           |       1.00896e+12 |                       50.1569 |                       15.7551  |          17.2712 |   9.95152e+11 |  10.3172  |   19.0127 |     2.0355 |   4.09034 |
    | aapl     | 2019-12-31 00:00:00 | 3M           |       1.29513e+12 |                       43.8746 |                       14.1053  |          22.1729 |   1.28764e+12 |  14.23    |   24.6972 |     2.0292 |   5.24708 |
    | aapl     | 2020-03-05 00:00:00 | TTM          |       1.2828e+12  |                      nan      |                      nan       |          22.1239 |   1.28167e+12 |  14.3153  |   23.0646 |     1.7784 |   5.00004 |
    | aapl     | 2020-03-08 00:00:00 | TTM          |     nan           |                       15.4204 |                        4.79222 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-03-31 00:00:00 | 3M           |       1.10068e+12 |                       65.9957 |                       18.8753  |          19.6464 |   1.09955e+12 |  12.2812  |   20.0228 |     1.5803 |   4.34064 |
    | aapl     | 2020-05-08 00:00:00 | TTM          |       1.35966e+12 |                      nan      |                      nan       |          26.178  |   1.34421e+12 |  17.14    |   24.2478 |     2.171  |   5.20229 |
    | aapl     | 2020-05-11 00:00:00 | TTM          |     nan           |                       16.5766 |                        5.07373 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-05-28 00:00:00 | TTM          |       1.39486e+12 |                      nan      |                      nan       |          26.8097 |   1.3794e+12  |  17.5888  |   24.8827 |     2.2278 |   5.3385  |
    | aapl     | 2020-05-29 00:00:00 | TTM          |     nan           |                       17.0057 |                        5.20506 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-06-12 00:00:00 | TTM          |       1.48393e+12 |                      nan      |                      nan       |          22.5734 |   1.46847e+12 |  18.7245  |   26.4894 |     1.8786 |   5.68322 |
    | aapl     | 2020-06-15 00:00:00 | TTM          |     nan           |                       18.0916 |                        5.53744 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-07-14 00:00:00 | TTM          |       1.69817e+12 |                      nan      |                      nan       |          25.8398 |   1.68272e+12 |  21.4564  |   30.3542 |     2.1527 |   6.51239 |
    | aapl     | 2020-07-15 00:00:00 | TTM          |     nan           |                       20.7036 |                        6.33692 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-07-16 00:00:00 | TTM          |       1.6889e+12  |                      nan      |                      nan       |          26.3158 |   1.67344e+12 |  21.3381  |   30.1869 |     2.1897 |   6.47649 |
    | aapl     | 2020-07-18 00:00:00 | TTM          |     nan           |                       20.5906 |                        6.30231 |         nan      | nan           | nan       |  nan      |   nan      | nan       |
    | aapl     | 2020-07-29 00:00:00 | TTM          |       1.6632e+12  |                      nan      |                      nan       |          25.1256 |   1.64774e+12 |  21.0104  |   29.7232 |     2.0905 |   6.37702 |
    | aapl     | 2020-07-30 00:00:00 | TTM          |     nan           |                       20.2772 |                        6.2064  |         nan      | nan           | nan       |  nan      |   nan      | nan       |


## Multiple


### all_financial_data

=== "Details"

    - *Description*:  Retrieve all financial data, including income statement, balance sheet, cash flow, and valuation measures.
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |

    !!! warning
        No trailing twelve month (TTM) data will be returned with this method

=== "Example"

    ```python
    aapl = Ticker('aapl')
    aapl.all_financial_data()
    ```

=== "Data"

| symbol   | asOfDate            | periodType   |   AccountsPayable |   AccountsReceivable |   AccumulatedDepreciation |   AllowanceForDoubtfulAccountsReceivable |   AvailableForSaleSecurities |   BasicAverageShares |   BasicEPS |   BeginningCashPosition |   CapitalExpenditure |   CapitalStock |   CashAndCashEquivalents |   CashCashEquivalentsAndShortTermInvestments |   CashDividendsPaid |   CashEquivalents |   CashFinancial |   CashFlowFromContinuingFinancingActivities |   ChangeInAccountPayable |   ChangeInCashSupplementalAsReported |   ChangeInInventory |   ChangeInWorkingCapital |   ChangesInAccountReceivables |   CommercialPaper |   CommonStock |   CommonStockEquity |   CommonStockIssuance |   CostOfRevenue |   CurrentAccruedExpenses |   CurrentAssets |   CurrentDebt |   CurrentDebtAndCapitalLeaseObligation |   CurrentDeferredLiabilities |   CurrentDeferredRevenue |   CurrentLiabilities |   DeferredIncomeTax |   DepreciationAndAmortization |   DilutedAverageShares |   DilutedEPS |   DilutedNIAvailtoComStockholders |       EBIT |   EndCashPosition |   EnterpriseValue |   EnterprisesValueEBITDARatio |   EnterprisesValueRevenueRatio |   ForwardPeRatio |   FreeCashFlow |   GainsLossesNotAffectingRetainedEarnings |    Goodwill |   GoodwillAndOtherIntangibleAssets |   GrossAccountsReceivable |   GrossPPE |   GrossProfit |   InterestExpense |   InterestExpenseNonOperating |   InterestIncome |   InterestIncomeNonOperating |   Inventory |   InvestedCapital |   InvestingCashFlow |   InvestmentinFinancialAssets |   InvestmentsAndAdvances |   LandAndImprovements |    Leases |   LongTermDebt |   LongTermDebtAndCapitalLeaseObligation |   MachineryFurnitureEquipment |   MarketCap |    NetDebt |   NetIncome |   NetIncomeCommonStockholders |   NetIncomeContinuousOperations |   NetIncomeFromContinuingAndDiscontinuedOperation |   NetIncomeFromContinuingOperationNetMinorityInterest |   NetIncomeIncludingNoncontrollingInterests |   NetInterestIncome |   NetNonOperatingInterestIncomeExpense |   NetOtherFinancingCharges |   NetOtherInvestingChanges |     NetPPE |   NetTangibleAssets |   NonCurrentDeferredLiabilities |   NonCurrentDeferredRevenue |   NonCurrentDeferredTaxesLiabilities |   NormalizedEBITDA |   NormalizedIncome |   OperatingCashFlow |   OperatingExpense |   OperatingIncome |   OperatingRevenue |   OrdinarySharesNumber |   OtherCurrentAssets |   OtherCurrentBorrowings |   OtherCurrentLiabilities |   OtherIncomeExpense |   OtherIntangibleAssets |   OtherNonCashItems |   OtherNonCurrentAssets |   OtherNonCurrentLiabilities |   OtherNonOperatingIncomeExpenses |   OtherReceivables |   OtherShortTermInvestments |   Payables |   PayablesAndAccruedExpenses |   PbRatio |   PeRatio |   PegRatio |   PretaxIncome |   Properties |   PsRatio |   PurchaseOfBusiness |   PurchaseOfInvestment |   Receivables |   ReconciledCostOfRevenue |   ReconciledDepreciation |   RepaymentOfDebt |   RepurchaseOfCapitalStock |   ResearchAndDevelopment |   RetainedEarnings |   SaleOfInvestment |   SellingGeneralAndAdministration |   ShareIssued |   StockBasedCompensation |   StockholdersEquity |   TangibleBookValue |   TaxEffectOfUnusualItems |   TaxProvision |   TaxRateForCalcs |   TotalAssets |   TotalCapitalization |   TotalDebt |   TotalEquityGrossMinorityInterest |   TotalExpenses |   TotalLiabilitiesNetMinorityInterest |   TotalNonCurrentAssets |   TotalNonCurrentLiabilitiesNetMinorityInterest |   TotalOperatingIncomeAsReported |   TotalRevenue |   TradeandOtherPayablesNonCurrent |   WorkingCapital |
|:---------|:--------------------|:-------------|------------------:|---------------------:|--------------------------:|-----------------------------------------:|-----------------------------:|---------------------:|-----------:|------------------------:|---------------------:|---------------:|-------------------------:|---------------------------------------------:|--------------------:|------------------:|----------------:|--------------------------------------------:|-------------------------:|-------------------------------------:|--------------------:|-------------------------:|------------------------------:|------------------:|--------------:|--------------------:|----------------------:|----------------:|-------------------------:|----------------:|--------------:|---------------------------------------:|-----------------------------:|-------------------------:|---------------------:|--------------------:|------------------------------:|-----------------------:|-------------:|----------------------------------:|-----------:|------------------:|------------------:|------------------------------:|-------------------------------:|-----------------:|---------------:|------------------------------------------:|------------:|-----------------------------------:|--------------------------:|-----------:|--------------:|------------------:|------------------------------:|-----------------:|-----------------------------:|------------:|------------------:|--------------------:|------------------------------:|-------------------------:|----------------------:|----------:|---------------:|----------------------------------------:|------------------------------:|------------:|-----------:|------------:|------------------------------:|--------------------------------:|--------------------------------------------------:|------------------------------------------------------:|--------------------------------------------:|--------------------:|---------------------------------------:|---------------------------:|---------------------------:|-----------:|--------------------:|--------------------------------:|----------------------------:|-------------------------------------:|-------------------:|-------------------:|--------------------:|-------------------:|------------------:|-------------------:|-----------------------:|---------------------:|-------------------------:|--------------------------:|---------------------:|------------------------:|--------------------:|------------------------:|-----------------------------:|----------------------------------:|-------------------:|----------------------------:|-----------:|-----------------------------:|----------:|----------:|-----------:|---------------:|-------------:|----------:|---------------------:|-----------------------:|--------------:|--------------------------:|-------------------------:|------------------:|---------------------------:|-------------------------:|-------------------:|-------------------:|----------------------------------:|--------------:|-------------------------:|---------------------:|--------------------:|--------------------------:|---------------:|------------------:|--------------:|----------------------:|------------:|-----------------------------------:|----------------:|--------------------------------------:|------------------------:|------------------------------------------------:|---------------------------------:|---------------:|----------------------------------:|-----------------:|
| aapl     | 2016-09-30 00:00:00 | 12M          |        3.7294e+10 |           1.5754e+10 |               -3.4235e+10 |                                 -5.3e+07 |                  1.7043e+11  |          5.47082e+09 |       8.35 |              2.112e+10  |          -1.3548e+10 |     3.1251e+10 |               2.0484e+10 |                                  6.7155e+10  |         -1.215e+10  |        1.1883e+10 |      8.601e+09  |                                 -2.0483e+10 |                1.791e+09 |                          -6.36e+08   |           2.17e+08  |               4.84e+08   |                     1.095e+09 |        8.105e+09  |    3.1251e+10 |         1.28249e+11 |              4.95e+08 |     1.31376e+11 |               2.2027e+10 |     1.06869e+11 |    1.1605e+10 |                             1.1605e+10 |                    8.08e+09  |                8.08e+09  |          7.9006e+10  |           4.938e+09 |                    1.0505e+10 |            5.50028e+09 |         8.31 |                        4.5687e+10 | 6.2828e+10 |        2.0484e+10 |       6.26433e+11 |                        8.5423 |                        2.90501 |          12.6582 |     5.2276e+10 |                                 6.34e+08  |   5.414e+09 |                          8.62e+09  |                1.5807e+10 | 6.1245e+10 |   8.4263e+10  |         1.456e+09 |                     1.456e+09 |        3.999e+09 |                    3.999e+09 |   2.132e+09 |       2.15281e+11 |         -4.5977e+10 |                   1.7043e+11  |              1.7043e+11  |            1.0185e+10 | 6.517e+09 |     7.5427e+10 |                              7.5427e+10 |                    4.4543e+10 | 6.03254e+11 | 6.6548e+10 |  4.5687e+10 |                    4.5687e+10 |                      4.5687e+10 |                                        4.5687e+10 |                                            4.5687e+10 |                                  4.5687e+10 |           2.543e+09 |                              2.543e+09 |                 -1.163e+09 |                 -1.1e+08   | 2.701e+10  |         1.19629e+11 |                      2.8949e+10 |                   2.93e+09  |                           2.6019e+10 |         7.3333e+10 |         4.5687e+10 |          6.5824e+10 |         2.4239e+10 |        6.0024e+10 |        2.15639e+11 |            5.33617e+09 |           8.283e+09  |                3.5e+09   |              nan          |           -1.195e+09 |               3.206e+09 |          nan        |              8.757e+09  |                   1.0055e+10 |                        -1.195e+09 |         1.3545e+10 |                  4.6671e+10 | 3.7294e+10 |                   5.9321e+10 |   4.76726 |   13.1607 |     2.4275 |     6.1372e+10 |            0 |   2.8598  |            -2.97e+08 |           -1.43816e+11 |    2.9299e+10 |               1.31376e+11 |               1.0505e+10 |        -2.5e+09   |                -2.9722e+10 |               1.0045e+10 |         9.6364e+10 |        1.11794e+11 |                        1.4194e+10 |   5.33617e+09 |                4.21e+09  |          1.28249e+11 |         1.19629e+11 |                         0 |     1.5685e+10 |             0.256 |   3.21686e+11 |           2.03676e+11 | 8.7032e+10  |                        1.28249e+11 |     1.55615e+11 |                           1.93437e+11 |             2.14817e+11 |                                     1.14431e+11 |                       6.0024e+10 |    2.15639e+11 |                      nan          |       2.7863e+10 |
| aapl     | 2017-09-30 00:00:00 | 12M          |        4.9049e+10 |           1.7874e+10 |               -4.1293e+10 |                                 -5.8e+07 |                  1.94714e+11 |          5.21724e+09 |       9.27 |              2.0484e+10 |          -1.2795e+10 |     3.5867e+10 |               2.0289e+10 |                                  7.4181e+10  |         -1.2769e+10 |        1.2307e+10 |      7.982e+09  |                                 -1.7347e+10 |                9.618e+09 |                          -1.95e+08   |          -2.723e+09 |              -5.55e+09   |                    -2.093e+09 |        1.1977e+10 |    3.5867e+10 |         1.34047e+11 |              5.55e+08 |     1.41048e+11 |               2.5744e+10 |     1.28645e+11 |    1.8473e+10 |                             1.8473e+10 |                    7.548e+09 |                7.548e+09 |          1.00814e+11 |           5.966e+09 |                    1.0157e+10 |            5.25169e+09 |         9.21 |                        4.8351e+10 | 6.6412e+10 |        2.0289e+10 |       8.27645e+11 |                       10.8091 |                        3.61048 |          14.245  |     5.0803e+10 |                                -1.5e+08   |   5.717e+09 |                          8.015e+09 |                1.7932e+10 | 7.5076e+10 |   8.8186e+10  |         2.323e+09 |                     2.323e+09 |        5.201e+09 |                    5.201e+09 |   4.855e+09 |       2.49727e+11 |         -4.6446e+10 |                   1.94714e+11 |              1.94714e+11 |            1.3587e+10 | 7.279e+09 |     9.7207e+10 |                              9.7207e+10 |                    5.421e+10  | 7.96065e+11 | 9.5391e+10 |  4.8351e+10 |                    4.8351e+10 |                      4.8351e+10 |                                        4.8351e+10 |                                            4.8351e+10 |                                  4.8351e+10 |           2.878e+09 |                              2.878e+09 |                 -1.247e+09 |                  2.2e+08   | 3.3783e+10 |         1.26032e+11 |                      3.434e+10  |                   2.836e+09 |                           3.1504e+10 |         7.6569e+10 |         4.8351e+10 |          6.3598e+10 |         2.6842e+10 |        6.1344e+10 |        2.29234e+11 |            5.1262e+09  |           1.3936e+10 |                6.496e+09 |              nan          |           -1.33e+08  |               2.298e+09 |           -1.66e+08 |              1.0162e+10 |                   8.911e+09  |                        -1.33e+08  |         1.7799e+10 |                  5.3892e+10 | 4.9049e+10 |                   7.4793e+10 |   5.96602 |   17.4541 |     2.087  |     6.4089e+10 |            0 |   3.65748 |            -3.29e+08 |           -1.59881e+11 |    3.5673e+10 |               1.41048e+11 |               1.0157e+10 |        -3.5e+09   |                -3.29e+10   |               1.1581e+10 |         9.833e+10  |        1.26339e+11 |                        1.5261e+10 |   5.1262e+09  |                4.84e+09  |          1.34047e+11 |         1.26032e+11 |                         0 |     1.5738e+10 |             0.246 |   3.75319e+11 |           2.31254e+11 | 1.1568e+11  |                        1.34047e+11 |     1.6789e+11  |                           2.41272e+11 |             2.46674e+11 |                                     1.40458e+11 |                       6.1344e+10 |    2.29234e+11 |                      nan          |       2.7831e+10 |
| aapl     | 2018-09-30 00:00:00 | 12M          |        5.5888e+10 |           2.3186e+10 |               -4.9099e+10 |                                nan       |                  1.70799e+11 |          4.95538e+09 |      12.01 |              2.0289e+10 |          -1.3313e+10 |     4.0201e+10 |               2.5913e+10 |                                  6.6301e+10  |         -1.3712e+10 |        1.4338e+10 |      1.1575e+10 |                                 -8.7876e+10 |                9.175e+09 |                           5.624e+09  |           8.28e+08  |               3.4694e+10 |                    -5.322e+09 |        1.1964e+10 |    4.0201e+10 |         1.07147e+11 |              6.69e+08 |     1.63756e+11 |             nan          |     1.31339e+11 |    2.0748e+10 |                             2.0748e+10 |                    7.543e+09 |                7.543e+09 |          1.16866e+11 |          -3.259e+10 |                    1.0903e+10 |            5.00011e+09 |        11.91 |                        5.9531e+10 | 7.6143e+10 |        2.5913e+10 |       1.13394e+12 |                       13.0269 |                        4.26942 |          16.6945 |     6.4121e+10 |                                -3.454e+09 | nan         |                        nan         |              nan          | 9.0403e+10 |   1.01839e+11 |         3.24e+09  |                     3.24e+09  |        5.686e+09 |                    5.686e+09 |   3.956e+09 |       2.2163e+11  |          1.6066e+10 |                   1.70799e+11 |              1.70799e+11 |            1.6216e+10 | 8.205e+09 |     9.3735e+10 |                              9.3735e+10 |                    6.5982e+10 | 1.09031e+12 | 8.857e+10  |  5.9531e+10 |                    5.9531e+10 |                      5.9531e+10 |                                        5.9531e+10 |                                            5.9531e+10 |                                  5.9531e+10 |           2.446e+09 |                              2.446e+09 |                 -2.527e+09 |                 -7.45e+08  | 4.1304e+10 |         1.07147e+11 |                      3.223e+09  |                   2.797e+09 |                           4.26e+08   |         8.7046e+10 |         5.9531e+10 |          7.7434e+10 |         3.0941e+10 |        7.0898e+10 |        2.65595e+11 |            4.75499e+09 |           1.2087e+10 |                8.784e+09 |                3.2687e+10 |           -4.41e+08  |             nan         |           -4.44e+08 |              2.2283e+10 |                   1.1165e+10 |                        -4.41e+08  |         2.5809e+10 |                  4.0388e+10 | 5.5888e+10 |                   5.5888e+10 |   9.33797 |   20.4105 |     1.2848 |     7.2903e+10 |            0 |   4.49591 |            -7.21e+08 |           -7.3227e+10  |    4.8995e+10 |               1.63756e+11 |               1.0903e+10 |        -6.5e+09   |                -7.2738e+10 |               1.4236e+10 |         7.04e+10   |        1.04072e+11 |                        1.6705e+10 |   4.75499e+09 |                5.34e+09  |          1.07147e+11 |         1.07147e+11 |                         0 |     1.3372e+10 |             0.183 |   3.65725e+11 |           2.00882e+11 | 1.14483e+11 |                        1.07147e+11 |     1.94697e+11 |                           2.58578e+11 |             2.34386e+11 |                                     1.41712e+11 |                       7.0898e+10 |    2.65595e+11 |                        3.3589e+10 |       1.4473e+10 |
| aapl     | 2019-09-30 00:00:00 | 12M          |        4.6236e+10 |           2.2926e+10 |               -5.8579e+10 |                                nan       |                  1.05341e+11 |          4.61783e+09 |      11.97 |              2.5913e+10 |          -1.0495e+10 |     4.5174e+10 |               4.8844e+10 |                                  1.00557e+11 |         -1.4119e+10 |        3.664e+10  |      1.2204e+10 |                                 -9.0976e+10 |               -1.923e+09 |                           2.4311e+10 |          -2.89e+08  |              -3.488e+09  |                     2.45e+08  |        5.98e+09   |    4.5174e+10 |         9.0488e+10  |              7.81e+08 |     1.61782e+11 |             nan          |     1.62819e+11 |    1.624e+10  |                             1.624e+10  |                    5.522e+09 |                5.522e+09 |          1.05718e+11 |          -3.4e+08   |                    1.2547e+10 |            4.64891e+09 |        11.89 |                        5.5256e+10 | 6.9313e+10 |        5.0224e+10 |       1.00896e+12 |                       12.3254 |                        3.878   |          17.2712 |     5.8896e+10 |                                -5.84e+08  | nan         |                        nan         |              nan          | 9.5957e+10 |   9.8392e+10  |         3.576e+09 |                     3.576e+09 |        4.961e+09 |                    4.961e+09 |   4.106e+09 |       1.98535e+11 |          4.5896e+10 |                   1.05341e+11 |              1.05341e+11 |            1.7085e+10 | 9.075e+09 |     9.1807e+10 |                              9.1807e+10 |                    6.9797e+10 | 9.95152e+11 | 5.9203e+10 |  5.5256e+10 |                    5.5256e+10 |                      5.5256e+10 |                                        5.5256e+10 |                                            5.5256e+10 |                                  5.5256e+10 |           1.385e+09 |                              1.385e+09 |                 -2.922e+09 |                 -1.078e+09 | 3.7378e+10 |         9.0488e+10  |                    nan          |                 nan         |                         nan          |         8.186e+10  |         5.5256e+10 |          6.9391e+10 |         3.4462e+10 |        6.393e+10  |        2.60174e+11 |            4.44324e+09 |           1.2352e+10 |                1.026e+10 |                3.772e+10  |            4.22e+08  |             nan         |           -6.52e+08 |              3.2978e+10 |                   2.0958e+10 |                         4.22e+08  |         2.2878e+10 |                  5.1713e+10 | 4.6236e+10 |                   4.6236e+10 |  10.3172  |   19.0127 |     2.0355 |     6.5737e+10 |            0 |   4.09034 |            -6.24e+08 |           -4.0631e+10  |    4.5804e+10 |               1.61782e+11 |               1.2547e+10 |        -8.805e+09 |                -6.6897e+10 |               1.6217e+10 |         4.5898e+10 |        9.8724e+10  |                        1.8245e+10 |   4.44324e+09 |                6.068e+09 |          9.0488e+10  |         9.0488e+10  |                         0 |     1.0481e+10 |             0.159 |   3.38516e+11 |           1.82295e+11 | 1.08047e+11 |                        9.0488e+10  |     1.96244e+11 |                           2.48028e+11 |             1.75697e+11 |                                     1.4231e+11  |                       6.393e+10  |    2.60174e+11 |                        2.9545e+10 |       5.7101e+10 |

### get_financial_data

=== "Details"

    - *Description*:  Obtain specific data from either cash flow, income statement, balance sheet, or valuation measures.
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | types      | `list` or `str` | `None`    | **Required**   | See options below             |
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

    !!! warning
        If you try and use all of the options below **AND** `trailing=True`, you will
        receive an error because the requested URL will be too long

    === "Balance Sheet"

        ```python
        [
            'AccountsPayable', 'AccountsReceivable', 'AccruedInterestReceivable',
            'AccumulatedDepreciation', 'AdditionalPaidInCapital',
            'AllowanceForDoubtfulAccountsReceivable', 'AssetsHeldForSaleCurrent',
            'AvailableForSaleSecurities', 'BuildingsAndImprovements', 'CapitalLeaseObligations',
            'CapitalStock', 'CashAndCashEquivalents', 'CashCashEquivalentsAndShortTermInvestments',
            'CashEquivalents', 'CashFinancial', 'CommercialPaper', 'CommonStock',
            'CommonStockEquity', 'ConstructionInProgress', 'CurrentAccruedExpenses',
            'CurrentAssets', 'CurrentCapitalLeaseObligation', 'CurrentDebt',
            'CurrentDebtAndCapitalLeaseObligation', 'CurrentDeferredAssets',
            'CurrentDeferredLiabilities', 'CurrentDeferredRevenue', 'CurrentDeferredTaxesAssets',
            'CurrentDeferredTaxesLiabilities', 'CurrentLiabilities', 'CurrentNotesPayable',
            'CurrentProvisions', 'DefinedPensionBenefit', 'DerivativeProductLiabilities',
            'DividendsPayable', 'DuefromRelatedPartiesCurrent', 'DuefromRelatedPartiesNonCurrent',
            'DuetoRelatedPartiesCurrent', 'DuetoRelatedPartiesNonCurrent', 'EmployeeBenefits',
            'FinancialAssets', 'FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal',
            'FinishedGoods', 'FixedAssetsRevaluationReserve', 'ForeignCurrencyTranslationAdjustments',
            'GainsLossesNotAffectingRetainedEarnings', 'GeneralPartnershipCapital', 'Goodwill',
            'GoodwillAndOtherIntangibleAssets', 'GrossAccountsReceivable', 'GrossPPE',
            'HedgingAssetsCurrent', 'HeldToMaturitySecurities', 'IncomeTaxPayable',
            'InterestPayable', 'InventoriesAdjustmentsAllowances', 'Inventory',
            'InvestedCapital', 'InvestmentProperties', 'InvestmentinFinancialAssets',
            'InvestmentsAndAdvances', 'InvestmentsInOtherVenturesUnderEquityMethod',
            'InvestmentsinAssociatesatCost', 'InvestmentsinJointVenturesatCost',
            'InvestmentsinSubsidiariesatCost', 'LandAndImprovements', 'Leases',
            'LiabilitiesHeldforSaleNonCurrent', 'LimitedPartnershipCapital',
            'LineOfCredit', 'LoansReceivable', 'LongTermCapitalLeaseObligation',
            'LongTermDebt', 'LongTermDebtAndCapitalLeaseObligation', 'LongTermEquityInvestment',
            'LongTermProvisions', 'MachineryFurnitureEquipment', 'MinimumPensionLiabilities',
            'MinorityInterest', 'NetDebt', 'NetPPE', 'NetTangibleAssets', 'NonCurrentAccountsReceivable',
            'NonCurrentAccruedExpenses', 'NonCurrentDeferredAssets', 'NonCurrentDeferredLiabilities',
            'NonCurrentDeferredRevenue', 'NonCurrentDeferredTaxesAssets', 'NonCurrentDeferredTaxesLiabilities',
            'NonCurrentNoteReceivables', 'NonCurrentPensionAndOtherPostretirementBenefitPlans',
            'NonCurrentPrepaidAssets', 'NotesReceivable', 'OrdinarySharesNumber',
            'OtherCapitalStock', 'OtherCurrentAssets', 'OtherCurrentBorrowings',
            'OtherCurrentLiabilities', 'OtherEquityAdjustments', 'OtherEquityInterest',
            'OtherIntangibleAssets', 'OtherInventories', 'OtherInvestments', 'OtherNonCurrentAssets',
            'OtherNonCurrentLiabilities', 'OtherPayable', 'OtherProperties', 'OtherReceivables',
            'OtherShortTermInvestments', 'Payables', 'PayablesAndAccruedExpenses',
            'PensionandOtherPostRetirementBenefitPlansCurrent', 'PreferredSecuritiesOutsideStockEquity',
            'PreferredSharesNumber', 'PreferredStock', 'PreferredStockEquity',
            'PrepaidAssets', 'Properties', 'RawMaterials', 'Receivables',
            'ReceivablesAdjustmentsAllowances', 'RestrictedCash', 'RestrictedCommonStock',
            'RetainedEarnings', 'ShareIssued', 'StockholdersEquity', 'TangibleBookValue',
            'TaxesReceivable', 'TotalAssets', 'TotalCapitalization', 'TotalDebt',
            'TotalEquityGrossMinorityInterest', 'TotalLiabilitiesNetMinorityInterest',
            'TotalNonCurrentAssets', 'TotalNonCurrentLiabilitiesNetMinorityInterest',
            'TotalPartnershipCapital', 'TotalTaxPayable', 'TradeandOtherPayablesNonCurrent',
            'TradingSecurities', 'TreasurySharesNumber', 'TreasuryStock', 'UnrealizedGainLoss',
            'WorkInProcess', 'WorkingCapital'
        ]
        ```

    === "Cash Flow"

        ```python
        [
            'RepaymentOfDebt', 'RepurchaseOfCapitalStock', 'CashDividendsPaid',
            'CommonStockIssuance', 'ChangeInWorkingCapital',
            'CapitalExpenditure',
            'CashFlowFromContinuingFinancingActivities', 'NetIncome',
            'FreeCashFlow', 'ChangeInCashSupplementalAsReported',
            'SaleOfInvestment', 'EndCashPosition', 'OperatingCashFlow',
            'DeferredIncomeTax', 'NetOtherInvestingChanges',
            'ChangeInAccountPayable', 'NetOtherFinancingCharges',
            'PurchaseOfInvestment', 'ChangeInInventory',
            'DepreciationAndAmortization', 'PurchaseOfBusiness',
            'InvestingCashFlow', 'ChangesInAccountReceivables',
            'StockBasedCompensation', 'OtherNonCashItems',
            'BeginningCashPosition'
        ]
        ```

    === "Income Statement"

        ```python
        [
            'Amortization', 'AmortizationOfIntangiblesIncomeStatement',
            'AverageDilutionEarnings', 'BasicAccountingChange', 'BasicAverageShares',
            'BasicContinuousOperations', 'BasicDiscontinuousOperations', 'BasicEPS',
            'BasicEPSOtherGainsLosses', 'BasicExtraordinary', 'ContinuingAndDiscontinuedBasicEPS',
            'ContinuingAndDiscontinuedDilutedEPS', 'CostOfRevenue', 'DepletionIncomeStatement',
            'DepreciationAmortizationDepletionIncomeStatement', 'DepreciationAndAmortizationInIncomeStatement',
            'DepreciationIncomeStatement', 'DilutedAccountingChange', 'DilutedAverageShares',
            'DilutedContinuousOperations', 'DilutedDiscontinuousOperations', 'DilutedEPS',
            'DilutedEPSOtherGainsLosses', 'DilutedExtraordinary', 'DilutedNIAvailtoComStockholders',
            'DividendPerShare', 'EBIT', 'EBITDA', 'EarningsFromEquityInterest',
            'EarningsFromEquityInterestNetOfTax', 'ExciseTaxes', 'GainOnSaleOfBusiness',
            'GainOnSaleOfPPE', 'GainOnSaleOfSecurity', 'GeneralAndAdministrativeExpense',
            'GrossProfit', 'ImpairmentOfCapitalAssets', 'InsuranceAndClaims',
            'InterestExpense', 'InterestExpenseNonOperating', 'InterestIncome',
            'InterestIncomeNonOperating', 'MinorityInterests', 'NetIncome', 'NetIncomeCommonStockholders',
            'NetIncomeContinuousOperations', 'NetIncomeDiscontinuousOperations',
            'NetIncomeExtraordinary', 'NetIncomeFromContinuingAndDiscontinuedOperation',
            'NetIncomeFromContinuingOperationNetMinorityInterest', 'NetIncomeFromTaxLossCarryforward',
            'NetIncomeIncludingNoncontrollingInterests', 'NetInterestIncome',
            'NetNonOperatingInterestIncomeExpense', 'NormalizedBasicEPS', 'NormalizedDilutedEPS',
            'NormalizedEBITDA', 'NormalizedIncome', 'OperatingExpense', 'OperatingIncome',
            'OperatingRevenue', 'OtherGandA', 'OtherIncomeExpense', 'OtherNonOperatingIncomeExpenses',
            'OtherOperatingExpenses', 'OtherSpecialCharges', 'OtherTaxes',
            'OtherunderPreferredStockDividend', 'PreferredStockDividends',
            'PretaxIncome', 'ProvisionForDoubtfulAccounts', 'ReconciledCostOfRevenue',
            'ReconciledDepreciation', 'RentAndLandingFees', 'RentExpenseSupplemental',
            'ReportedNormalizedBasicEPS', 'ReportedNormalizedDilutedEPS', 'ResearchAndDevelopment',
            'RestructuringAndMergernAcquisition', 'SalariesAndWages', 'SecuritiesAmortization',
            'SellingAndMarketingExpense', 'SellingGeneralAndAdministration', 'SpecialIncomeCharges',
            'TaxEffectOfUnusualItems', 'TaxLossCarryforwardBasicEPS', 'TaxLossCarryforwardDilutedEPS',
            'TaxProvision', 'TaxRateForCalcs', 'TotalExpenses', 'TotalOperatingIncomeAsReported',
            'TotalOtherFinanceCost', 'TotalRevenue', 'TotalUnusualItems',
            'TotalUnusualItemsExcludingGoodwill', 'WriteOff'
        ]
        ```

    === "Valuation Measures"

        ```python
        [
            'ForwardPeRatio', 'PsRatio', 'PbRatio',
            'EnterprisesValueEBITDARatio', 'EnterprisesValueRevenueRatio',
            'PeRatio', 'MarketCap', 'EnterpriseValue', 'PegRatio'
        ]
        ```    
    
=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl')
    types = ['TotalDebt', 'TotalAssets', 'EBIT', 'EBITDA', 'PeRatio']
    aapl.get_financial_data(types, trailing=False)
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |       EBIT |   PeRatio |   TotalAssets |   TotalDebt |
    |:---------|:--------------------|:-------------|-----------:|----------:|--------------:|------------:|
    | aapl     | 2016-09-30 00:00:00 | 12M          | 6.2828e+10 |   13.1607 |   3.21686e+11 | 8.7032e+10  |
    | aapl     | 2017-09-30 00:00:00 | 12M          | 6.6412e+10 |   17.4541 |   3.75319e+11 | 1.1568e+11  |
    | aapl     | 2018-09-30 00:00:00 | 12M          | 7.6143e+10 |   20.4105 |   3.65725e+11 | 1.14483e+11 |
    | aapl     | 2019-09-30 00:00:00 | 12M          | 6.9313e+10 |   19.0127 |   3.38516e+11 | 1.08047e+11 |
