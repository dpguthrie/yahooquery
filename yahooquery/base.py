import os
import time
from concurrent.futures import as_completed
from datetime import datetime

from requests_futures.sessions import FuturesSession

from yahooquery.login import YahooSelenium
from yahooquery.utils import _convert_to_list, _init_session
from yahooquery.utils.countries import COUNTRIES

try:
    from urllib import parse
except ImportError:
    import urlparse as parse


class _YahooFinance(object):

    FUNDAMENTALS_OPTIONS = {
        'income_statement': [
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
            'TotalUnusualItemsExcludingGoodwill', 'WriteOff'],
        'balance_sheet': [
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
            'WorkInProcess', 'WorkingCapital'],
        'cash_flow': [
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
            'BeginningCashPosition'],
        'valuation': [
            'ForwardPeRatio', 'PsRatio', 'PbRatio',
            'EnterprisesValueEBITDARatio', 'EnterprisesValueRevenueRatio',
            'PeRatio', 'MarketCap', 'EnterpriseValue', 'PegRatio'],
    }

    CORPORATE_EVENTS = [
        'sigdev_corporate_guidance', 'sigdev_performance',
        'sigdev_corporate_deals', 'sigdev_expansion_new_markets_new_units',
        'sigdev_products', 'sigdev_ownership_control', 'sigdev_financing',
        'sigdev_litigation_regulatory', 'sigdev_accounting_issues',
        'sigdev_restructuring_reorganization_related', 'sigdev_reference',
        'sigdev_special_events', 'sigdev_environment']

    FUNDAMENTALS_TIME_ARGS = {
        'a': {
            'prefix': 'annual',
            'period_type': '12M'
        },
        'q': {
            'prefix': 'quarterly',
            'period_type': '3M'
        },
        'm': {
            'prefix': 'monthly',
            'period_type': '1M'
        }
    }

    _MODULES_DICT = {
        'assetProfile': {
            'convert_dates': [
                'governanceEpochDate', 'compensationAsOfEpochDate']},
        'balanceSheetHistory': {
            'filter': 'balanceSheetStatements', 'convert_dates': ['endDate']},
        'balanceSheetHistoryQuarterly': {
            'filter': 'balanceSheetStatements', 'convert_dates': ['endDate']},
        'calendarEvents': {
            'convert_dates': [
                'earningsDate', 'exDividendDate', 'dividendDate']},
        'cashflowStatementHistory': {
            'filter': 'cashflowStatements', 'convert_dates': ['endDate']},
        'cashflowStatementHistoryQuarterly': {
            'filter': 'cashflowStatements', 'convert_dates': ['endDate']},
        'defaultKeyStatistics': {
            'convert_dates': [
                'sharesShortPreviousMonthDate', 'dateShortInterest',
                'lastFiscalYearEnd', 'nextFiscalYearEnd', 'fundInceptionDate',
                'lastSplitDate', 'mostRecentQuarter']},
        'earnings': {'convert_dates': ['earningsDate']},
        'earningsHistory': {
            'filter': 'history', 'convert_dates': ['quarter']},
        'earningsTrend': {'convert_dates': []},
        'esgScores': {'convert_dates': []},
        'financialData': {'convert_dates': []},
        'fundOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate']},
        'fundPerformance': {'convert_dates': ['asOfDate']},
        'fundProfile': {'convert_dates': []},
        'indexTrend': {'convert_dates': []},
        'incomeStatementHistory': {
            'filter': 'incomeStatementHistory', 'convert_dates': ['endDate']},
        'incomeStatementHistoryQuarterly': {
            'filter': 'incomeStatementHistory', 'convert_dates': ['endDate']},
        'industryTrend': {'convert_dates': []},
        'insiderHolders': {
            'filter': 'holders', 'convert_dates':
            ['latestTransDate', 'positionDirectDate']},
        'insiderTransactions': {
            'filter': 'transactions', 'convert_dates': ['startDate']},
        'institutionOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate']},
        'majorHoldersBreakdown': {'convert_dates': []},
        'pageViews': {'convert_dates': []},
        'price': {'convert_dates': ['preMarketTime', 'regularMarketTime']},
        'quoteType': {'convert_dates': ['firstTradeDateEpochUtc']},
        'recommendationTrend': {'filter': 'trend', 'convert_dates': []},
        'secFilings': {'filter': 'filings', 'convert_dates': ['epochDate']},
        'netSharePurchaseActivity': {'convert_dates': []},
        'sectorTrend': {'convert_dates': []},
        'summaryDetail': {
            'convert_dates': ['exDividendDate', 'expireDate', 'startDate']},
        'summaryProfile': {'convert_dates': []},
        'topHoldings': {'convert_dates': []},
        'upgradeDowngradeHistory': {
            'filter': 'history', 'convert_dates': ['epochGradeDate']}
    }

    _FUND_DETAILS = [
        'holdings', 'equityHoldings', 'bondHoldings', 'bondRatings',
        'sectorWeightings']

    _STYLE_BOX = {
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq1.gif':
            ('Large Cap Stocks', 'Value'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq2.gif':
            ('Large Cap Stocks', 'Blend'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq3.gif':
            ('Large Cap Stocks', 'Growth'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq4.gif':
            ('Mid Cap Stocks', 'Value'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq5.gif':
            ('Mid Cap Stocks', 'Blend'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq6.gif':
            ('Mid Cap Stocks', 'Growth'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq7.gif':
            ('Small Cap Stocks', 'Value'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq8.gif':
            ('Small Cap Stocks', 'Blend'),
        'http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq9.gif':
            ('Small Cap Stocks', 'Growth')
    }

    _CONFIG = {
        'news': {
            'path': 'https://query2.finance.yahoo.com/v2/finance/news',
            'response_field': 'Content',
            'query': {
                'start': {'required': False, 'default': None},
                'count': {'required': False, 'default': None},
                'symbols': {'required': True, 'default': None},
                'sizeLabels': {'required': False, 'default': None},
                'widths': {'required': False, 'default': None},
                'tags': {'required': False, 'default': None},
                'filterOldVideos': {'required': False, 'default': None},
                'category': {'required': False, 'default': None}
            }
        },
        'quoteSummary': {
            'path': 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}',
            'response_field': 'quoteSummary',
            'query': {
                'formatted': {'required': False, 'default': False},
                'modules': {'required': True, 'default': None,
                            'options': list(_MODULES_DICT.keys())},
            }
        },
        'fundamentals': {
            'path': 'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{symbol}',
            'response_field': 'timeseries',
            'query': {
                'period1': {'required': True, 'default': 493590046},
                'period2': {'required': True, 'default': int(time.time())},
                'type': {'required': True, 'default': None,
                         'options': FUNDAMENTALS_OPTIONS},
                'merge': {'required': False, 'default': False},
                'padTimeSeries': {'required': False, 'default': False}
            }
        },
        'fundamentals_premium': {
            'path': 'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/{symbol}',
            'response_field': 'timeseries',
            'query': {
                'period1': {'required': True, 'default': 493590046},
                'period2': {'required': True, 'default': int(time.time())},
                'type': {'required': True, 'default': None,
                         'options': FUNDAMENTALS_OPTIONS},
                'merge': {'required': False, 'default': False},
                'padTimeSeries': {'required': False, 'default': False}
            }
        },
        'chart': {
            'path': 'https://query2.finance.yahoo.com/v8/finance/chart/{symbol}',
            'response_field': 'chart',
            'query': {
                'period1': {'required': False, 'default': None},
                'period2': {'required': False, 'default': None},
                'interval': {'required': False, 'default': None, 'options': [
                    '1m', '2m', '5m', '15m',
                    '30m', '60m', '90m', '1h',
                    '1d', '5d', '1wk', '1mo', '3mo'
                ]},
                'range': {'required': False, 'default': None, 'options': [
                    '1d', '5d', '7d', '60d', '1mo', '3mo',
                    '6mo', '1y', '2y', '5y',
                    '10y', 'ytd', 'max'
                ]},
                'events': {'required': False, 'default': 'div,split'},
                'numberOfPoints': {'required': False, 'default': None},
                'formatted': {'required': False, 'default': False}
            }
        },
        'options': {
            'path': 'https://query2.finance.yahoo.com/v7/finance/options/{symbol}',
            'response_field': 'optionChain',
            'query': {
                'formatted': {'required': False, 'default': False},
                'date': {'required': False, 'default': None},
                'endDate': {'required': False, 'default': None},
                'size': {'required': False, 'default': None},
                'strikeMin': {'required': False, 'default': None},
                'strikeMax': {'required': False, 'default': None},
                'straddle': {'required': False, 'default': None},
                'getAllData': {'required': False, 'default': None}
            }
        },
        'validation': {
            'path': 'https://query2.finance.yahoo.com/v6/finance/quote/validate',
            'response_field': 'symbolsValidation',
            'query': {
                'symbols': {'required': True, 'default': None}
            }
        },
        'esg_chart': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/esgChart',
            'responseField': 'esgChart',
            'query': {
                'symbol': {'required': True, 'default': None}
            }
        },
        'esg_peer_scores': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/esgPeerScores',
            'responseField': 'esgPeerScores',
            'query': {
                'symbol': {'required': True, 'default': None}
            }
        },
        'recommendations': {
            'path': 'https://query2.finance.yahoo.com/v6/finance/recommendationsbysymbol/{symbol}',
            'response_field': 'finance',
            'query': {}
        },
        'insights': {
            'path': 'https://query2.finance.yahoo.com/ws/insights/v2/finance/insights',
            'response_field': 'finance',
            'query': {
                'symbol': {'required': True, 'default': None},
                'reportsCount': {'required': False, 'default': None}
            }
        },
        'premium_insights': {
            'path': 'https://query2.finance.yahoo.com/ws/insights/v2/finance/premium/insights',
            'response_field': 'finance',
            'query': {
                'symbol': {'required': True, 'default': None},
                'reportsCount': {'required': False, 'default': None}
            }
        },
        'screener': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/screener/predefined/saved',
            'response_field': 'finance',
            'query': {
                'formatted': {'required': False, 'default': False},
                'scrIds': {'required': True, 'default': None},
                'count': {'required': False, 'default': 25},
            }
        },
        'company360': {
            'path': 'https://query2.finance.yahoo.com/ws/finance-company-360/v1/finance/premium/company360',
            'response_field': 'finance',
            'premium': True,
            'query': {
                'symbol': {'required': True, 'default': None},
                'modules': {'required': True, 'default': ','.join([
                    'innovations', 'sustainability', 'insiderSentiments',
                    'significantDevelopments', 'supplyChain', 'earnings',
                    'dividend', 'companyOutlookSummary', 'hiring',
                    'companySnapshot'
                ])}

            }
        },
        'premium_portal': {
            'path': 'https://query2.finance.yahoo.com/ws/portal/v1/finance/premium/portal',
            'response_field': 'finance',
            'query': {
                'symbols': {'required': True, 'default': None},
                'modules': {'required': False, 'default': None},
                'quotefields': {'required': False, 'default': None}
            }
        },
        'trade_ideas': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/premium/tradeideas/overlay',
            'response_field': 'tradeIdeasOverlay',
            'query': {
                'ideaId': {'required': True, 'default': None}
            }
        },
        'visualization': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/visualization',
            'response_field': 'finance',
            'query': {
                'crumb': {'required': True, 'default': None}
            }
        },
        'research': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/premium/visualization',
            'response_field': 'finance',
            'query': {
                'crumb': {'required': True, 'default': None}
            }
        },
        'reports': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/premium/researchreports/overlay',
            'response_field': 'researchReportsOverlay',
            'query': {
                'reportId': {'required': True, 'default': None}
            }
        },
        'value_analyzer': {
            'path': 'https://query2.finance.yahoo.com/ws/value-analyzer/v1/finance/premium/valueAnalyzer/portal',
            'response_field': 'finance',
            'query': {
                'symbols': {'required': True, 'default': None},
                'formatted': {'required': False, 'default': False}
            }
        },
        'value_analyzer_drilldown': {
            'path': 'https://query2.finance.yahoo.com/ws/value-analyzer/v1/finance/premium/valueAnalyzer',
            'response_field': 'finance',
            'query': {
                'symbol': {'required': True, 'default': None},
                'formatted': {'required': False, 'default': False},
                'start': {'required': False, 'default': None},
                'end': {'required': False, 'default': None}
            }
        },
        'technical_events': {
            'path': 'https://query2.finance.yahoo.com/ws/finance-technical-events/v1/finance/premium/technicalevents',
            'response_field': 'technicalEvents',
            'query': {
                'symbol': {'required': True, 'default': None},
                'formatted': {'required': False, 'default': False},
                'tradingHorizons': {'required': False, 'default': None},
                'size': {'required': False, 'default': None}
            }
        },
        'quotes': {
            'path': 'https://query2.finance.yahoo.com/v6/finance/quote',
            'response_field': 'quoteResponse',
            'query': {
                'symbols': {'required': True, 'default': None}
            }
        },
        'search': {
            'path': 'https://query2.finance.yahoo.com/v1/finance/search',
            'response_field': 'quotes',
            'query': {
                'q': {'required': True, 'default': None},
                'quotesCount': {'required': False, 'default': None},
                'newsCount': {'required': False, 'default': None}
            }
        }
    }

    PERIODS = _CONFIG['chart']['query']['range']['options']
    INTERVALS = _CONFIG['chart']['query']['interval']['options']
    MODULES = _CONFIG['quoteSummary']['query']['modules']['options']

    def __init__(self, **kwargs):
        self.country = kwargs.get('country', 'united states').lower()
        self.formatted = kwargs.pop('formatted', False)
        self.session = _init_session(kwargs.pop('session', None), **kwargs)
        self.crumb = kwargs.pop('crumb', None)
        username = os.getenv("YF_USERNAME") or kwargs.get('username')
        password = os.getenv("YF_PASSWORD") or kwargs.get('password')
        if username and password:
            self.login(username, password)

    @property
    def symbols(self):
        """
        List of symbol(s) used to retrieve information
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = _convert_to_list(symbols)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country.lower() not in COUNTRIES:
            raise ValueError(
                "{} is not a valid country.  Valid countries include {}".format(
                    country, ', '.join(COUNTRIES.keys())
                ))
        self._country = country.lower()
        self._default_query_params = COUNTRIES[self._country]

    @property
    def default_query_params(self):
        """
        Dictionary containing default query parameters that are sent with
        each request.  The dictionary contains three keys:  lang, region, and
        corsDomain.

        Notes
        -----
        The query parameters will default to
        {'lang': 'en-US', 'region': 'US', 'corsDomain': 'finance.yahoo.com'}

        To change the default query parameters, set the country property equal
        to a valid country.
        """
        return self._default_query_params

    def login(self, username, password):
        ys = YahooSelenium(username=username, password=password)
        d = ys.yahoo_login()
        try:
            [self.session.cookies.set(c['name'], c['value'])
             for c in d['cookies']]
            self.crumb = d['crumb']
            self.userId = d['userId']
        except TypeError:
            print('Invalid credentials provided.  Please check username and'
                  ' password and try again')

    @property
    def validation(self):
        """Symbol Validation

        Validate existence of given symbol(s) and modify the symbols property
        to include only the valid symbols.  If invalid symbols were passed,
        they will be stored in the `invalid_symbols` property.
        """
        current_symbols = self.symbols
        valid_symbols = []
        invalid_symbols = []
        for i in range(0, len(current_symbols), 1500):
            self._symbols = current_symbols[i:i+1500]
            data = self._get_data('validation')
            if 'error' in data:
                self._symbols = current_symbols
                return data
            if None in data:
                data = data[None]
            valid_symbols.extend([k for k, v in data.items() if v])
            invalid_symbols.extend([k for k, v in data.items() if not v])
        self.symbols = valid_symbols
        self.invalid_symbols = invalid_symbols or None

    # @property
    # def _get_crumb(self):
    #     r = requests.get("https://finance.yahoo.com/screener/new")
    #     crumbs = re.findall('"crumb":"(.+?)"', r.text)
    #     crumb = crumbs[-1].replace('\\u002F', '/')
    #     if not crumb:
    #         return 'Unable to retrieve crumb.  Try again'
    #     return crumb

    def _format_data(self, obj, dates):
        for k, v in obj.items():
            if k in dates:
                if isinstance(v, dict):
                    obj[k] = v.get('fmt', v)
                elif isinstance(v, list):
                    try:
                        obj[k] = [item.get('fmt') for item in v]
                    except AttributeError:
                        obj[k] = v
                else:
                    try:
                        obj[k] = datetime.fromtimestamp(
                            v).strftime('%Y-%m-%d %H:%M:%S')
                    except (TypeError, OSError):
                        obj[k] = v
            elif isinstance(v, dict):
                if 'raw' in v:
                    obj[k] = v.get('raw')
                elif 'min' in v:
                    obj[k] = v
                else:
                    obj[k] = self._format_data(v, dates)
            elif isinstance(v, list):
                if len(v) == 0:
                    obj[k] = v
                elif isinstance(v[0], dict):
                    for i, list_item in enumerate(v):
                        obj[k][i] = self._format_data(list_item, dates)
                else:
                    obj[k] = v
            else:
                obj[k] = v
        return obj

    def _get_data(self, key, params={}, **kwargs):
        config = self._CONFIG[key]
        params = self._construct_params(config, params)
        urls = self._construct_urls(config, params, **kwargs)
        response_field = config['response_field']
        try:
            if isinstance(self.session, FuturesSession):
                data = self._async_requests(
                    response_field, urls, params, **kwargs)
            else:
                data = self._sync_requests(
                    response_field, urls, params, **kwargs)
            return data
        except ValueError:
            return {'error': 'HTTP 404 Not Found.  Please try again'}

    def _construct_params(self, config, params):
        required_params = [
            k for k in config['query']
            if config['query'][k]['required'] and 'symbol' not in k]
        for required in required_params:
            if not params.get(required):
                params.update(
                    {required: getattr(
                        self, required, config['query'][required]['default'])})
        optional_params = [
            k for k in config['query'] if not config['query'][k]['required']
            and config['query'][k]['default'] is not None
        ]
        for optional in optional_params:
            params.update({optional: getattr(
                self, optional, config['query'][optional]['default']
            )})
        params.update(self._default_query_params)
        params = {
            k: str(v).lower() if v is True or v is False else v
            for k, v in params.items()
        }
        if 'symbol' in config['query']:
            return [dict(params, symbol=symbol) for symbol in self._symbols]
        return params

    def _construct_urls(self, config, params, **kwargs):
        if 'symbol' in config['query']:
            urls = [self.session.get(
                url=config['path'], params=p) for p in params]
        elif 'symbols' in config['query']:
            params.update({'symbols': ','.join(self._symbols)})
            urls = [self.session.get(url=config['path'], params=params)]
        else:
            urls = [self.session.get(url=config['path'].format(
                **{'symbol': symbol}), params=params)
                for symbol in self._symbols]
        return urls

    def _async_requests(self, response_field, urls, params, **kwargs):
        data = {}
        for future in as_completed(urls):
            response = future.result()
            json = self._validate_response(response.json(), response_field)
            symbol = self._get_symbol(response, params)
            data[symbol] = self._construct_data(json, response_field, **kwargs)
        return data

    def _sync_requests(self, response_field, urls, params, **kwargs):
        data = {}
        for response in urls:
            json = self._validate_response(response.json(), response_field)
            symbol = self._get_symbol(response, params)
            if symbol is not None:
                data[symbol] = \
                    self._construct_data(json, response_field, **kwargs)
            else:
                data = self._construct_data(json, response_field, **kwargs)
        return data

    def _validate_response(self, response, response_field):
        try:
            if response[response_field]['error']:
                error = response[response_field]['error']
                return error.get('description')
            if not response[response_field]['result']:
                return 'No data found'
            return response
        except KeyError:
            if 'finance' in response:
                if response['finance'].get('error'):
                    return response['finance']['error']['description']
                return response
            return {response_field: {'result': [response]}}

    def _get_symbol(self, response, params):
        if isinstance(params, list):
            query_params = dict(
                parse.parse_qsl(parse.urlsplit(response.url).query))
            return query_params['symbol']
        if 'symbols' in params:
            return None
        return parse.unquote(response.url.rsplit('/')[-1].split('?')[0])

    def _construct_data(self, json, response_field, **kwargs):
        try:
            addl_key = kwargs.get('addl_key')
            if addl_key:
                data = json[response_field]['result'][0][addl_key]
            elif kwargs.get('list_result', False):
                data = json[response_field]['result']
            else:
                data = json[response_field]['result'][0]
        except KeyError:
            data = json[response_field]['result'][addl_key] \
                if addl_key else json[response_field]['result']
        except TypeError:
            data = json
        return data
