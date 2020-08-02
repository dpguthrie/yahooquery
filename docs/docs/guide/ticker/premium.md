
## Financials

### Individual

#### **p_balance_sheet**

=== "Details"

    - *Description*:  Retrieves balance sheet data for given symbol(s)
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    df = aapl.p_balance_sheet()
    df.head()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   AccountsPayable |   AccountsReceivable |   AccumulatedDepreciation |   AdditionalPaidInCapital |   AllowanceForDoubtfulAccountsReceivable |   AvailableForSaleSecurities |   BuildingsAndImprovements |   CapitalStock |   CashAndCashEquivalents |   CashCashEquivalentsAndShortTermInvestments |   CashEquivalents |   CashFinancial |   CommercialPaper |   CommonStock |   CommonStockEquity |   CurrentAccruedExpenses |   CurrentAssets |   CurrentDebt |   CurrentDebtAndCapitalLeaseObligation |   CurrentDeferredAssets |   CurrentDeferredLiabilities |   CurrentDeferredRevenue |   CurrentDeferredTaxesAssets |   CurrentLiabilities |   CurrentNotesPayable |   FinishedGoods |   ForeignCurrencyTranslationAdjustments |   GainsLossesNotAffectingRetainedEarnings |   Goodwill |   GoodwillAndOtherIntangibleAssets |   GrossAccountsReceivable |   GrossPPE |   IncomeTaxPayable |   Inventory |   InvestedCapital |   InvestmentinFinancialAssets |   InvestmentsAndAdvances |   LandAndImprovements |   Leases |   LongTermDebt |   LongTermDebtAndCapitalLeaseObligation |   MachineryFurnitureEquipment |   NetDebt |    NetPPE |   NetTangibleAssets |   NonCurrentDeferredAssets |   NonCurrentDeferredLiabilities |   NonCurrentDeferredRevenue |   NonCurrentDeferredTaxesAssets |   NonCurrentDeferredTaxesLiabilities |   NonCurrentPrepaidAssets |   OrdinarySharesNumber |   OtherCurrentAssets |   OtherCurrentBorrowings |   OtherCurrentLiabilities |   OtherEquityAdjustments |   OtherEquityInterest |   OtherIntangibleAssets |   OtherNonCurrentAssets |   OtherNonCurrentLiabilities |   OtherPayable |   OtherProperties |   OtherReceivables |   OtherShortTermInvestments |    Payables |   PayablesAndAccruedExpenses |   PensionandOtherPostRetirementBenefitPlansCurrent |   PreferredStock |   PreferredStockEquity |   PrepaidAssets |   Properties |   RawMaterials |   Receivables |   RetainedEarnings |   ShareIssued |   StockholdersEquity |   TangibleBookValue |   TotalAssets |   TotalCapitalization |   TotalDebt |   TotalEquityGrossMinorityInterest |   TotalLiabilitiesNetMinorityInterest |   TotalNonCurrentAssets |   TotalNonCurrentLiabilitiesNetMinorityInterest |   TotalTaxPayable |   TradeandOtherPayablesNonCurrent |   WorkInProcess |   WorkingCapital |
    |:---------|:--------------------|:-------------|------------------:|---------------------:|--------------------------:|--------------------------:|-----------------------------------------:|-----------------------------:|---------------------------:|---------------:|-------------------------:|---------------------------------------------:|------------------:|----------------:|------------------:|--------------:|--------------------:|-------------------------:|----------------:|--------------:|---------------------------------------:|------------------------:|-----------------------------:|-------------------------:|-----------------------------:|---------------------:|----------------------:|----------------:|----------------------------------------:|------------------------------------------:|-----------:|-----------------------------------:|--------------------------:|-----------:|-------------------:|------------:|------------------:|------------------------------:|-------------------------:|----------------------:|---------:|---------------:|----------------------------------------:|------------------------------:|----------:|----------:|--------------------:|---------------------------:|--------------------------------:|----------------------------:|--------------------------------:|-------------------------------------:|--------------------------:|-----------------------:|---------------------:|-------------------------:|--------------------------:|-------------------------:|----------------------:|------------------------:|------------------------:|-----------------------------:|---------------:|------------------:|-------------------:|----------------------------:|------------:|-----------------------------:|---------------------------------------------------:|-----------------:|-----------------------:|----------------:|-------------:|---------------:|--------------:|-------------------:|--------------:|---------------------:|--------------------:|--------------:|----------------------:|------------:|-----------------------------------:|--------------------------------------:|------------------------:|------------------------------------------------:|------------------:|----------------------------------:|----------------:|-----------------:|
    | aapl     | 1985-09-30 00:00:00 | 12M          |       nan         |                  nan |                -8.52e+07  |                       nan |                                      nan |                          nan |                        nan |            nan |                3.37e+08  |                                    3.37e+08  |               nan |             nan |               nan |           nan |          5.505e+08  |                      nan |      8.221e+08  |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            2.954e+08 |                   nan |             nan |                                     nan |                                       nan |        nan |                                nan |                       nan |  1.756e+08 |                nan |   1.67e+08  |        5.505e+08  |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan |       nan | 9.04e+07  |          5.505e+08  |                        nan |                       9.03e+07  |                         nan |                             nan |                            9.03e+07  |                       nan |            3.4636e+09  |            9.79e+07  |                      nan |               nan         |                      nan |             2.302e+08 |                     nan |               2.37e+07  |                          nan |            nan |               nan |                nan |                         nan | nan         |                  nan         |                                                nan |              nan |                    nan |             nan |          nan |            nan |     2.202e+08 |         3.203e+08  |   3.4636e+09  |           5.505e+08  |          5.505e+08  |    9.362e+08  |            5.505e+08  | nan         |                         5.505e+08  |                            3.857e+08  |               1.141e+08 |                                       9.03e+07  |               nan |                               nan |             nan |       5.267e+08  |
    | aapl     | 1986-09-30 00:00:00 | 12M          |       nan         |                  nan |                -1.147e+08 |                       nan |                                      nan |                          nan |                        nan |            nan |                5.762e+08 |                                    5.762e+08 |               nan |             nan |               nan |           nan |          6.941e+08  |                      nan |      1.0409e+09 |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            3.285e+08 |                   nan |             nan |                                     nan |                                       nan |        nan |                                nan |                       nan |  2.22e+08  |                nan |   1.087e+08 |        6.941e+08  |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan |       nan | 1.073e+08 |          6.941e+08  |                        nan |                       1.375e+08 |                         nan |                             nan |                            1.375e+08 |                       nan |            3.50717e+09 |            9.29e+07  |                      nan |               nan         |                      nan |             2.198e+08 |                     nan |               1.19e+07  |                          nan |            nan |               nan |                nan |                         nan | nan         |                  nan         |                                                nan |              nan |                    nan |             nan |          nan |            nan |     2.631e+08 |         4.743e+08  |   3.50717e+09 |           6.941e+08  |          6.941e+08  |    1.1601e+09 |            6.941e+08  | nan         |                         6.941e+08  |                            4.66e+08   |               1.192e+08 |                                       1.375e+08 |               nan |                               nan |             nan |       7.124e+08  |
    | aapl     | 1987-09-30 00:00:00 | 12M          |       nan         |                  nan |                -1.587e+08 |                       nan |                                      nan |                          nan |                        nan |            nan |                5.651e+08 |                                    5.651e+08 |               nan |             nan |               nan |           nan |          8.365e+08  |                      nan |      1.3074e+09 |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            4.787e+08 |                   nan |             nan |                                     nan |                                       nan |        nan |                                nan |                       nan |  2.891e+08 |                nan |   2.258e+08 |        8.365e+08  |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan |       nan | 1.304e+08 |          8.365e+08  |                        nan |                       1.628e+08 |                         nan |                             nan |                            1.628e+08 |                       nan |            3.53046e+09 |            1.109e+08 |                      nan |               nan         |                      nan |             2.634e+08 |                     nan |               4.01e+07  |                      -100000 |            nan |               nan |                nan |                         nan | nan         |                  nan         |                                                nan |              nan |                    nan |             nan |          nan |            nan |     4.056e+08 |         5.731e+08  |   3.53046e+09 |           8.365e+08  |          8.365e+08  |    1.4779e+09 |            8.365e+08  | nan         |                         8.365e+08  |                            6.414e+08  |               1.705e+08 |                                       1.627e+08 |               nan |                               nan |             nan |       8.287e+08  |
    | aapl     | 1988-09-30 00:00:00 | 12M          |       nan         |                  nan |                -2.13e+08  |                       nan |                                      nan |                          nan |                        nan |            nan |                5.457e+08 |                                    5.457e+08 |               nan |             nan |               nan |           nan |          1.0034e+09 |                      nan |      1.783e+09  |     1.279e+08 |                              1.279e+08 |                     nan |                          nan |                      nan |                          nan |            8.271e+08 |                   nan |             nan |                                     nan |                                       nan |        nan |                                nan |                       nan |  4.204e+08 |                nan |   4.615e+08 |        1.1313e+09 |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan |       nan | 2.074e+08 |          1.0034e+09 |                        nan |                       2.516e+08 |                         nan |                             nan |                            2.516e+08 |                       nan |            3.4375e+09  |            1.37e+08  |                      nan |                 6.992e+08 |                      nan |             2.269e+08 |                     nan |               9.17e+07  |                          nan |            nan |               nan |                nan |                         nan | nan         |                  nan         |                                                nan |              nan |                    nan |             nan |          nan |            nan |     6.388e+08 |         7.765e+08  |   3.4375e+09  |           1.0034e+09 |          1.0034e+09 |    2.0821e+09 |            1.0034e+09 |   1.279e+08 |                         1.0034e+09 |                            1.0787e+09 |               2.991e+08 |                                       2.516e+08 |               nan |                               nan |             nan |       9.559e+08  |
    | aapl     | 1989-09-30 00:00:00 | 12M          |         3.342e+08 |                  nan |                -3.091e+08 |                       nan |                                      nan |                          nan |                        nan |            nan |                4.383e+08 |                                    4.383e+08 |               nan |             nan |               nan |           nan |          1.4857e+09 |                      nan |      2.2944e+09 |     5.68e+07  |                              5.68e+07  |                     nan |                          nan |                      nan |                          nan |            8.953e+08 |                   nan |             nan |                                     nan |                                       nan |        nan |                                nan |                       nan |  6.433e+08 |                nan |   4.754e+08 |        1.5425e+09 |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan |       nan | 3.342e+08 |          1.4857e+09 |                        nan |                       3.629e+08 |                         nan |                             nan |                            3.629e+08 |                       nan |            3.53556e+09 |            5.879e+08 |                      nan |                 5.043e+08 |                      nan |             3.098e+08 |                     nan |               1.153e+08 |                          nan |            nan |               nan |                nan |                         nan |   3.342e+08 |                    3.342e+08 |                                                nan |              nan |                    nan |             nan |          nan |            nan |     7.928e+08 |         1.1759e+09 |   3.53556e+09 |           1.4857e+09 |          1.4857e+09 |    2.7439e+09 |            1.4857e+09 |   5.68e+07  |                         1.4857e+09 |                            1.2582e+09 |               4.495e+08 |                                       3.629e+08 |               nan |                               nan |             nan |       1.3991e+09 |


#### **p_cash_flow**

=== "Details"

    - *Description*:  Retrieves cash flow data for given symbol(s)
    - *Return*:  `pandas.DataFrame`
    - *Arguments*

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `a`       | optional   | Annual - `a`<br>Quarter - `q` |
    | trailing   | `bool` | `True`    | optional   | `True`<br>`False`             |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    df = aapl.p_cash_flow()
    df.head()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   BeginningCashPosition |   CapitalExpenditure |   CashDividendsPaid |   CashFlowFromContinuingFinancingActivities |   ChangeInAccountPayable |   ChangeInCashSupplementalAsReported |   ChangeInInventory |   ChangeInWorkingCapital |   ChangesInAccountReceivables |   CommonStockIssuance |   DeferredIncomeTax |   DepreciationAndAmortization |   EndCashPosition |   FreeCashFlow |   InvestingCashFlow |   NetIncome |   NetOtherFinancingCharges |   NetOtherInvestingChanges |   OperatingCashFlow |   OtherNonCashItems |   PurchaseOfBusiness |   PurchaseOfInvestment |   RepaymentOfDebt |   RepurchaseOfCapitalStock |   SaleOfInvestment |   StockBasedCompensation |
    |:---------|:--------------------|:-------------|------------------------:|---------------------:|--------------------:|--------------------------------------------:|-------------------------:|-------------------------------------:|--------------------:|-------------------------:|------------------------------:|----------------------:|--------------------:|------------------------------:|------------------:|---------------:|--------------------:|------------:|---------------------------:|---------------------------:|--------------------:|--------------------:|---------------------:|-----------------------:|------------------:|---------------------------:|-------------------:|-------------------------:|
    | aapl     | 1985-09-30 00:00:00 | 12M          |             nan         |           nan        |          nan        |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |             nan       |         nan         |                   nan         |               nan |    nan         |         nan         |   6.12e+07  |                        nan |                 nan        |         nan         |                 nan |                  nan |            nan         |               nan |                 nan        |        nan         |                      nan |
    | aapl     | 1986-09-30 00:00:00 | 12M          |             nan         |           nan        |          nan        |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |             nan       |         nan         |                   nan         |               nan |    nan         |         nan         |   1.54e+08  |                        nan |                 nan        |         nan         |                 nan |                  nan |            nan         |               nan |                 nan        |        nan         |                      nan |
    | aapl     | 1987-09-30 00:00:00 | 12M          |             nan         |           nan        |          nan        |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |             nan       |         nan         |                   nan         |               nan |    nan         |         nan         |   2.175e+08 |                        nan |                 nan        |         nan         |                 nan |                  nan |            nan         |               nan |                 nan        |        nan         |                      nan |
    | aapl     | 1988-09-30 00:00:00 | 12M          |             nan         |           nan        |          nan        |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |             nan       |         nan         |                   nan         |               nan |    nan         |         nan         |   4.003e+08 |                        nan |                 nan        |         nan         |                 nan |                  nan |            nan         |               nan |                 nan        |        nan         |                      nan |
    | aapl     | 1989-09-30 00:00:00 | 12M          |               3.724e+08 |            -2.39e+08 |           -5.03e+07 |                                   -3.83e+07 |                      nan |                             6.59e+07 |           -1.39e+07 |                -1.09e+08 |                           nan |               9.6e+07 |           1.113e+08 |                     1.248e+08 |                 0 |      2.683e+08 |          -4.031e+08 |   4.54e+08  |                        nan |                   3.32e+07 |           5.073e+08 |              100000 |                  nan |             -9.847e+08 |               nan |                  -1.29e+07 |          7.874e+08 |                      nan |

#### **p_income_statement**

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
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    df = aapl.income_statement()
    df.head()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   BasicAverageShares |   BasicEPS |   CostOfRevenue |   DepreciationAmortizationDepletionIncomeStatement |   DepreciationAndAmortizationInIncomeStatement |   DilutedAverageShares |   DilutedEPS |   DilutedNIAvailtoComStockholders |      EBIT |   EBITDA |   EarningsFromEquityInterest |   GainOnSaleOfSecurity |   GrossProfit |   InterestExpense |   InterestExpenseNonOperating |   InterestIncome |   InterestIncomeNonOperating |   NetIncome |   NetIncomeCommonStockholders |   NetIncomeContinuousOperations |   NetIncomeExtraordinary |   NetIncomeFromContinuingAndDiscontinuedOperation |   NetIncomeFromContinuingOperationNetMinorityInterest |   NetIncomeFromTaxLossCarryforward |   NetIncomeIncludingNoncontrollingInterests |   NetInterestIncome |   NetNonOperatingInterestIncomeExpense |   NormalizedEBITDA |   NormalizedIncome |   OperatingExpense |   OperatingIncome |   OperatingRevenue |   OtherIncomeExpense |   OtherNonOperatingIncomeExpenses |   OtherOperatingExpenses |   OtherSpecialCharges |   PretaxIncome |   ReconciledCostOfRevenue |   ReconciledDepreciation |   ResearchAndDevelopment |   RestructuringAndMergernAcquisition |   SellingGeneralAndAdministration |   SpecialIncomeCharges |   TaxEffectOfUnusualItems |   TaxProvision |   TaxRateForCalcs |   TotalExpenses |   TotalOperatingIncomeAsReported |   TotalOtherFinanceCost |   TotalRevenue |   TotalUnusualItems |   TotalUnusualItemsExcludingGoodwill |
    |:---------|:--------------------|:-------------|---------------------:|-----------:|----------------:|---------------------------------------------------:|-----------------------------------------------:|-----------------------:|-------------:|----------------------------------:|----------:|---------:|-----------------------------:|-----------------------:|--------------:|------------------:|------------------------------:|-----------------:|-----------------------------:|------------:|------------------------------:|--------------------------------:|-------------------------:|--------------------------------------------------:|------------------------------------------------------:|-----------------------------------:|--------------------------------------------:|--------------------:|---------------------------------------:|-------------------:|-------------------:|-------------------:|------------------:|-------------------:|---------------------:|----------------------------------:|-------------------------:|----------------------:|---------------:|--------------------------:|-------------------------:|-------------------------:|-------------------------------------:|----------------------------------:|-----------------------:|--------------------------:|---------------:|------------------:|----------------:|---------------------------------:|------------------------:|---------------:|--------------------:|-------------------------------------:|
    | aapl     | 1985-09-30 00:00:00 | 12M          |          3.4272e+09  |   0.017857 |      1.076e+09  |                                          4.18e+07  |                                      4.18e+07  |            3.4272e+09  |     0.017857 |                         6.12e+07  | 1.473e+08 |      nan |                          nan |                    nan |    8.423e+08  |               nan |                           nan |              nan |                          nan |   6.12e+07  |                     6.12e+07  |                       6.12e+07  |                      nan |                                         6.12e+07  |                                             6.12e+07  |                                nan |                                   6.12e+07  |                 nan |                                    nan |          2.163e+08 |        7.752e+07   |         6.95e+08   |         1.473e+08 |         1.9183e+09 |            -2.72e+07 |                               nan |                      nan |                   nan |      1.2e+08   |                1.076e+09  |                4.18e+07  |                      nan |                                  nan |                        6.532e+08  |              -2.72e+07 |              -1.088e+07   |      5.88e+07  |          0.4      |      1.771e+09  |                        1.473e+08 |                     nan |     1.9183e+09 |           -2.72e+07 |                            -2.72e+07 |
    | aapl     | 1986-09-30 00:00:00 | 12M          |          3.59333e+09 |   0.042857 |      8.4e+08    |                                          5.11e+07  |                                      5.11e+07  |            3.59333e+09 |     0.042857 |                         1.54e+08  | 2.735e+08 |      nan |                          nan |                    nan |    1.0619e+09 |               nan |                           nan |              nan |                          nan |   1.54e+08  |                     1.54e+08  |                       1.54e+08  |                      nan |                                         1.54e+08  |                                             1.54e+08  |                                nan |                                   1.54e+08  |                 nan |                                    nan |          2.884e+08 |        1.3228e+08  |         7.884e+08  |         2.735e+08 |         1.9019e+09 |             3.62e+07 |                               nan |                      nan |                   nan |      3.098e+08 |                8.4e+08    |                5.11e+07  |                      nan |                                  nan |                        7.373e+08  |               3.62e+07 |               1.448e+07   |      1.558e+08 |          0.4      |      1.6284e+09 |                        2.735e+08 |                     nan |     1.9019e+09 |            3.62e+07 |                             3.62e+07 |
    | aapl     | 1987-09-30 00:00:00 | 12M          |          3.66867e+09 |   0.059286 |      1.2257e+09 |                                          7.05e+07  |                                      7.05e+07  |            3.66867e+09 |     0.059286 |                         2.175e+08 | 3.715e+08 |      nan |                          nan |                    nan |    1.4354e+09 |               nan |                           nan |              nan |                          nan |   2.175e+08 |                     2.175e+08 |                       2.175e+08 |                      nan |                                         2.175e+08 |                                             2.175e+08 |                                nan |                                   2.175e+08 |                 nan |                                    nan |          4.031e+08 |        1.9416e+08  |         1.0639e+09 |         3.715e+08 |         2.6611e+09 |             3.89e+07 |                               nan |                      nan |                   nan |      4.104e+08 |                1.2257e+09 |                7.05e+07  |                      nan |                                  nan |                        9.934e+08  |               3.89e+07 |               1.556e+07   |      1.929e+08 |          0.4      |      2.2896e+09 |                        3.715e+08 |                     nan |     2.6611e+09 |            3.89e+07 |                             3.89e+07 |
    | aapl     | 1988-09-30 00:00:00 | 12M          |          3.63909e+09 |   0.11     |      1.9132e+09 |                                          7.77e+07  |                                      7.77e+07  |            3.63909e+09 |     0.11     |                         4.003e+08 | 6.203e+08 |      nan |                          nan |                    nan |    2.1582e+09 |               nan |                           nan |              nan |                          nan |   4.003e+08 |                     4.003e+08 |                       4.003e+08 |                      nan |                                         4.003e+08 |                                             4.003e+08 |                                nan |                                   4.003e+08 |                 nan |                                    nan |          6.622e+08 |        3.78461e+08 |         1.5379e+09 |         6.203e+08 |         4.0714e+09 |             3.58e+07 |                               nan |                      nan |                   nan |      6.562e+08 |                1.9132e+09 |                7.77e+07  |                      nan |                                  nan |                        1.4602e+09 |               3.58e+07 |               1.3961e+07  |      2.559e+08 |          0.389973 |      3.4511e+09 |                        6.203e+08 |                     nan |     4.0714e+09 |            3.58e+07 |                             3.58e+07 |
    | aapl     | 1989-09-30 00:00:00 | 12M          |          3.59096e+09 |   0.126429 |      2.57e+09   |                                          1.248e+08 |                                      1.248e+08 |            3.59096e+09 |     0.126429 |                         4.54e+08  | 6.343e+08 |      nan |                          nan |                    nan |    2.714e+09  |               nan |                           nan |              nan |                          nan |   4.54e+08  |                     4.54e+08  |                       4.54e+08  |                      nan |                                         4.54e+08  |                                             4.54e+08  |                                nan |                                   4.54e+08  |                 nan |                                    nan |          6.491e+08 |        3.86903e+08 |         2.0797e+09 |         6.343e+08 |         5.284e+09  |             1.1e+08  |                               nan |                      nan |                   nan |      7.443e+08 |                2.57e+09   |                1.248e+08 |                      nan |                                  nan |                        1.9549e+09 |               1.1e+08  |               4.29034e+07 |      2.903e+08 |          0.390031 |      4.6497e+09 |                        6.343e+08 |                     nan |     5.284e+09  |            1.1e+08  |                             1.1e+08  |

#### **p_valuation_measures**


=== "Details"

    - *Description*:  Retrieves valuation measures for given symbol(s)
    - *Return*:  `pandas.DataFrame`
    - *Arguments*:

    | Argument   | Type   | Default   | Required   | Options                       |
    |:-----------|:-------|:----------|:-----------|:------------------------------|
    | frequency  | `str`  | `q`       | optional   | Annual - `a`<br>Quarter - `q`<br>Monthly - `m` |

=== "Example"

    ```python hl_lines="2"
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    df = aapl.p_valuation_measures()
    df.head()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   EnterpriseValue |   EnterprisesValueEBITDARatio |   EnterprisesValueRevenueRatio |   ForwardPeRatio |   MarketCap |   PbRatio |   PeRatio |   PegRatio |   PsRatio |
    |:---------|:--------------------|:-------------|------------------:|------------------------------:|-------------------------------:|-----------------:|------------:|----------:|----------:|-----------:|----------:|
    | aapl     | 1985-09-30 00:00:00 | 3M           |       6.37162e+08 |                     -0.468054 |                        1.55519 |              nan | 9.74162e+08 |   1.7696  |   15.7505 |        nan |  0.502489 |
    | aapl     | 1985-12-31 00:00:00 | 3M           |       1.02207e+09 |                      1.91435  |                        1.91435 |              nan | 1.35907e+09 |   2.4688  |   18.9658 |        nan |  0.774886 |
    | aapl     | 1986-03-31 00:00:00 | 3M           |       1.43289e+09 |                      3.50425  |                        3.50425 |              nan | 1.76989e+09 |   3.21505 |   19.0878 |        nan |  1.02454  |
    | aapl     | 1986-06-30 00:00:00 | 3M           |       1.94685e+09 |                      4.34274  |                        4.34274 |              nan | 2.28385e+09 |   4.14868 |   15.7348 |        nan |  1.26824  |
    | aapl     | 1986-09-30 00:00:00 | 3M           |       1.52184e+09 |                     -1.3617   |                        2.97932 |              nan | 2.09804e+09 |   3.02267 |   13.9584 |        nan |  1.13023  |

### Multiple

#### **p_all_financial_data**

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
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    aapl.p_all_financial_data()
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |   AccountsPayable |   AccountsReceivable |   AccumulatedDepreciation |   AdditionalPaidInCapital |   AllowanceForDoubtfulAccountsReceivable |   AvailableForSaleSecurities |   BasicAverageShares |   BasicEPS |   BeginningCashPosition |   BuildingsAndImprovements |   CapitalExpenditure |   CapitalStock |   CashAndCashEquivalents |   CashCashEquivalentsAndShortTermInvestments |   CashDividendsPaid |   CashEquivalents |   CashFinancial |   CashFlowFromContinuingFinancingActivities |   ChangeInAccountPayable |   ChangeInCashSupplementalAsReported |   ChangeInInventory |   ChangeInWorkingCapital |   ChangesInAccountReceivables |   CommercialPaper |   CommonStock |   CommonStockEquity |   CommonStockIssuance |   CostOfRevenue |   CurrentAccruedExpenses |   CurrentAssets |   CurrentDebt |   CurrentDebtAndCapitalLeaseObligation |   CurrentDeferredAssets |   CurrentDeferredLiabilities |   CurrentDeferredRevenue |   CurrentDeferredTaxesAssets |   CurrentLiabilities |   CurrentNotesPayable |   DeferredIncomeTax |   DepreciationAmortizationDepletionIncomeStatement |   DepreciationAndAmortization |   DepreciationAndAmortizationInIncomeStatement |   DilutedAverageShares |   DilutedEPS |   DilutedNIAvailtoComStockholders |      EBIT |   EarningsFromEquityInterest |   EndCashPosition |   EnterpriseValue |   EnterprisesValueEBITDARatio |   EnterprisesValueRevenueRatio |   FinishedGoods |   ForeignCurrencyTranslationAdjustments |   ForwardPeRatio |   FreeCashFlow |   GainOnSaleOfSecurity |   GainsLossesNotAffectingRetainedEarnings |   Goodwill |   GoodwillAndOtherIntangibleAssets |   GrossAccountsReceivable |   GrossPPE |   GrossProfit |   IncomeTaxPayable |   InterestExpense |   InterestExpenseNonOperating |   InterestIncome |   InterestIncomeNonOperating |   Inventory |   InvestedCapital |   InvestingCashFlow |   InvestmentinFinancialAssets |   InvestmentsAndAdvances |   LandAndImprovements |   Leases |   LongTermDebt |   LongTermDebtAndCapitalLeaseObligation |   MachineryFurnitureEquipment |   MarketCap |   NetDebt |   NetIncome |   NetIncomeCommonStockholders |   NetIncomeContinuousOperations |   NetIncomeExtraordinary |   NetIncomeFromContinuingAndDiscontinuedOperation |   NetIncomeFromContinuingOperationNetMinorityInterest |   NetIncomeFromTaxLossCarryforward |   NetIncomeIncludingNoncontrollingInterests |   NetInterestIncome |   NetNonOperatingInterestIncomeExpense |   NetOtherFinancingCharges |   NetOtherInvestingChanges |    NetPPE |   NetTangibleAssets |   NonCurrentDeferredAssets |   NonCurrentDeferredLiabilities |   NonCurrentDeferredRevenue |   NonCurrentDeferredTaxesAssets |   NonCurrentDeferredTaxesLiabilities |   NonCurrentPrepaidAssets |   NormalizedEBITDA |   NormalizedIncome |   OperatingCashFlow |   OperatingExpense |   OperatingIncome |   OperatingRevenue |   OrdinarySharesNumber |   OtherCurrentAssets |   OtherCurrentBorrowings |   OtherCurrentLiabilities |   OtherEquityAdjustments |   OtherEquityInterest |   OtherIncomeExpense |   OtherIntangibleAssets |   OtherNonCashItems |   OtherNonCurrentAssets |   OtherNonCurrentLiabilities |   OtherNonOperatingIncomeExpenses |   OtherOperatingExpenses |   OtherPayable |   OtherProperties |   OtherReceivables |   OtherShortTermInvestments |   OtherSpecialCharges |    Payables |   PayablesAndAccruedExpenses |   PbRatio |   PeRatio |   PegRatio |   PensionandOtherPostRetirementBenefitPlansCurrent |   PreferredStock |   PreferredStockEquity |   PrepaidAssets |   PretaxIncome |   Properties |   PsRatio |   PurchaseOfBusiness |   PurchaseOfInvestment |   RawMaterials |   Receivables |   ReconciledCostOfRevenue |   ReconciledDepreciation |   RepaymentOfDebt |   RepurchaseOfCapitalStock |   ResearchAndDevelopment |   RestructuringAndMergernAcquisition |   RetainedEarnings |   SaleOfInvestment |   SellingGeneralAndAdministration |   ShareIssued |   SpecialIncomeCharges |   StockBasedCompensation |   StockholdersEquity |   TangibleBookValue |   TaxEffectOfUnusualItems |   TaxProvision |   TaxRateForCalcs |   TotalAssets |   TotalCapitalization |   TotalDebt |   TotalEquityGrossMinorityInterest |   TotalExpenses |   TotalLiabilitiesNetMinorityInterest |   TotalNonCurrentAssets |   TotalNonCurrentLiabilitiesNetMinorityInterest |   TotalOperatingIncomeAsReported |   TotalOtherFinanceCost |   TotalRevenue |   TotalTaxPayable |   TotalUnusualItems |   TotalUnusualItemsExcludingGoodwill |   TradeandOtherPayablesNonCurrent |   WorkInProcess |   WorkingCapital |
    |:---------|:--------------------|:-------------|------------------:|---------------------:|--------------------------:|--------------------------:|-----------------------------------------:|-----------------------------:|---------------------:|-----------:|------------------------:|---------------------------:|---------------------:|---------------:|-------------------------:|---------------------------------------------:|--------------------:|------------------:|----------------:|--------------------------------------------:|-------------------------:|-------------------------------------:|--------------------:|-------------------------:|------------------------------:|------------------:|--------------:|--------------------:|----------------------:|----------------:|-------------------------:|----------------:|--------------:|---------------------------------------:|------------------------:|-----------------------------:|-------------------------:|-----------------------------:|---------------------:|----------------------:|--------------------:|---------------------------------------------------:|------------------------------:|-----------------------------------------------:|-----------------------:|-------------:|----------------------------------:|----------:|-----------------------------:|------------------:|------------------:|------------------------------:|-------------------------------:|----------------:|----------------------------------------:|-----------------:|---------------:|-----------------------:|------------------------------------------:|-----------:|-----------------------------------:|--------------------------:|-----------:|--------------:|-------------------:|------------------:|------------------------------:|-----------------:|-----------------------------:|------------:|------------------:|--------------------:|------------------------------:|-------------------------:|----------------------:|---------:|---------------:|----------------------------------------:|------------------------------:|------------:|----------:|------------:|------------------------------:|--------------------------------:|-------------------------:|--------------------------------------------------:|------------------------------------------------------:|-----------------------------------:|--------------------------------------------:|--------------------:|---------------------------------------:|---------------------------:|---------------------------:|----------:|--------------------:|---------------------------:|--------------------------------:|----------------------------:|--------------------------------:|-------------------------------------:|--------------------------:|-------------------:|-------------------:|--------------------:|-------------------:|------------------:|-------------------:|-----------------------:|---------------------:|-------------------------:|--------------------------:|-------------------------:|----------------------:|---------------------:|------------------------:|--------------------:|------------------------:|-----------------------------:|----------------------------------:|-------------------------:|---------------:|------------------:|-------------------:|----------------------------:|----------------------:|------------:|-----------------------------:|----------:|----------:|-----------:|---------------------------------------------------:|-----------------:|-----------------------:|----------------:|---------------:|-------------:|----------:|---------------------:|-----------------------:|---------------:|--------------:|--------------------------:|-------------------------:|------------------:|---------------------------:|-------------------------:|-------------------------------------:|-------------------:|-------------------:|----------------------------------:|--------------:|-----------------------:|-------------------------:|---------------------:|--------------------:|--------------------------:|---------------:|------------------:|--------------:|----------------------:|------------:|-----------------------------------:|----------------:|--------------------------------------:|------------------------:|------------------------------------------------:|---------------------------------:|------------------------:|---------------:|------------------:|--------------------:|-------------------------------------:|----------------------------------:|----------------:|-----------------:|
    | aapl     | 1985-09-30 00:00:00 | 12M          |       nan         |                  nan |                -8.52e+07  |                       nan |                                      nan |                          nan |          3.4272e+09  |   0.017857 |             nan         |                        nan |           nan        |            nan |                3.37e+08  |                                    3.37e+08  |          nan        |               nan |             nan |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |               nan |           nan |          5.505e+08  |             nan       |      1.076e+09  |                      nan |      8.221e+08  |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            2.954e+08 |                   nan |         nan         |                                          4.18e+07  |                   nan         |                                      4.18e+07  |            3.4272e+09  |     0.017857 |                         6.12e+07  | 1.473e+08 |                          nan |               nan |       6.37162e+08 |                       3.36945 |                       0.332149 |             nan |                                     nan |              nan |    nan         |                    nan |                                       nan |        nan |                                nan |                       nan |  1.756e+08 |    8.423e+08  |                nan |               nan |                           nan |              nan |                          nan |   1.67e+08  |        5.505e+08  |         nan         |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan | 9.74162e+08 |       nan |   6.12e+07  |                     6.12e+07  |                       6.12e+07  |                      nan |                                         6.12e+07  |                                             6.12e+07  |                                nan |                                   6.12e+07  |                 nan |                                    nan |                        nan |                 nan        | 9.04e+07  |          5.505e+08  |                        nan |                       9.03e+07  |                         nan |                             nan |                            9.03e+07  |                       nan |          2.163e+08 |        7.752e+07   |         nan         |         6.95e+08   |         1.473e+08 |         1.9183e+09 |            3.4636e+09  |            9.79e+07  |                      nan |               nan         |                      nan |             2.302e+08 |            -2.72e+07 |                     nan |                 nan |               2.37e+07  |                          nan |                               nan |                      nan |            nan |               nan |                nan |                         nan |                   nan | nan         |                  nan         |   1.7696  |   15.7505 |        nan |                                                nan |              nan |                    nan |             nan |      1.2e+08   |          nan |  0.502489 |                  nan |            nan         |            nan |     2.202e+08 |                1.076e+09  |                4.18e+07  |               nan |                 nan        |                      nan |                                  nan |         3.203e+08  |        nan         |                        6.532e+08  |   3.4636e+09  |              -2.72e+07 |                      nan |           5.505e+08  |          5.505e+08  |              -1.088e+07   |      5.88e+07  |          0.4      |    9.362e+08  |            5.505e+08  | nan         |                         5.505e+08  |      1.771e+09  |                            3.857e+08  |               1.141e+08 |                                       9.03e+07  |                        1.473e+08 |                     nan |     1.9183e+09 |               nan |           -2.72e+07 |                            -2.72e+07 |                               nan |             nan |       5.267e+08  |
    | aapl     | 1986-09-30 00:00:00 | 12M          |       nan         |                  nan |                -1.147e+08 |                       nan |                                      nan |                          nan |          3.59333e+09 |   0.042857 |             nan         |                        nan |           nan        |            nan |                5.762e+08 |                                    5.762e+08 |          nan        |               nan |             nan |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |               nan |           nan |          6.941e+08  |             nan       |      8.4e+08    |                      nan |      1.0409e+09 |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            3.285e+08 |                   nan |         nan         |                                          5.11e+07  |                   nan         |                                      5.11e+07  |            3.59333e+09 |     0.042857 |                         1.54e+08  | 2.735e+08 |                          nan |               nan |       1.52184e+09 |                       4.68835 |                       0.800167 |             nan |                                     nan |              nan |    nan         |                    nan |                                       nan |        nan |                                nan |                       nan |  2.22e+08  |    1.0619e+09 |                nan |               nan |                           nan |              nan |                          nan |   1.087e+08 |        6.941e+08  |         nan         |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan | 2.09804e+09 |       nan |   1.54e+08  |                     1.54e+08  |                       1.54e+08  |                      nan |                                         1.54e+08  |                                             1.54e+08  |                                nan |                                   1.54e+08  |                 nan |                                    nan |                        nan |                 nan        | 1.073e+08 |          6.941e+08  |                        nan |                       1.375e+08 |                         nan |                             nan |                            1.375e+08 |                       nan |          2.884e+08 |        1.3228e+08  |         nan         |         7.884e+08  |         2.735e+08 |         1.9019e+09 |            3.50717e+09 |            9.29e+07  |                      nan |               nan         |                      nan |             2.198e+08 |             3.62e+07 |                     nan |                 nan |               1.19e+07  |                          nan |                               nan |                      nan |            nan |               nan |                nan |                         nan |                   nan | nan         |                  nan         |   3.02267 |   13.9584 |        nan |                                                nan |              nan |                    nan |             nan |      3.098e+08 |          nan |  1.13023  |                  nan |            nan         |            nan |     2.631e+08 |                8.4e+08    |                5.11e+07  |               nan |                 nan        |                      nan |                                  nan |         4.743e+08  |        nan         |                        7.373e+08  |   3.50717e+09 |               3.62e+07 |                      nan |           6.941e+08  |          6.941e+08  |               1.448e+07   |      1.558e+08 |          0.4      |    1.1601e+09 |            6.941e+08  | nan         |                         6.941e+08  |      1.6284e+09 |                            4.66e+08   |               1.192e+08 |                                       1.375e+08 |                        2.735e+08 |                     nan |     1.9019e+09 |               nan |            3.62e+07 |                             3.62e+07 |                               nan |             nan |       7.124e+08  |
    | aapl     | 1987-09-30 00:00:00 | 12M          |       nan         |                  nan |                -1.587e+08 |                       nan |                                      nan |                          nan |          3.66867e+09 |   0.059286 |             nan         |                        nan |           nan        |            nan |                5.651e+08 |                                    5.651e+08 |          nan        |               nan |             nan |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |               nan |           nan |          8.365e+08  |             nan       |      1.2257e+09 |                      nan |      1.3074e+09 |   nan         |                            nan         |                     nan |                          nan |                      nan |                          nan |            4.787e+08 |                   nan |         nan         |                                          7.05e+07  |                   nan         |                                      7.05e+07  |            3.66867e+09 |     0.059286 |                         2.175e+08 | 3.715e+08 |                          nan |               nan |       6.55887e+09 |                      14.8391  |                       2.46472  |             nan |                                     nan |              nan |    nan         |                    nan |                                       nan |        nan |                                nan |                       nan |  2.891e+08 |    1.4354e+09 |                nan |               nan |                           nan |              nan |                          nan |   2.258e+08 |        8.365e+08  |         nan         |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan | 7.12397e+09 |       nan |   2.175e+08 |                     2.175e+08 |                       2.175e+08 |                      nan |                                         2.175e+08 |                                             2.175e+08 |                                nan |                                   2.175e+08 |                 nan |                                    nan |                        nan |                 nan        | 1.304e+08 |          8.365e+08  |                        nan |                       1.628e+08 |                         nan |                             nan |                            1.628e+08 |                       nan |          4.031e+08 |        1.9416e+08  |         nan         |         1.0639e+09 |         3.715e+08 |         2.6611e+09 |            3.53046e+09 |            1.109e+08 |                      nan |               nan         |                      nan |             2.634e+08 |             3.89e+07 |                     nan |                 nan |               4.01e+07  |                      -100000 |                               nan |                      nan |            nan |               nan |                nan |                         nan |                   nan | nan         |                  nan         |   8.5164  |   34.036  |        nan |                                                nan |              nan |                    nan |             nan |      4.104e+08 |          nan |  2.78188  |                  nan |            nan         |            nan |     4.056e+08 |                1.2257e+09 |                7.05e+07  |               nan |                 nan        |                      nan |                                  nan |         5.731e+08  |        nan         |                        9.934e+08  |   3.53046e+09 |               3.89e+07 |                      nan |           8.365e+08  |          8.365e+08  |               1.556e+07   |      1.929e+08 |          0.4      |    1.4779e+09 |            8.365e+08  | nan         |                         8.365e+08  |      2.2896e+09 |                            6.414e+08  |               1.705e+08 |                                       1.627e+08 |                        3.715e+08 |                     nan |     2.6611e+09 |               nan |            3.89e+07 |                             3.89e+07 |                               nan |             nan |       8.287e+08  |
    | aapl     | 1988-09-30 00:00:00 | 12M          |       nan         |                  nan |                -2.13e+08  |                       nan |                                      nan |                          nan |          3.63909e+09 |   0.11     |             nan         |                        nan |           nan        |            nan |                5.457e+08 |                                    5.457e+08 |          nan        |               nan |             nan |                                  nan        |                      nan |                           nan        |          nan        |               nan        |                           nan |               nan |           nan |          1.0034e+09 |             nan       |      1.9132e+09 |                      nan |      1.783e+09  |     1.279e+08 |                              1.279e+08 |                     nan |                          nan |                      nan |                          nan |            8.271e+08 |                   nan |         nan         |                                          7.77e+07  |                   nan         |                                      7.77e+07  |            3.63909e+09 |     0.11     |                         4.003e+08 | 6.203e+08 |                          nan |               nan |       4.89192e+09 |                       7.00848 |                       1.20153  |             nan |                                     nan |              nan |    nan         |                    nan |                                       nan |        nan |                                nan |                       nan |  4.204e+08 |    2.1582e+09 |                nan |               nan |                           nan |              nan |                          nan |   4.615e+08 |        1.1313e+09 |         nan         |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan | 5.30972e+09 |       nan |   4.003e+08 |                     4.003e+08 |                       4.003e+08 |                      nan |                                         4.003e+08 |                                             4.003e+08 |                                nan |                                   4.003e+08 |                 nan |                                    nan |                        nan |                 nan        | 2.074e+08 |          1.0034e+09 |                        nan |                       2.516e+08 |                         nan |                             nan |                            2.516e+08 |                       nan |          6.622e+08 |        3.78461e+08 |         nan         |         1.5379e+09 |         6.203e+08 |         4.0714e+09 |            3.4375e+09  |            1.37e+08  |                      nan |                 6.992e+08 |                      nan |             2.269e+08 |             3.58e+07 |                     nan |                 nan |               9.17e+07  |                          nan |                               nan |                      nan |            nan |               nan |                nan |                         nan |                   nan | nan         |                  nan         |   5.29172 |   14.0422 |        nan |                                                nan |              nan |                    nan |             nan |      6.562e+08 |          nan |  1.38063  |                  nan |            nan         |            nan |     6.388e+08 |                1.9132e+09 |                7.77e+07  |               nan |                 nan        |                      nan |                                  nan |         7.765e+08  |        nan         |                        1.4602e+09 |   3.4375e+09  |               3.58e+07 |                      nan |           1.0034e+09 |          1.0034e+09 |               1.3961e+07  |      2.559e+08 |          0.389973 |    2.0821e+09 |            1.0034e+09 |   1.279e+08 |                         1.0034e+09 |      3.4511e+09 |                            1.0787e+09 |               2.991e+08 |                                       2.516e+08 |                        6.203e+08 |                     nan |     4.0714e+09 |               nan |            3.58e+07 |                             3.58e+07 |                               nan |             nan |       9.559e+08  |
    | aapl     | 1989-09-30 00:00:00 | 12M          |         3.342e+08 |                  nan |                -3.091e+08 |                       nan |                                      nan |                          nan |          3.59096e+09 |   0.126429 |               3.724e+08 |                        nan |            -2.39e+08 |            nan |                4.383e+08 |                                    4.383e+08 |           -5.03e+07 |               nan |             nan |                                   -3.83e+07 |                      nan |                             6.59e+07 |           -1.39e+07 |                -1.09e+08 |                           nan |               nan |           nan |          1.4857e+09 |               9.6e+07 |      2.57e+09   |                      nan |      2.2944e+09 |     5.68e+07  |                              5.68e+07  |                     nan |                          nan |                      nan |                          nan |            8.953e+08 |                   nan |           1.113e+08 |                                          1.248e+08 |                     1.248e+08 |                                      1.248e+08 |            3.59096e+09 |     0.126429 |                         4.54e+08  | 6.343e+08 |                          nan |                 0 |       5.20121e+09 |                       6.85182 |                       0.984333 |             nan |                                     nan |              nan |      2.683e+08 |                    nan |                                       nan |        nan |                                nan |                       nan |  6.433e+08 |    2.714e+09  |                nan |               nan |                           nan |              nan |                          nan |   4.754e+08 |        1.5425e+09 |          -4.031e+08 |                           nan |                      nan |                   nan |      nan |            nan |                                     nan |                           nan | 5.61901e+09 |       nan |   4.54e+08  |                     4.54e+08  |                       4.54e+08  |                      nan |                                         4.54e+08  |                                             4.54e+08  |                                nan |                                   4.54e+08  |                 nan |                                    nan |                        nan |                   3.32e+07 | 3.342e+08 |          1.4857e+09 |                        nan |                       3.629e+08 |                         nan |                             nan |                            3.629e+08 |                       nan |          6.491e+08 |        3.86903e+08 |           5.073e+08 |         2.0797e+09 |         6.343e+08 |         5.284e+09  |            3.53556e+09 |            5.879e+08 |                      nan |                 5.043e+08 |                      nan |             3.098e+08 |             1.1e+08  |                     nan |              100000 |               1.153e+08 |                          nan |                               nan |                      nan |            nan |               nan |                nan |                         nan |                   nan |   3.342e+08 |                    3.342e+08 |   5.59997 |   14.2628 |        nan |                                                nan |              nan |                    nan |             nan |      7.443e+08 |          nan |  1.08872  |                  nan |             -9.847e+08 |            nan |     7.928e+08 |                2.57e+09   |                1.248e+08 |               nan |                  -1.29e+07 |                      nan |                                  nan |         1.1759e+09 |          7.874e+08 |                        1.9549e+09 |   3.53556e+09 |               1.1e+08  |                      nan |           1.4857e+09 |          1.4857e+09 |               4.29034e+07 |      2.903e+08 |          0.390031 |    2.7439e+09 |            1.4857e+09 |   5.68e+07  |                         1.4857e+09 |      4.6497e+09 |                            1.2582e+09 |               4.495e+08 |                                       3.629e+08 |                        6.343e+08 |                     nan |     5.284e+09  |               nan |            1.1e+08  |                             1.1e+08  |                               nan |             nan |       1.3991e+09 |

#### **p_get_financial_data**

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
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    types = ['TotalDebt', 'TotalAssets', 'EBIT', 'EBITDA', 'PeRatio']
    aapl.p_get_financial_data(types, trailing=False)
    ```

=== "Data"

    | symbol   | asOfDate            | periodType   |      EBIT |   EBITDA |   PeRatio |   TotalAssets |   TotalDebt |
    |:---------|:--------------------|:-------------|----------:|---------:|----------:|--------------:|------------:|
    | aapl     | 1985-09-30 00:00:00 | 12M          | 1.473e+08 |      nan |   15.7505 |    9.362e+08  | nan         |
    | aapl     | 1986-09-30 00:00:00 | 12M          | 2.735e+08 |      nan |   13.9584 |    1.1601e+09 | nan         |
    | aapl     | 1987-09-30 00:00:00 | 12M          | 3.715e+08 |      nan |   34.036  |    1.4779e+09 | nan         |
    | aapl     | 1988-09-30 00:00:00 | 12M          | 6.203e+08 |      nan |   14.0422 |    2.0821e+09 |   1.279e+08 |
    | aapl     | 1989-09-30 00:00:00 | 12M          | 6.343e+08 |      nan |   14.2628 |    2.7439e+09 |   5.68e+07  |


## Miscellaneous

#### **p_company_360**

=== "Details"

    - *Description*:  Retrieve data related to innovation, hiring, insider sentiment, developments, supply chain, sustainability, and company outlook for given symbol(s) 
    - *Return*:  `dict`

=== "Example"

    ```python
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    aapl.p_company_360
    ```

=== "Data"

    ```python
    {
        'aapl': {
            'metaData': {
                'symbol': 'aapl'
            },
            'innovations': {
                'score': 94.0,
                'text': 'Outperform',
                'sectorAvg': 52.6145648312611
            },
            'sustainability': {
                'totalScore': 64,
                'totalScorePercentile': 83,
                'environmentScore': 66,
                'environmentScorePercentile': 85,
                'socialScore': 66,
                'socialScorePercentile': 70,
                'governanceScore': 66,
                'governanceScorePercentile': 89,
                'controversyLevel': 2
            },
            'insiderSentiments': {
                'vickersIndex': -57,
                'vickersIndexChange': 0,
                'sentimentText': 'Negative'
            },
            'significantDevelopments': [{
                'id': 4252812,
                'symbol': 'AAPL',
                'date': '2020-07-30',
                'headline': 'Apple Reports Q3 Earnings Of $2.58 Per Share'
            }, {
                'id': 4248528,
                'symbol': 'AAPL',
                'date': '2020-07-23',
                'headline': 'Apple Faces Multi-State Consumer Protection Probe - Axios'
            }, {
                'id': 4246944,
                'symbol': 'AAPL',
                'date': '2020-07-21',
                'headline': 'Apple To Become Carbon Neutral Across Manufacturing Supply Chain, Product Life Cycle By 2030'
            }, {
                'id': 4244661,
                'symbol': 'AAPL',
                'date': '2020-07-15',
                'headline': 'TomTom Eyes Better Operational Revenues In H2 - Conf Call'
            }, {
                'id': 4241255,
                'symbol': 'AAPL',
                'date': '2020-07-07',
                'headline': 'Apple Opts For OLED Screens For Entire 5G iPhone Range - Nikkei'
            }],
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
            'hiring': [{
                'month': 2,
                'year': 2019,
                'hiringChangePercent': -0.18330134,
                'sectorAvgChangePercent': -0.21709615
            }, {
                'month': 3,
                'year': 2019,
                'hiringChangePercent': 0.89659226,
                'sectorAvgChangePercent': 0.998416
            }, {
                'month': 4,
                'year': 2019,
                'hiringChangePercent': -0.19826518,
                'sectorAvgChangePercent': -0.48218337
            }, {
                'month': 5,
                'year': 2019,
                'hiringChangePercent': -0.311051,
                'sectorAvgChangePercent': -0.3965309
            }, {
                'month': 6,
                'year': 2019,
                'hiringChangePercent': -0.11497476,
                'sectorAvgChangePercent': -0.13750465
            }, {
                'month': 7,
                'year': 2019,
                'hiringChangePercent': -0.20278834,
                'sectorAvgChangePercent': -0.14868993
            }, {
                'month': 8,
                'year': 2019,
                'hiringChangePercent': 0.057233706,
                'sectorAvgChangePercent': 0.18088417
            }, {
                'month': 9,
                'year': 2019,
                'hiringChangePercent': -0.25413534,
                'sectorAvgChangePercent': -0.2411767
            }, {
                'month': 10,
                'year': 2019,
                'hiringChangePercent': 0.25705644,
                'sectorAvgChangePercent': -0.03286806
            }, {
                'month': 11,
                'year': 2019,
                'hiringChangePercent': -0.21892542,
                'sectorAvgChangePercent': -0.17327583
            }, {
                'month': 12,
                'year': 2019,
                'hiringChangePercent': 0.1550308,
                'sectorAvgChangePercent': -0.012864476
            }, {
                'month': 1,
                'year': 2020,
                'hiringChangePercent': -0.13511111,
                'sectorAvgChangePercent': -0.031074993
            }, {
                'month': 2,
                'year': 2020,
                'hiringChangePercent': -0.18602261,
                'sectorAvgChangePercent': -0.1585546
            }, {
                'month': 3,
                'year': 2020,
                'hiringChangePercent': 0.24368687,
                'sectorAvgChangePercent': 0.90801805
            }, {
                'month': 4,
                'year': 2020,
                'hiringChangePercent': -0.17766498,
                'sectorAvgChangePercent': -0.59851396
            }, {
                'month': 5,
                'year': 2020,
                'hiringChangePercent': -0.24444444,
                'sectorAvgChangePercent': -0.12799595
            }, {
                'month': 6,
                'year': 2020,
                'hiringChangePercent': 0.0,
                'sectorAvgChangePercent': -0.04588681
            }, {
                'month': 7,
                'year': 2020,
                'hiringChangePercent': -0.6535948,
                'sectorAvgChangePercent': -0.6510271
            }],
            'supplyChain': {
                'topSuppliers': [{
                    'entityYName': 'POSCO',
                    'entityYTicker': 'PKXFF',
                    'relationToType': 'Supplier',
                    'exposureTotal': 0.016477,
                    'exposureFinancial': 0.000125,
                    'exposureMedia': 0.000301,
                    'exposureEconomic': 0.049003,
                    'economicValue': 8136720000.0
                }, {
                    'entityYName': 'ENEOS Holdings, Inc.',
                    'entityYTicker': 'JXHGF',
                    'relationToType': 'Supplier',
                    'exposureTotal': 0.012025,
                    'exposureFinancial': 1.7e-05,
                    'exposureMedia': 0.00015,
                    'exposureEconomic': 0.035907,
                    'economicValue': 5962190000.0
                }, {
                    'entityYName': 'Jabil Inc.',
                    'entityYTicker': 'JBL',
                    'relationToType': 'Supplier',
                    'exposureTotal': 0.018778,
                    'exposureFinancial': 0.020268,
                    'exposureMedia': 0.000902,
                    'exposureEconomic': 0.035164,
                    'economicValue': 5838770000.0
                }, {
                    'entityYName': 'Quanta Computer Inc.',
                    'entityYTicker': '2382.TW',
                    'relationToType': 'Supplier',
                    'exposureTotal': 0.014186,
                    'exposureFinancial': 0.007526,
                    'exposureMedia': 0.001955,
                    'exposureEconomic': 0.033077,
                    'economicValue': 5492230000.0
                }, {
                    'entityYName': 'Hon Hai Precision Industry Co., Ltd.',
                    'entityYTicker': 'HNHAF',
                    'relationToType': 'Supplier',
                    'exposureTotal': 0.012083,
                    'exposureFinancial': 0.003068,
                    'exposureMedia': 0.00015,
                    'exposureEconomic': 0.033029,
                    'economicValue': 5484340000.0
                }],
                'topCustomers': [{
                    'entityYName': 'Costco Wholesale Corporation',
                    'entityYTicker': 'COST',
                    'relationToType': 'Customer',
                    'exposureTotal': 0.034341,
                    'exposureFinancial': 0.018305,
                    'exposureMedia': 0.034568,
                    'exposureEconomic': 0.050148,
                    'economicValue': 10429790000.0
                }, {
                    'entityYName': 'AT&T Inc.',
                    'entityYTicker': 'T',
                    'relationToType': 'Customer',
                    'exposureTotal': 0.078284,
                    'exposureFinancial': 0.032478,
                    'exposureMedia': 0.158848,
                    'exposureEconomic': 0.043524,
                    'economicValue': 9052120000.0
                }, {
                    'entityYName': 'Cencosud S.A.',
                    'entityYTicker': 'CENCOSUD.SN',
                    'relationToType': 'Customer',
                    'exposureTotal': 0.012515,
                    'exposureFinancial': 0.000711,
                    'exposureMedia': 0.000823,
                    'exposureEconomic': 0.03601,
                    'economicValue': 7489330000.0
                }, {
                    'entityYName': 'Vodafone Idea Limited',
                    'entityYTicker': 'IDEA.NS',
                    'relationToType': 'Customer',
                    'exposureTotal': 0.011229,
                    'exposureFinancial': 8.8e-05,
                    'exposureMedia': 0.000823,
                    'exposureEconomic': 0.032777,
                    'economicValue': 6816940000.0
                }, {
                    'entityYName': 'Mazda Motor Corporation',
                    'entityYTicker': 'MZDAF',
                    'relationToType': 'Customer',
                    'exposureTotal': 0.011536,
                    'exposureFinancial': 0.000236,
                    'exposureMedia': 0.001646,
                    'exposureEconomic': 0.032727,
                    'economicValue': 6806610000.0
                }],
                'remainingSuppliers': 0,
                'remainingCustomers': 0
            },
            'earnings': [{
                'quarter': 'Q3',
                'year': '2017',
                'actual': 0.9,
                'consensus': 0.96
            }, {
                'quarter': 'Q4',
                'year': '2017',
                'actual': 1.1,
                'consensus': 1.04
            }, {
                'quarter': 'Q1',
                'year': '2018',
                'actual': 1.1,
                'consensus': 1.1
            }],
            'dividend': {
                'amount': 0.82,
                'date': '2020-05-08',
                'yield': 0.0101,
                'sectorMedian': 0.0172,
                'marketMedian': 0.0379
            },
            'companyOutlookSummary': {
                'innovationTrend': 'trending up',
                'innovationScore': 94.0,
                'innovationPerformance': 'outperforming',
                'hiringTrend': 'decreased',
                'insiderSentiment': 'negative',
                'topSupplier': 'POSCO',
                'dividendsPerformance': 'lower'
            }
        }
    }
    ```

#### **p_corporate_events**

=== "Details"

    - *Description*:  Obtain significant corporate events related to given symbol(s)
    - *Return*:  `pandas.DataFrame`

=== "Example"

    ```python
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    df = aapl.p_corporate_events
    df.head()
    ```

=== "Data"

    |                                            |      id |   significance | headline                                                           | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | parentTopics                         |
    |:-------------------------------------------|--------:|---------------:|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
    | ('aapl', Timestamp('2011-01-17 00:00:00')) | 2064853 |              1 | Apple Inc.'s Steve Jobs Takes Second Medical Leave-Reuters         | Reuters reported that Apple Inc. Chief Executive Steve Jobs is taking medical leave for the second time in as many years, sending its shares tumbling as the unexpected news revived concerns over the long-term future of Apple. The news, which was disclosed early on a U.S. holiday when markets were closed, came nearly two years to the date after Jobs first took a six-month break to undergo a liver transplant. Unlike the previous announcement, Apple did not specify any timeline for Jobs to resume his duties. Jobs said Chief Operating Officer Tim Cook would take responsibility for day-to-day operations but he would continue to be Chief Executive and be involved in major strategic decisions. | Restructuring/Reorganization/Related |
    | ('aapl', Timestamp('2011-08-24 00:00:00')) | 2389197 |              1 | Steve Jobs Resigns as CEO of Apple Inc.; Names Tim Cook As New CEO | Apple Inc.'s Board of Directors announced that Steve Jobs has resigned as Chief Executive Officer (CEO), and the Board has named Tim Cook, previously Apple's Chief Operating Officer, as the Company's new CEO. Jobs has been elected Chairman of the Board and Cook will join the Board, effective immediately. Jobs submitted his resignation to the Board on August 24, 2011, and recommended that the Board implement its succession plan and name Tim Cook as CEO.                                                                                                                                                                                                                                                | Restructuring/Reorganization/Related |
    | ('aapl', Timestamp('2011-10-05 00:00:00')) | 2410928 |              1 | Apple Inc.'s Steve Jobs Passes Away                                | Apple Inc. announced that Steve Jobs, Chairman of the Company, passed away.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Restructuring/Reorganization/Related |
    | ('aapl', Timestamp('2011-11-15 00:00:00')) | 2435048 |              1 | Apple Inc. Names Arthur D. Levinson As Chairman Of Board           | Apple Inc. announced that it named Arthur D. Levinson, Ph. D. as the Company’s non-executive Chairman of the Board. Levinson has been a co-lead director of Apple’s board since 2005, has served on all three board committees—audit and finance, nominating and corporate governance, and compensation—and will continue to serve on the audit committee. Apple also announced that Robert A. Iger, President and Chief Executive Officer of The Walt Disney Company, will join Apple’s board and will serve on the audit committee.                                                                                                                                                                                   | Restructuring/Reorganization/Related |
    | ('aapl', Timestamp('2014-03-04 00:00:00')) | 2935872 |              2 | Apple Inc's Peter Oppenheimer to retire at the end of september    | Apple Inc:Says that Peter Oppenheimer, its senior vice president and CFO, will retire at the end of September.Luca Maestri, Apple's vice president of Finance and corporate controller, will succeed Peter as CFO.Peter will transition the CFO role to Luca in June and the balance of his responsibilities over the remaining time allowing for a professional and seamless transition.                                                                                                                                                                                                                                                                                                                               | Restructuring/Reorganization/Related |

#### **p_ideas**

!!! tip
    See [Research](../research.md)

#### **p_reports**

!!! tip
    See [Research](../research.md)

#### **p_value_analyzer_drilldown**


=== "Details"

    - *Description*:  Valuation metrics for given symbol(s)
    - *Return*:  `dict`

=== "Example"

    ```python
    aapl = Ticker('aapl', username='username@yahoo.com', password='password')
    aapl.p_value_analyzer_drilldown
    ```

=== "Data"

    ```python
    {
        'aapl': {
            'currentPrice': 425.04,
            'revenue': 260174000000.0,
            'epsGrowth': 11.02,
            'peRatio': 28.5418,
            'dps': 3.28,
            'priceBookRatio': 21.010402,
            'symbol': 'aapl',
            'valuationDescription': 'Overvalued',
            'valuationColor': 0.0,
            'outlook': '-8%',
            'currentFairValue': 146.5,
            'timeSeries': [{
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualEps': [{
                    'basicNetEps': 2.201429,
                    'yoyPercentage': 66.022039,
                    'yoyPercentageFormatted': '66.02%'
                }, {
                    'basicNetEps': 4.007143,
                    'yoyPercentage': 82.02463,
                    'yoyPercentageFormatted': '82.02%'
                }, {
                    'basicNetEps': 6.38,
                    'yoyPercentage': 59.215681,
                    'yoyPercentageFormatted': '59.22%'
                }, {
                    'basicNetEps': 5.72,
                    'yoyPercentage': -10.344828,
                    'yoyPercentageFormatted': '-10.34%'
                }, {
                    'basicNetEps': 6.49,
                    'yoyPercentage': 13.461538,
                    'yoyPercentageFormatted': '13.46%'
                }, {
                    'basicNetEps': 9.28,
                    'yoyPercentage': 42.989214,
                    'yoyPercentageFormatted': '42.99%'
                }, {
                    'basicNetEps': 8.35,
                    'yoyPercentage': -10.021552,
                    'yoyPercentageFormatted': '-10.02%'
                }, {
                    'basicNetEps': 9.27,
                    'yoyPercentage': 11.017964,
                    'yoyPercentageFormatted': '11.02%'
                }, {
                    'basicNetEps': 12.01,
                    'yoyPercentage': 29.557713,
                    'yoyPercentageFormatted': '29.56%'
                }, {
                    'basicNetEps': 11.97,
                    'yoyPercentage': -0.333056,
                    'yoyPercentageFormatted': '-0.33%'
                }],
                'type': 'annualEps'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualSharesOutstanding': [{
                    'sharesOutstanding': 6411790350
                }, {
                    'sharesOutstanding': 6504939000
                }, {
                    'sharesOutstanding': 6574456000
                }, {
                    'sharesOutstanding': 6294491000
                }, {
                    'sharesOutstanding': 5866161000
                }, {
                    'sharesOutstanding': 5578753000
                }, {
                    'sharesOutstanding': 5336166000
                }, {
                    'sharesOutstanding': 5126201000
                }, {
                    'sharesOutstanding': 4754986000
                }, {
                    'sharesOutstanding': 4443236000
                }],
                'type': 'annualSharesOutstanding'
            }, {
                'timestamp': [20200930, 20210930, 20220930, 20230930, 20240930, 20250930],
                'futureFairValue': [{
                    'fairValue': 146.5
                }, {
                    'fairValue': 162.64
                }, {
                    'fairValue': 180.56
                }, {
                    'fairValue': 200.46
                }, {
                    'fairValue': 222.55
                }, {
                    'fairValue': 247.08
                }],
                'type': 'futureFairValue'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualLogEps': [{
                    'logEarningsPerShare': 0.0
                }, {
                    'logEarningsPerShare': 0.598972
                }, {
                    'logEarningsPerShare': 1.064061
                }, {
                    'logEarningsPerShare': 0.954862
                }, {
                    'logEarningsPerShare': 1.081156
                }, {
                    'logEarningsPerShare': 1.438755
                }, {
                    'logEarningsPerShare': 1.333155
                }, {
                    'logEarningsPerShare': 1.437677
                }, {
                    'logEarningsPerShare': 1.696633
                }, {
                    'logEarningsPerShare': 1.693297
                }],
                'type': 'annualLogEps'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualPriceRange': [{
                    'priceHigh': 42.104244,
                    'priceLow': 25.81426
                }, {
                    'priceHigh': 60.408511,
                    'priceLow': 39.681389
                }, {
                    'priceHigh': 100.724185,
                    'priceLow': 50.605664
                }, {
                    'priceHigh': 96.678475,
                    'priceLow': 55.014231
                }, {
                    'priceHigh': 103.74,
                    'priceLow': 67.772932
                }, {
                    'priceHigh': 134.54,
                    'priceLow': 92.0
                }, {
                    'priceHigh': 123.82,
                    'priceLow': 89.47
                }, {
                    'priceHigh': 164.94,
                    'priceLow': 104.08
                }, {
                    'priceHigh': 229.67,
                    'priceLow': 150.24
                }, {
                    'priceHigh': 233.47,
                    'priceLow': 142.0
                }],
                'type': 'annualPriceRange'
            }, {
                'timestamp': [20140930, 20141231, 20150331, 20150630, 20150930, 20151231, 20160331, 20160630, 20160930, 20161231, 20170331, 20170630, 20170930, 20171231, 20180331, 20180630, 20180930, 20181231, 20190331, 20190630, 20190930, 20191231, 20200331],
                'quarterlyEps': [{
                    'basicNetEps': 1.43
                }, {
                    'basicNetEps': 3.08
                }, {
                    'basicNetEps': 2.34
                }, {
                    'basicNetEps': 1.86
                }, {
                    'basicNetEps': 1.97
                }, {
                    'basicNetEps': 3.3
                }, {
                    'basicNetEps': 1.91
                }, {
                    'basicNetEps': 1.43
                }, {
                    'basicNetEps': 1.68
                }, {
                    'basicNetEps': 3.38
                }, {
                    'basicNetEps': 2.11
                }, {
                    'basicNetEps': 1.68
                }, {
                    'basicNetEps': 2.08
                }, {
                    'basicNetEps': 3.92
                }, {
                    'basicNetEps': 2.75
                }, {
                    'basicNetEps': 2.36
                }, {
                    'basicNetEps': 2.94
                }, {
                    'basicNetEps': 4.22
                }, {
                    'basicNetEps': 2.47
                }, {
                    'basicNetEps': 2.2
                }, {
                    'basicNetEps': 3.05
                }, {
                    'basicNetEps': 5.04
                }, {
                    'basicNetEps': 2.58
                }],
                'type': 'quarterlyEps'
            }, {
                'timestamp': [20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualDebtToEquityRatio': [{
                    'debtToEquityRatio': 0.137273
                }, {
                    'debtToEquityRatio': 0.316414
                }, {
                    'debtToEquityRatio': 0.538964
                }, {
                    'debtToEquityRatio': 0.678617
                }, {
                    'debtToEquityRatio': 0.862981
                }, {
                    'debtToEquityRatio': 1.068467
                }, {
                    'debtToEquityRatio': 1.194048
                }],
                'type': 'annualDebtToEquityRatio'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualLogRevenue': [{
                    'logRevenue': 0.926689
                }, {
                    'logRevenue': 1.433281
                }, {
                    'logRevenue': 1.801954
                }, {
                    'logRevenue': 1.889984
                }, {
                    'logRevenue': 1.957212
                }, {
                    'logRevenue': 2.202949
                }, {
                    'logRevenue': 2.122452
                }, {
                    'logRevenue': 2.18359
                }, {
                    'logRevenue': 2.330819
                }, {
                    'logRevenue': 2.310197
                }],
                'type': 'annualLogRevenue'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualCash': [{
                    'cash': 25620000000.0,
                    'cashFormatted': '25.62B'
                }, {
                    'cash': 25952000000.0,
                    'cashFormatted': '25.95B'
                }, {
                    'cash': 29129000000.0,
                    'cashFormatted': '29.13B'
                }, {
                    'cash': 40546000000.0,
                    'cashFormatted': '40.55B'
                }, {
                    'cash': 25077000000.0,
                    'cashFormatted': '25.08B'
                }, {
                    'cash': 41601000000.0,
                    'cashFormatted': '41.60B'
                }, {
                    'cash': 67155000000.0,
                    'cashFormatted': '67.16B'
                }, {
                    'cash': 74181000000.0,
                    'cashFormatted': '74.18B'
                }, {
                    'cash': 66301000000.0,
                    'cashFormatted': '66.30B'
                }, {
                    'cash': 100557000000.0,
                    'cashFormatted': '100.56B'
                }],
                'type': 'annualCash'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualDps': [{
                    'dividendPerShare': 0.0
                }, {
                    'dividendPerShare': 0.0
                }, {
                    'dividendPerShare': 0.378571
                }, {
                    'dividendPerShare': 1.628571
                }, {
                    'dividendPerShare': 1.811429
                }, {
                    'dividendPerShare': 1.98
                }, {
                    'dividendPerShare': 2.18
                }, {
                    'dividendPerShare': 2.4
                }, {
                    'dividendPerShare': 2.72
                }, {
                    'dividendPerShare': 3.0
                }],
                'type': 'annualDps'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualFairValue': [{
                    'fairValue': 24.268181
                }, {
                    'fairValue': 44.174066
                }, {
                    'fairValue': 70.33204
                }, {
                    'fairValue': 63.056312
                }, {
                    'fairValue': 71.544661
                }, {
                    'fairValue': 102.301149
                }, {
                    'fairValue': 92.048987
                }, {
                    'fairValue': 102.190911
                }, {
                    'fairValue': 132.396207
                }, {
                    'fairValue': 131.955254
                }],
                'type': 'annualFairValue',
                'futureTimestamp': [2020, 2021, 2022, 2023, 2024],
                'futureAnnualFairValue': [{
                    'fairValue': 146.5
                }, {
                    'fairValue': 162.64
                }, {
                    'fairValue': 180.56
                }, {
                    'fairValue': 200.46
                }, {
                    'fairValue': 222.55
                }]
            }, {
                'timestamp': [20140930, 20141231, 20150331, 20150630, 20150930, 20151231, 20160331, 20160630, 20160930, 20161231, 20170331, 20170630, 20170930, 20171231, 20180331, 20180630, 20180930, 20181231, 20190331, 20190630, 20190930, 20191231, 20200331],
                'quarterlyAdjustedRevenue': [{
                    'adjustedRevenue': 2.618226
                }, {
                    'adjustedRevenue': 4.636826
                }, {
                    'adjustedRevenue': 3.881656
                }, {
                    'adjustedRevenue': 3.319248
                }, {
                    'adjustedRevenue': 3.446116
                }, {
                    'adjustedRevenue': 5.076867
                }, {
                    'adjustedRevenue': 3.885146
                }, {
                    'adjustedRevenue': 3.255078
                }, {
                    'adjustedRevenue': 3.600428
                }, {
                    'adjustedRevenue': 6.021027
                }, {
                    'adjustedRevenue': 4.06489
                }, {
                    'adjustedRevenue': 3.489461
                }, {
                    'adjustedRevenue': 4.04053
                }, {
                    'adjustedRevenue': 6.785038
                }, {
                    'adjustedRevenue': 4.698185
                }, {
                    'adjustedRevenue': 4.093247
                }, {
                    'adjustedRevenue': 4.833666
                }, {
                    'adjustedRevenue': 6.478957
                }, {
                    'adjustedRevenue': 4.458269
                }, {
                    'adjustedRevenue': 4.135052
                }, {
                    'adjustedRevenue': 4.921272
                }, {
                    'adjustedRevenue': 7.056
                }, {
                    'adjustedRevenue': 4.48117
                }],
                'type': 'quarterlyAdjustedRevenue'
            }, {
                'timestamp': [20101231, 20111231, 20121231, 20131231, 20141231, 20151231, 20161231, 20171231, 20181231, 20191231],
                'annualRevenue': [{
                    'revenue': 65225000000.0,
                    'formatted': '65.22B',
                    'yoyPercentage': 52.021909,
                    'yoyPercentageFormatted': '52.02%'
                }, {
                    'revenue': 108249000000.0,
                    'formatted': '108.25B',
                    'yoyPercentage': 65.962438,
                    'yoyPercentageFormatted': '65.96%'
                }, {
                    'revenue': 156508000000.0,
                    'formatted': '156.51B',
                    'yoyPercentage': 44.581474,
                    'yoyPercentageFormatted': '44.58%'
                }, {
                    'revenue': 170910000000.0,
                    'formatted': '170.91B',
                    'yoyPercentage': 9.202086,
                    'yoyPercentageFormatted': '9.20%'
                }, {
                    'revenue': 182795000000.0,
                    'formatted': '182.79B',
                    'yoyPercentage': 6.953952,
                    'yoyPercentageFormatted': '6.95%'
                }, {
                    'revenue': 233715000000.0,
                    'formatted': '233.72B',
                    'yoyPercentage': 27.856342,
                    'yoyPercentageFormatted': '27.86%'
                }, {
                    'revenue': 215639000000.0,
                    'formatted': '215.64B',
                    'yoyPercentage': -7.734206,
                    'yoyPercentageFormatted': '-7.73%'
                }, {
                    'revenue': 229234000000.0,
                    'formatted': '229.23B',
                    'yoyPercentage': 6.304518,
                    'yoyPercentageFormatted': '6.30%'
                }, {
                    'revenue': 265595000000.0,
                    'formatted': '265.60B',
                    'yoyPercentage': 15.861958,
                    'yoyPercentageFormatted': '15.86%'
                }, {
                    'revenue': 260174000000.0,
                    'formatted': '260.17B',
                    'yoyPercentage': -2.041078,
                    'yoyPercentageFormatted': '-2.04%'
                }],
                'type': 'annualRevenue'
            }]
        }
    }
    ```
