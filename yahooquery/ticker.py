from datetime import datetime
import pandas as pd
from collections import ChainMap

from .base import _YahooBase
from yahooquery.utils.format import _Format


class Ticker(_YahooBase):

    _ENDPOINTS = [
        'assetProfile', 'incomeStatementHistory',
        'balanceSheetHistory', 'cashflowStatementHistory', 'financialData'
        'defaultKeyStatistics', 'calendarEvents', 'secFilings',
        'recommendationTrend', 'upgradeDowngradeHistory',
        'institutionOwnership', 'fundOwnership',
        'majorHoldersBreakdown', 'insiderTransactions', 'insiderHolders',
        'netSharePurchaseActivity', 'earnings', 'earningsHistory',
        'earningsTrend', 'industryTrend', 'indexTrend', 'sectorTrend',
        'summaryDetail', 'price', 'quoteType', 'summaryProfile', 'fundProfile',
        'fundPerformance', 'topHoldings', 'esgScores'
    ]

    _ENDPOINT_DICT = {
        'assetProfile': {
            'exclude_cols': ['maxAge'], 'convert_dates': [
                'governanceEpochDate', 'compensationAsOfEpochDate']},
        'balanceSheetHistory': {
            'filter': 'balanceSheetStatements', 'convert_dates': ['endDate'],
            'exclude_cols': ['maxAge']},
        'cashflowStatementHistory': {
            'filter': 'cashflowStatements', 'convert_dates': ['endDate'],
            'exclude_cols': ['maxAge']},
        'defaultKeyStatistics': {
            'exclude_cols': ['maxAge'], 'convert_dates': [
                'sharesShortPreviousMonthDate', 'dateShortInterest',
                'lastFiscalYearEnd', 'nextFiscalYearEnd', 'fundInceptionDate',
                'lastSplitDate', 'mostRecentQuarter']},
        'earningsHistory': {
            'filter': 'history', 'convert_dates': ['quarter'],
            'exclude_cols': ['maxAge']},
        'esgScores': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'financialData': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'fundOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate'],
            'exclude_cols': []},
        'fundProfile': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'incomeStatementHistory': {
            'filter': 'incomeStatementHistory', 'convert_dates': ['endDate'],
            'exclude_cols': []},
        'insiderHolders': {
            'filter': 'holders', 'convert_dates':
            ['latestTransDate', 'positionDirectDate'],
            'exclude_cols': ['maxAge']},
        'insiderTransactions': {
            'filter': 'transactions', 'convert_dates': ['startDate'],
            'exclude_cols': ['maxAge']},
        'institutionOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate'],
            'exclude_cols': ['maxAge']},
        'majorHoldersBreakdown': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'price': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'quoteType': {
            'exclude_cols': ['maxAge'],
            'convert_dates': ['firstTradeDateEpochUtc']},
        'recommendationTrend': {
            'filter': 'trend', 'convert_dates': [], 'exclude_cols': []},
        'secFilings': {
            'filter': 'filings', 'convert_dates': ['epochDate'],
            'exclude_cols': ['maxAge']},
        'netSharePurchaseActivity': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'summaryDetail': {
            'exclude_cols': ['maxAge'],
            'convert_dates': ['exDividendDate', 'expireDate', 'startDate']},
        'summaryProfile': {
            'exclude_cols': ['maxAge'], 'convert_dates': []},
        'topHoldings': {
            'exclude_cols': [], 'convert_dates': []},
        'upgradeDowngradeHistory': {
            'filter': 'history', 'convert_dates': ['quarter'],
            'exclude_cols': []}
    }

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

    _FUND_DETAILS = [
        'holdings', 'equityHoldings', 'bondHoldings', 'bondRatings',
        'sectorWeightings']

    _INTERVALS = [
        '1m', '2m', '5m', '15m',
        '30m', '60m', '90m', '1h',
        '1d', '5d', '1wk', '1mo', '3mo'
    ]

    _PERIODS = [
        '1d', '5d', '1mo', '3mo',
        '6mo', '1y', '2y', '5y',
        '10y', 'ytd', 'max'
    ]

    def __init__(self, symbols=None, **kwargs):
        self.symbols = symbols if isinstance(symbols, list) else [symbols]
        self.period = kwargs.get('period', 'ytd')
        self.interval = kwargs.get('interval', '1d')
        self.combine_dataframes = kwargs.get('combine_dataframes', True)
        self.formatted = kwargs.get('formatted', True)
        self.endpoints = []
        self._expiration_dates = {}
        super(Ticker, self).__init__(**kwargs)

    @property
    def _base_urls(self):
        return [f"{self._YAHOO_API_URL}/v10/finance/quoteSummary/{symbol}"
                for symbol in self.symbols]

    @property
    def _options_urls(self):
        return [f'{self._YAHOO_API_URL}/v7/finance/options/{symbol}'
                for symbol in self.symbols]

    @property
    def _chart_urls(self):
        return [f'{self._CHART_API_URL}/v8/finance/chart/{symbol}'
                for symbol in self.symbols]

    @property
    def _urls_dict(self):
        return {
            'base': {'urls': self._base_urls, 'key': 'quoteSummary'},
            'options': {'urls': self._options_urls, 'key': 'optionChain'},
            'chart': {'urls': self._chart_urls, 'key': 'chart'}
        }

    @property
    def params(self):
        temp = {"modules": ','.join(self.endpoints)}
        temp.update(self.optional_params)
        params = {k: str(v) if v is True or v is False else str(v)
                  for k, v in temp.items()}
        return params

    @property
    def _chart_params(self):
        return {"events": ','.join(['div', 'split'])}

    def _get_endpoint(self, endpoint=None, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = endpoint if isinstance(endpoint, list) else [endpoint]
        formatted = kwargs.get('formatted', self.formatted)
        data = {}
        url_key = kwargs.pop('url_key', 'base')
        for i, url in enumerate(self._urls_dict[url_key]['urls']):
            json = self.fetch(url, **kwargs)
            try:
                d = json[self._urls_dict[url_key]['key']]['result'][0]
                data[self.symbols[i]] = \
                    _Format(d, self).format if formatted else d
            except TypeError:
                data[self.symbols[i]] = json
        return data

    def _to_dataframe(self, endpoint=None, params={}, **kwargs):
        data = self._get_endpoint(endpoint, params, **kwargs)
        dataframes = []
        try:
            for symbol in self.symbols:
                if kwargs.get('from_dict', False):
                    if kwargs.get('data_filter'):
                        df = pd.DataFrame.from_dict(ChainMap(
                            *data[symbol][kwargs.get('data_filter')]),
                            orient='index', columns=[symbol])
                    else:
                        df = pd.DataFrame.from_dict(
                            ChainMap(*data[symbol]), orient='index',
                            columns=[symbol])
                else:
                    if kwargs.get('data_filter'):
                        df = pd.DataFrame(
                            data[symbol][kwargs.get('data_filter')])
                    else:
                        df = pd.DataFrame(data[symbol])
                    df['ticker'] = symbol.upper()
                dataframes.append(df)
            if kwargs.get('from_dict', False):
                return pd.concat(dataframes, axis=1)
            return pd.concat(dataframes, ignore_index=True)
        except TypeError:
            return data

    def _expiration_date_list(self, symbol):
        return [[(k, v) for k, v in d.items()]
                for d in self._expiration_dates[symbol]]

    def get_multiple_endpoints(self, endpoints, **kwargs):
        if not isinstance(endpoints, list):
            raise ValueError(f"""
                A list is expected.  {endpoints} is not a list.""")
        elif any(elem not in self._ENDPOINTS for elem in endpoints):
            raise ValueError(f"""
                One of {', '.join(endpoints)} is not a valid value.
                Valid values are {', '.join(self._ENDPOINTS)})""")
        else:
            return self._get_endpoint(endpoints, **kwargs)

    # RETURN DICTIONARY
    @property
    def asset_profile(self):
        return self._get_endpoint("assetProfile")

    @property
    def esg_scores(self):
        return self._get_endpoint("esgScores", from_dict=True)

    @property
    def financial_data(self):
        return self._get_endpoint("financialData")

    @property
    def fund_profile(self):
        return self._get_endpoint("fundProfile")

    @property
    def key_stats(self):
        return self._get_endpoint("defaultKeyStatistics")

    @property
    def major_holders(self):
        return self._get_endpoint("majorHoldersBreakdown")

    @property
    def price(self):
        return self._get_endpoint("price")

    @property
    def quote_type(self):
        return self._get_endpoint("quoteType")

    @property
    def share_purchase_activity(self):
        return self._get_endpoint("netSharePurchaseActivity")

    @property
    def summary_detail(self):
        return self._get_endpoint("summaryDetail")

    @property
    def summary_profile(self):
        return self._get_endpoint("summaryProfile")

    # RETURN DATAFRAMES
    @property
    def balance_sheet(self):
        return self._to_dataframe(
            "balanceSheetHistory", data_filter="balanceSheetStatements")

    @property
    def cash_flow(self):
        return self._to_dataframe(
            "cashflowStatementHistory", data_filter="cashflowStatements")

    @property
    def company_officers(self):
        return self._to_dataframe(
            "assetProfile", data_filter="companyOfficers")

    @property
    def earning_history(self):
        return self._to_dataframe("earningsHistory", data_filter="history")

    @property
    def fund_ownership(self):
        return self._to_dataframe("fundOwnership", data_filter="ownershipList")

    @property
    def grading_history(self):
        return self._to_dataframe(
            "upgradeDowngradeHistory", data_filter="history")

    @property
    def income_statement(self):
        return self._to_dataframe(
            "incomeStatementHistory", data_filter="incomeStatementHistory")

    @property
    def insider_holders(self):
        return self._to_dataframe("insiderHolders", data_filter="holders")

    @property
    def insider_transactions(self):
        return self._to_dataframe(
            "insiderTransactions", data_filter="transactions")

    @property
    def institution_ownership(self):
        return self._to_dataframe(
            "institutionOwnership", data_filter="ownershipList")

    @property
    def recommendation_trend(self):
        return self._to_dataframe("recommendationTrend", data_filter="trend")

    @property
    def sec_filings(self):
        return self._to_dataframe("secFilings", data_filter="filings")

    @property
    def earnings_trend(self):
        raise NotImplementedError()
        # return self._list_to_dataframe(
        #     endpoint="earningsTrend", key="trend", date_fields=[])

    # FUND SPECIFIC

    def _fund_dataframe(self, endpoint, key):
        data = self._get_endpoint(endpoint)
        df = pd.DataFrame()
        for symbol in self.symbols:
            temp_df = pd.DataFrame(data[symbol][key])
            temp_df['ticker'] = symbol.upper()
            df = df.append(temp_df)
        df = df.applymap(lambda x:  x.get('raw') if isinstance(x, dict) else x)
        return df

    def _fund_dataframe_concat(self, endpoint, key):
        data = self._get_endpoint(endpoint)
        dataframes = []
        for symbol in self.symbols:
            d = {}
            for item in data[symbol][key]:
                for k, v in item.items():
                    d[k] = v.get('raw')
            df = pd.DataFrame.from_dict(d, orient='index', columns=[symbol])
            dataframes.append(df)
        return pd.concat(dataframes, axis=1, sort=False)

    @property
    def fund_category_holdings(self):
        data_dict = self._get_endpoint("topHoldings")
        for symbol in self.symbols:
            for key in self._FUND_DETAILS:
                del data_dict[symbol][key]
        return pd.DataFrame(
            [pd.Series(data_dict[symbol]) for symbol in self.symbols],
            index=self.symbols)

    @property
    def fund_holding_info(self):
        return self._get_endpoint("topHoldings")

    @property
    def fund_top_holdings(self):
        return self._to_dataframe("topHoldings", data_filter="holdings")

    @property
    def fund_bond_ratings(self):
        return self._to_dataframe(
            "topHoldings", data_filter="bondRatings", from_dict=True)

    @property
    def fund_sector_weightings(self):
        return self._to_dataframe(
            "topHoldings", data_filter="sectorWeightings", from_dict=True)

    @property
    def fund_bond_holdings(self):
        data = self.fund_holding_info
        for symbol in self.symbols:
            data[symbol] = data[symbol]["bondHoldings"]
        return data

    @property
    def fund_equity_holdings(self):
        data = self.fund_holding_info
        for symbol in self.symbols:
            data[symbol] = data[symbol]["equityHoldings"]
        return data

    # OPTIONS

    def _get_options(self):
        data = self._get_endpoint(
            url_key='options', other_params=(), formatted=False)
        for symbol in self.symbols:
            self._expiration_dates[symbol] = []
            for exp_date in data[symbol]['expirationDates']:
                self._expiration_dates[symbol].append(
                    {datetime.fromtimestamp(exp_date).strftime('%Y-%m-%d'):
                     exp_date})

    def _options_to_dataframe(self, df, options, symbol, expiration_dates):
        calls = pd.DataFrame(options['calls'])
        calls['optionType'] = 'call'
        calls['ticker'] = symbol.upper()
        puts = pd.DataFrame(options['puts'])
        puts['optionType'] = 'put'
        puts['ticker'] = symbol.upper()
        d = {}
        for item in expiration_dates:
            d[item[0][0][0]] = item[0][0][1]
        for df in [calls, puts]:
            df['expiration'] = df['expiration'].map(
                {v: k for k, v in d.items()})
            df['lastTradeDate'] = pd.to_datetime(df['lastTradeDate'], unit='s')
        return df.append([calls, puts])

    @property
    def option_chain(self):
        df = pd.DataFrame()
        if not self._expiration_dates:
            self._get_options()
        for symbol in self.symbols:
            expiration_dates = self._expiration_date_list(symbol)
            for date in expiration_dates:
                json = self._get_endpoint(
                    url_key='options', other_params={'date': date[0][1]},
                    formatted=False)
                options = json[symbol]['options'][0]
                df = df.append(
                    self._options_to_dataframe(
                        df, options, symbol, expiration_dates),
                    sort=False)
        return df

    @property
    def option_expiration_dates(self):
        if not self._expiration_dates:
            self._get_options()
        return list(self._expiration_dates.keys())

    # HISTORICAL PRICE DATA

    def _get_historical_data(self, **kwargs):
        period = kwargs.get('period', self.period)
        interval = kwargs.get('interval', self.interval)
        other_params = {'range': period, 'interval': interval}
        if period not in self._PERIODS:
            raise ValueError("Period values must be one of {}".format(
                ', '.join(self._PERIODS)))
        if interval not in self._INTERVALS:
            raise ValueError("Interval values must be one of {}".format(
                ', '.join(self._INTERVALS)))
        data = self._get_endpoint(
            url_key='chart', other_params={
                **other_params, **self._chart_params}, formatted=False)
        return data

    def _historical_data_to_dataframe(self, data, **kwargs):
        d = {}
        for symbol in self.symbols:
            if isinstance(data[symbol], dict):
                dates = [datetime.fromtimestamp(x)
                         for x in data[symbol]['timestamp']]
                df = pd.DataFrame(data[symbol]['indicators']['quote'][0])
                df['dates'] = dates
                df['ticker'] = symbol.upper()
                df.set_index('dates', inplace=True)
                d[symbol] = df
            else:
                d[symbol] = data[symbol]
        if kwargs.get('combine_dataframes', self.combine_dataframes):
            ls = []
            for key in d:
                if isinstance(d[key], pd.DataFrame):
                    ls.append(d[key])
            return pd.concat(ls, sort=False)
        return d

    def history(self, **kwargs):
        data = self._get_historical_data(**kwargs)
        df = self._historical_data_to_dataframe(data, **kwargs)
        return df
