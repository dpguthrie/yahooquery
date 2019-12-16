from datetime import datetime
import pandas as pd

from .base import _YahooBase


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
        self.endpoints = []
        self._expiration_dates = {}
        self.period = kwargs.get('period', 'ytd')
        self.interval = kwargs.get('interval', '1d')
        self.combine_dataframes = kwargs.get('combine_dataframes', True)
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
            'base': self._base_urls,
            'options': self._options_urls,
            'chart': self._chart_urls
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

    # HELPER METHODS
    def _get_endpoint(self, endpoint=None, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = [endpoint]
        data = {}
        for i, url in enumerate(
                self._urls_dict[kwargs.pop('url_key', 'base')]):
            json = self.fetch(url, **kwargs)
            try:
                data[self.symbols[i]] = \
                    json['quoteSummary']['result'][0][endpoint]
            except KeyError:
                try:
                    data[self.symbols[i]] = \
                        json['chart']['result'][0]
                except KeyError:
                    data[self.symbols[i]] = \
                        json['optionChain']['result'][0]
            except TypeError:
                data[self.symbols[i]] = json
        return data

    def _get_endpoints(self, endpoints=[], params={}, **kwargs):
        self.optional_params = params
        self.endpoints = endpoints
        data = {}
        for i, url in enumerate(
                self._urls_dict[kwargs.pop('url_key', 'base')]):
            json = self.fetch(url, **kwargs)
            for endpoint in endpoints:
                data[self.symbols[i]][endpoint] = \
                    json['quoteSummary']['result'][0][endpoint]
        return data

    def _list_to_dataframe(
            self, endpoint, key, date_fields=['reportDate'],
            drop_cols=['maxAge'], combine_dataframes=True):
        data = self._get_endpoint(endpoint)
        df = pd.DataFrame()
        for symbol in self.symbols:
            temp_df = pd.DataFrame(data[symbol][key])
            for date in date_fields:
                try:
                    temp_df[date] = temp_df[date].apply(lambda x: x.get('fmt'))
                except AttributeError:
                    temp_df[date] = pd.to_datetime(temp_df[date], unit='s')
            temp_df = temp_df.applymap(
                lambda x:  x.get('raw') if isinstance(x, dict) else x)
            if drop_cols:
                temp_df.drop(drop_cols, axis=1, inplace=True)
            temp_df['ticker'] = symbol.upper()
            df = df.append(temp_df)
        return df

    def _retrieve_relevant_data(
            self, endpoint, exclude_cols=[], convert_dates=[], key=None):
        data = self._get_endpoint(endpoint)
        for symbol in self.symbols:
            try:
                iterator = data[symbol][key] if key else data[symbol]
                for k, v in iterator.items():
                    if v:
                        if k.lower() in [x.lower() for x in convert_dates]:
                            if isinstance(v, dict):
                                data[symbol][k] = v.get('fmt', v)
                            else:
                                data[symbol][k] = \
                                    datetime.fromtimestamp(v).strftime(
                                        '%Y-%m-%d')
                        else:
                            if isinstance(v, dict):
                                data[symbol][k] = v.get('raw', v)
                [data[symbol].pop(k) for k in exclude_cols]
            except AttributeError:
                pass
        if key:
            new_data = {}
            for symbol in self.symbols:
                new_data[symbol] = data[symbol][key]
            return new_data
        return data

    def _expiration_date_list(self, symbol):
        return [[(k, v) for k, v in d.items()]
                for d in self._expiration_dates[symbol]]

    # RETURN DICTIONARY
    @property
    def asset_profile(self):
        return self._retrieve_relevant_data(
            "assetProfile", ['maxAge'], convert_dates=[
                'governanceEpochDate', 'compensationAsOfEpochDate'])

    @property
    def esg_scores(self):
        return self._retrieve_relevant_data(
            "esgScores", exclude_cols=['maxAge'])

    @property
    def financial_data(self):
        return self._retrieve_relevant_data(
            "financialData", exclude_cols=['maxAge'])

    @property
    def fund_profile(self):
        return self._retrieve_relevant_data(
            "fundProfile", exclude_cols=['maxAge'])

    @property
    def key_stats(self):
        return self._retrieve_relevant_data(
            "defaultKeyStatistics", ['maxAge'], convert_dates=[
                'sharesShortPreviousMonthDate', 'dateShortInterest',
                'lastFiscalYearEnd', 'nextFiscalYearEnd', 'fundInceptionDate',
                'lastSplitDate', 'mostRecentQuarter'])

    @property
    def price(self):
        return self._retrieve_relevant_data("price", exclude_cols=['maxAge'])

    @property
    def quote_type(self):
        return self._retrieve_relevant_data(
            "quoteType", exclude_cols=['maxAge'],
            convert_dates=['firstTradeDateEpochUtc'])

    @property
    def share_purchase_activity(self):
        return self._retrieve_relevant_data(
            "netSharePurchaseActivity", exclude_cols=['maxAge'])

    @property
    def summary_detail(self):
        return self._retrieve_relevant_data(
            "summaryDetail", exclude_cols=['maxAge'],
            convert_dates=['exDividendDate', 'expireDate', 'startDate'])

    @property
    def summary_profile(self):
        return self._retrieve_relevant_data(
            "summaryProfile", exclude_cols=['maxAge'])

    # RETURN DATAFRAMES
    @property
    def balance_sheet(self):
        return self._list_to_dataframe(
            endpoint="balanceSheetHistory", key="balanceSheetStatements",
            date_fields=["endDate"])

    @property
    def cash_flow(self):
        return self._list_to_dataframe(
            endpoint="cashflowStatementHistory", key="cashflowStatements",
            date_fields=["endDate"])

    @property
    def company_officers(self):
        return self._list_to_dataframe(
            endpoint="assetProfile", key="companyOfficers", date_fields=[])

    @property
    def earning_history(self):
        return self._list_to_dataframe(
            endpoint="earningsHistory", key="history", date_fields=['quarter'])

    @property
    def grading_history(self):
        return self._list_to_dataframe(
            endpoint="upgradeDowngradeHistory", key="history",
            date_fields=["epochGradeDate"], drop_cols=[])

    @property
    def income_statement(self):
        return self._list_to_dataframe(
            endpoint="incomeStatementHistory", key="incomeStatementHistory",
            date_fields=["endDate"])

    @property
    def insider_holders(self):
        return self._list_to_dataframe(
            endpoint="insiderHolders", key="holders",
            date_fields=['latestTransDate', 'positionDirectDate'])

    @property
    def insider_transactions(self):
        return self._list_to_dataframe(
            endpoint="insiderTransactions", key="transactions",
            date_fields=['startDate'])

    @property
    def institution_ownership(self):
        return self._list_to_dataframe(
            endpoint="institutionOwnership", key="ownershipList")

    @property
    def recommendation_trend(self):
        return self._list_to_dataframe(
            endpoint="recommendationTrend", key="trend", date_fields=[],
            drop_cols=[])

    @property
    def sec_filings(self):
        return self._list_to_dataframe(
            endpoint="secFilings", key="filings", date_fields=[],
            drop_cols=["maxAge", "epochDate"])

    @property
    def fund_ownership(self):
        return self._list_to_dataframe(
            endpoint="fundOwnership", key="ownershipList")

    @property
    def major_holders(self):
        dataframes = []
        data = self._get_endpoint("majorHoldersBreakdown")
        for symbol in self.symbols:
            df = pd.DataFrame.from_dict(
                data[symbol], orient='index', columns=[symbol])
            df = df.applymap(
                lambda x: x.get('raw') if isinstance(x, dict) else x)
            df.drop(['maxAge'], inplace=True)
            dataframes.append(df)
        return pd.concat(dataframes, axis=1)

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
        data_dict = self._retrieve_relevant_data("topHoldings", ['maxAge'])
        for symbol in self.symbols:
            for key in self._FUND_DETAILS:
                del data_dict[symbol][key]
        return pd.DataFrame(
            [pd.Series(data_dict[symbol]) for symbol in self.symbols],
            index=self.symbols)

    @property
    def fund_top_holdings(self):
        return self._fund_dataframe(endpoint="topHoldings", key="holdings")

    @property
    def fund_bond_ratings(self):
        return self._fund_dataframe_concat(
            endpoint="topHoldings", key="bondRatings")

    @property
    def fund_sector_weightings(self):
        return self._fund_dataframe_concat(
            endpoint="topHoldings", key="sectorWeightings")

    @property
    def fund_bond_holdings(self):
        return self._retrieve_relevant_data(
            endpoint="topHoldings", key="bondHoldings")

    @property
    def fund_equity_holdings(self):
        return self._retrieve_relevant_data(
            endpoint="topHoldings", key="equityHoldings")

    # OPTIONS

    def _get_options(self):
        data = self._get_endpoint(url_key='options', other_params=())
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
                    url_key='options', other_params={'date': date[0][1]})
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
                **other_params, **self._chart_params})
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
