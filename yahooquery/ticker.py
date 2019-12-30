from datetime import datetime
import pandas as pd
from collections import ChainMap

from .base import _YahooBase
from yahooquery.utils import _convert_to_timestamp


class Ticker(_YahooBase):
    """
    Base class for interacting with Yahoo Finance API

    Attributes
    ----------
    symbols: str or list
        Symbol or list collection of symbols
    combine_dataframes: bool, default True, optional
        Desired pandas output format for multiple symbols
    formatted: bool, default True, optional
        Format output priot to returning data
    """

    _ENDPOINTS = [
        'assetProfile', 'incomeStatementHistory',
        'incomeStatementHistoryQuarterly',
        'balanceSheetHistory', 'balanceSheetHistoryQuarterly',
        'cashflowStatementHistory', 'cashFlowStatementHistoryQuarterly',
        'financialData', 'defaultKeyStatistics', 'calendarEvents',
        'secFilings', 'recommendationTrend', 'upgradeDowngradeHistory',
        'institutionOwnership', 'fundOwnership',
        'majorHoldersBreakdown', 'insiderTransactions', 'insiderHolders',
        'netSharePurchaseActivity', 'earnings', 'earningsHistory',
        'earningsTrend', 'industryTrend', 'indexTrend', 'sectorTrend',
        'summaryDetail', 'price', 'quoteType', 'summaryProfile', 'fundProfile',
        'fundPerformance', 'topHoldings', 'esgScores'
    ]

    _ENDPOINT_DICT = {
        'assetProfile': {
            'convert_dates': [
                'governanceEpochDate', 'compensationAsOfEpochDate']},
        'balanceSheetHistory': {
            'filter': 'balanceSheetStatements', 'convert_dates': ['endDate']},
        'balanceSheetHistoryQuarterly': {
            'filter': 'balanceSheetStatements', 'convert_dates': ['endDate']},
        'calendarEvents': {
            'convert_dates': ['earningsDate', 'exDividendDate, dividendDate']},
        'cashflowStatementHistory': {
            'filter': 'cashflowStatements', 'convert_dates': ['endDate']},
        'cashflowStatementHistoryQuarterly': {
            'filter': 'cashflowStatements', 'convert_dates': ['endDate']},
        'defaultKeyStatistics': {
            'convert_dates': [
                'sharesShortPreviousMonthDate', 'dateShortInterest',
                'lastFiscalYearEnd', 'nextFiscalYearEnd', 'fundInceptionDate',
                'lastSplitDate', 'mostRecentQuarter']},
        'earningsHistory': {
            'filter': 'history', 'convert_dates': ['quarter']},
        'esgScores': {'convert_dates': []},
        'financialData': {'convert_dates': []},
        'fundOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate']},
        'fundPerformance': {'convert_dates': ['asOfDate']},
        'fundProfile': {'convert_dates': []},
        'incomeStatementHistory': {
            'filter': 'incomeStatementHistory', 'convert_dates': ['endDate']},
        'incomeStatementHistoryQuarterly': {
            'filter': 'incomeStatementHistory', 'convert_dates': ['endDate']},
        'insiderHolders': {
            'filter': 'holders', 'convert_dates':
            ['latestTransDate', 'positionDirectDate']},
        'insiderTransactions': {
            'filter': 'transactions', 'convert_dates': ['startDate']},
        'institutionOwnership': {
            'filter': 'ownershipList', 'convert_dates': ['reportDate']},
        'majorHoldersBreakdown': {'convert_dates': []},
        'price': {'convert_dates': []},
        'quoteType': {'convert_dates': ['firstTradeDateEpochUtc']},
        'recommendationTrend': {'filter': 'trend', 'convert_dates': []},
        'secFilings': {'filter': 'filings', 'convert_dates': ['epochDate']},
        'netSharePurchaseActivity': {'convert_dates': []},
        'summaryDetail': {
            'convert_dates': ['exDividendDate', 'expireDate', 'startDate']},
        'summaryProfile': {'convert_dates': []},
        'topHoldings': {'convert_dates': []},
        'upgradeDowngradeHistory': {
            'filter': 'history', 'convert_dates': ['quarter']}
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

    def __init__(self, symbols, **kwargs):
        """Initialize class

        Parameters
        ----------
        symbols: str or list
            Symbol or list collection of symbols
        """
        self.symbols = symbols if isinstance(symbols, list) else [symbols]
        self.combine_dataframes = kwargs.get('combine_dataframes', True)
        self.formatted = kwargs.get('formatted', True)
        self.endpoints = []
        self._expiration_dates = {}
        self._url_key = 'base'
        super(Ticker, self).__init__(**kwargs)

    @property
    def _base_urls(self):
        return [f"{self._BASE_API_URL}/v10/finance/quoteSummary/{symbol}"
                for symbol in self.symbols]

    @property
    def _options_urls(self):
        return [f'{self._BASE_API_URL}/v7/finance/options/{symbol}'
                for symbol in self.symbols]

    @property
    def _chart_urls(self):
        return [f'{self._CHART_API_URL}/v8/finance/chart/{symbol}'
                for symbol in self.symbols]

    @property
    def _base_params(self):
        if self.endpoints[0]:
            return {'modules': ','.join(self.endpoints)}
        return {}

    @property
    def _chart_params(self):
        return {"events": ','.join(['div', 'split'])}

    @property
    def _options_params(self):
        return {}

    @property
    def params(self):
        temp = self._urls_dict[self._url_key]['params']
        temp.update(self.optional_params)
        params = {k: str(v) if v is True or v is False else str(v)
                  for k, v in temp.items()}
        return params

    @property
    def _urls_dict(self):
        return {
            'base': {
                'urls': self._base_urls, 'key': 'quoteSummary',
                'params': self._base_params},
            'options': {
                'urls': self._options_urls, 'key': 'optionChain',
                'params': self._options_params},
            'chart': {
                'urls': self._chart_urls, 'key': 'chart',
                'params': self._chart_params}
        }

    @property
    def _convert_dates(self):
        dates = []
        for endpoint in self.endpoints:
            dates.extend([date for date
                         in self._ENDPOINT_DICT[endpoint]['convert_dates']])
        return dates

    def _format_data(self, obj):
        for k, v in obj.items():
            if k in self._convert_dates:
                if isinstance(v, dict):
                    obj[k] = v.get('fmt', v)
                else:
                    obj[k] = datetime.fromtimestamp(v).strftime('%Y-%m-%d')
            elif isinstance(v, dict):
                if 'raw' in v:
                    obj[k] = v.get('raw')
                elif 'min' in v:
                    obj[k] = v
                else:
                    obj[k] = self._format_data(v)
            elif isinstance(v, list):
                if len(v) == 0:
                    obj[k] = v
                elif isinstance(v[0], dict):
                    for i, list_item in enumerate(v):
                        obj[k][i] = self._format_data(list_item)
                else:
                    obj[k] = v
            else:
                obj[k] = v
        return obj

    def _get_endpoint(self, endpoint=None, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = endpoint if isinstance(endpoint, list) else [endpoint]
        formatted = kwargs.get('formatted', self.formatted)
        data = {}
        self._url_key = kwargs.pop('url_key', 'base')
        for i, url in enumerate(self._urls_dict[self._url_key]['urls']):
            json = self.fetch(url, **kwargs)
            try:
                d = json[self._urls_dict[self._url_key]['key']]['result'][0]
                if len(self.endpoints) > 1 or self.endpoints[0] is None:
                    data[self.symbols[i]] = \
                        self._format_data(d) if formatted else d
                else:
                    data[self.symbols[i]] = \
                        self._format_data(d[endpoint]) if formatted \
                        else d[endpoint]
                # data[self.symbols[i]] = \
                #     _Format(d, self).format if formatted else d
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
        if any(elem not in self._ENDPOINTS for elem in endpoints):
            raise ValueError(f"""
                One of {', '.join(endpoints)} is not a valid value.
                Valid values are {', '.join(self._ENDPOINTS)})""")
        return self._get_endpoint(endpoints, **kwargs)

    # RETURN DICTIONARY
    @property
    def asset_profile(self):
        return self._get_endpoint("assetProfile")

    @property
    def calendar_events(self):
        return self._get_endpoint("calendarEvents")

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
    def _financials(self, endpoint, data_filter, frequency):
        if frequency.lower() == "q":
            endpoint += "Quarterly"
        return self._to_dataframe(endpoint, data_filter=data_filter)

    def balance_sheet(self, frequency="A"):
        return self._financials(
            "balanceSheetHistory", "balanceSheetStatements", frequency)

    def cash_flow(self, frequency="A"):
        return self._financials(
            "cashflowStatementHistory", "cashflowStatements", frequency)

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

    def income_statement(self, frequency="A"):
        return self._financials(
            "incomeStatementHistory", "incomeStatementHistory", frequency)

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

    @property
    def fund_performance(self):
        return self._get_endpoint("fundPerformance")

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
                try:
                    del data_dict[symbol][key]
                except TypeError:
                    return data_dict
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
            url_key='options', formatted=False)
        for symbol in self.symbols:
            self._expiration_dates[symbol] = []
            for exp_date in data[symbol]['expirationDates']:
                self._expiration_dates[symbol].append(
                    {datetime.fromtimestamp(exp_date).strftime('%Y-%m-%d'):
                     exp_date})

    def _options_to_dataframe(self, df, options, symbol, expiration_dates):
        calls = pd.DataFrame(options['calls'])
        calls['optionType'] = 'CALL'
        calls['ticker'] = symbol.upper()
        puts = pd.DataFrame(options['puts'])
        puts['optionType'] = 'PUT'
        puts['ticker'] = symbol.upper()
        d = {}
        for item in expiration_dates:
            d[item[0][0][0]] = item[0][0][1]
        for dataframe in [calls, puts]:
            dataframe['expiration'] = dataframe['expiration'].map(
                {v: k for k, v in d.items()})
            dataframe['lastTradeDate'] = pd.to_datetime(
                dataframe['lastTradeDate'], unit='s')
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
                    url_key='options', params={'date': date[0][1]},
                    formatted=False)
                options = json[symbol]['options'][0]
                df = df.append(
                    self._options_to_dataframe(
                        df, options, symbol, expiration_dates))
        return df

    @property
    def option_expiration_dates(self):
        """List of option expiration dates
        """
        if not self._expiration_dates:
            self._get_options()
        return list(self._expiration_dates.keys())

    # HISTORICAL PRICE DATA

    def _get_historical_data(self, period, interval, start, end, **kwargs):
        if start or period is None or period.lower() == 'max':
            start = _convert_to_timestamp(start)
            end = _convert_to_timestamp(end, start=False)
            params = {'period1': start, 'period2': end}
        else:
            period = period.lower()
            if period not in self._PERIODS:
                raise ValueError("Period values must be one of {}".format(
                    ', '.join(self._PERIODS)))
            params = {'range': period}
        if interval not in self._INTERVALS:
            raise ValueError("Interval values must be one of {}".format(
                ', '.join(self._INTERVALS)))
        params['interval'] = interval.lower()
        data = self._get_endpoint(
            url_key='chart', params=params, formatted=False)
        return data

    def _historical_data_to_dataframe(self, data, **kwargs):
        d = {}
        for symbol in self.symbols:
            if 'timestamp' in data[symbol]:
                dates = [datetime.fromtimestamp(x)
                         for x in data[symbol]['timestamp']]
                df = pd.DataFrame(data[symbol]['indicators']['quote'][0])
                df['dates'] = dates
                df['ticker'] = symbol.upper()
                df.set_index('dates', inplace=True)
                d[symbol] = df
            else:
                d[symbol] = data[symbol]
        if kwargs.get('combine_dataframes', self.combine_dataframes) and \
                all(isinstance(d[key], pd.DataFrame) for key in d):
            dataframes = []
            for key in d:
                if isinstance(d[key], pd.DataFrame):
                    dataframes.append(d[key])
            return pd.concat(dataframes, sort=False)
        return d

    def history(
            self, period='ytd', interval='1d', start=None, end=None, **kwargs):
        """
        Historical pricing data

        Pulls historical data for a symbol or symbols and returns
        a pandas.DataFrame

        Parameters
        ----------
        period: str, default ytd, optional
            Length of time
        interval: str, default 1d, optional
            Time between data points
        start: str or datetime.datetime, default None, optional
            Specify a starting point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object
        end: str of datetime.datetime, default None, optional
            Specify a ending point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object.

        Keyword Arguments
        -----------------
        combine_dataframes: bool, default True, optional
            When multiple symbols are present, specify if you'd like the
            resulting dataframes to be combined.  The ticker column will
            be added to identify rows.
        """
        data = self._get_historical_data(
            period, interval, start, end, **kwargs)
        df = self._historical_data_to_dataframe(data, **kwargs)
        return df
