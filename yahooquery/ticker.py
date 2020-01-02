from datetime import datetime
import pandas as pd

from .base import _YahooBase
from yahooquery.utils import _convert_to_timestamp


class Ticker(_YahooBase):
    """
    Base class for interacting with Yahoo Finance API

    Attributes
    ----------
    symbols: str or list
        Symbol or list collection of symbols
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
        self.formatted = kwargs.get('formatted', True)
        self.endpoints = []
        self._expiration_dates = {}
        self._url_key = 'base'
        super(Ticker, self).__init__(**kwargs)

    @property
    def _base_urls(self):
        return ["{}/v10/finance/quoteSummary/{}".format(
            self._BASE_API_URL, symbol) for symbol in self.symbols]

    @property
    def _options_urls(self):
        return ["{}/v7/finance/options/{}".format(
            self._BASE_API_URL, symbol) for symbol in self.symbols]

    @property
    def _chart_urls(self):
        return ["{}/v8/finance/chart/{}".format(
            self._CHART_API_URL, symbol) for symbol in self.symbols]

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
            except IndexError:
                data[self.symbols[i]] = "No data found for symbol {}".format(
                    self.symbols[i])
        return data

    def _to_dataframe(self, endpoint=None, params={}, **kwargs):
        data = self._get_endpoint(endpoint, params, **kwargs)
        dataframes = []
        try:
            for symbol in self.symbols:
                final_data = data[symbol][kwargs.get('data_filter')] if \
                    kwargs.get('data_filter') else data[symbol]
                if kwargs.get('from_dict', False):
                    df = pd.DataFrame(
                        [(k, v) for d in final_data for k, v in d.items()])
                    df.set_index(0, inplace=True)
                    df.columns = [symbol]
                else:
                    df = pd.DataFrame(final_data)
                dataframes.append(df)
            if kwargs.get('from_dict', False):
                return pd.concat(dataframes, axis=1)
            return pd.concat(
                dataframes, keys=self.symbols, names=['symbol', 'row'],
                sort=False)
        except TypeError:
            return data

    def get_multiple_endpoints(self, endpoints, **kwargs):
        if not isinstance(endpoints, list):
            raise ValueError("A list is expected.  {} is not a list.".format(
                endpoints))
        if any(elem not in self._ENDPOINTS for elem in endpoints):
            raise ValueError("""
                One of {} is not a valid value.
                Valid values are {})""".format(
                    ', '.join(endpoints),
                    ', '.join(self._ENDPOINTS)
                ))
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
        return self._get_endpoint("esgScores")

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
            try:
                data[symbol] = data[symbol]["bondHoldings"]
            except TypeError:
                pass
        return data

    @property
    def fund_equity_holdings(self):
        data = self.fund_holding_info
        for symbol in self.symbols:
            try:
                data[symbol] = data[symbol]["equityHoldings"]
            except TypeError:
                pass
        return data

    # OPTIONS

    def _get_options(self):
        data = self._get_endpoint(
            url_key='options', formatted=False)
        for symbol in self.symbols:
            self._expiration_dates[symbol] = []
            try:
                for exp_date in data[symbol]['expirationDates']:
                    self._expiration_dates[symbol].append(
                        {datetime.fromtimestamp(exp_date).strftime('%Y-%m-%d'):
                         exp_date})
            except TypeError:
                # No data
                pass

    def _options_to_dataframe(self, options, symbol):
        calls = pd.DataFrame(options['calls'])
        puts = pd.DataFrame(options['puts'])
        d = {v: k for d in self._expiration_dates[symbol]
             for k, v in d.items()}
        for dataframe in [calls, puts]:
            dataframe.replace({'expiration': d})
            try:
                dataframe['lastTradeDate'] = pd.to_datetime(
                    dataframe['lastTradeDate'], unit='s')
            except KeyError:
                pass
        return pd.concat([calls, puts], keys=['calls', 'puts'], sort=False)

    @property
    def option_chain(self):
        all_dataframes = []
        symbols = []
        if not self._expiration_dates:
            self._get_options()
        for symbol in self.symbols:
            symbol_dataframes = []
            for date in self._expiration_dates[symbol]:
                json = self._get_endpoint(
                    url_key='options', params={'date': list(date.values())[0]},
                    formatted=False)
                options = json[symbol]['options'][0]
                symbol_dataframes.append(
                    self._options_to_dataframe(options, symbol))
            try:
                all_dataframes.append(pd.concat(symbol_dataframes, keys=[
                    datetime.strptime(k, "%Y-%m-%d")
                    for d in self._expiration_dates[symbol]
                    for k, v in d.items()], names=[
                        'expiration_date', 'option_type', 'row'], sort=False))
                symbols.append(symbol)
            except ValueError:
                # No data was found for symbol
                pass
        if all_dataframes:
            return pd.concat(
                all_dataframes, keys=symbols, names=[
                    'symbol', 'expiration_date', 'option_type',
                    'row'], sort=False)
        return {symbol: 'No option data found'
                for symbol in self.symbols if symbol not in symbols}

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
                df.set_index('dates', inplace=True)
                d[symbol] = df
            else:
                d[symbol] = data[symbol]
        if all(isinstance(d[key], pd.DataFrame) for key in d):
            if len(d) == 1:
                return d[self.symbols[0]]
            else:
                return pd.concat(
                    list(d.values()), keys=list(d.keys()),
                    names=['symbol', 'dates'], sort=False)
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
        """
        data = self._get_historical_data(
            period, interval, start, end, **kwargs)
        df = self._historical_data_to_dataframe(data, **kwargs)
        return df
