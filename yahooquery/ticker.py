from datetime import datetime
import pandas as pd

from .base import _YahooBase


class Ticker(_YahooBase):

    _ENDPOINTS = [
        'assetProfile', 'incomeStatementHistory',
        'balanceSheetHistory', 'cashflowStatementHistory', 'financialData'
        'defaultKeyStatistics', 'calendarEvents', 'secFilings',
        'recommendationTrend', 'upgradeDowngradeHistory',
        'institutionOwnership', 'fundOwnership', 'majorDirectHolders',
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

    _CHART_BASE_URL = 'https://query1.finance.yahoo.com/'

    def __init__(self, symbols=None, **kwargs):
        self.symbols = symbols
        self.endpoints = []
        self._expiration_dates = {}
        self.period = kwargs.get('period', 'ytd')
        self.interval = kwargs.get('interval', '1d')
        super(Ticker, self).__init__(**kwargs)

    @property
    def url(self):
        if isinstance(self.symbols, list):
            return [f"v10/finance/quoteSummary/{symbol}" for symbol in self.symbols]
        else:
            return f'v10/finance/quoteSummary/{self.symbols}'

    @property
    def _options_url(self):
        if isinstance(self.symbols, list):
            return [f'v7/finance/options/{symbol}' for symbol in self.symbols]
        else:
            return f'v7/finance/options/{self.symbols}'

    @property
    def _chart_url(self):
        if isinstance(self.symbols, list):
            return [f'v8/finance/chart/{symbol}' for symbol in self.symbols]
        else:
            return f'v8/finance/chart/{self.symbols}'

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
    def _get_endpoint(self, endpoint, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = [endpoint]
        if isinstance(self.url, list):
            data = {}
            for i, url in enumerate(self.url):
                json = self.fetch(new_url=url, **kwargs)
                data[self.symbols[i]] = \
                    json['quoteSummary']['result'][0][endpoint]
        else:
            json = self.fetch(**kwargs)
            data = json['quoteSummary']['result'][0][endpoint]
        return data

    def _list_to_dataframe(
            self, endpoint, key, date_fields=['reportDate'],
            drop_cols=['maxAge']):
        data = self._get_endpoint(endpoint)
        df = pd.DataFrame(data[key])
        for date in date_fields:
            try:
                df[date] = df[date].apply(lambda x: x.get('fmt'))
            except AttributeError:
                df[date] = pd.to_datetime(df[date], unit='s')
        df = df.applymap(lambda x: x.get('raw') if isinstance(x, dict) else x)
        if drop_cols:
            df.drop(drop_cols, axis=1, inplace=True)
        return df

    def _retrieve_relevant_data(self, endpoint, exclude_cols=[], convert_dates=[]):
        data = self._get_endpoint(endpoint)
        if isinstance(self.url, list):
            for symbol in self.symbols:
                for k, v in data[symbol].items():
                    if v:
                        if k.lower() in [x.lower() for x in convert_dates]:
                            if isinstance(v, dict):
                                data[symbol][k] = v.get('fmt', v)
                            else:
                                data[symbol][k] = datetime.fromtimestamp(v).strftime('%Y-%m-%d')
                        else:
                            if isinstance(v, dict):
                                data[symbol][k] = v.get('raw', v)
                [data[symbol].pop(k) for k in exclude_cols]
        else:
            for k, v in data.items():
                if v:
                    if k.lower() in [x.lower() for x in convert_dates]:
                        if isinstance(v, dict):
                            data[k] = v.get('fmt', v)
                        else:
                            data[k] = datetime.fromtimestamp(v).strftime('%Y-%m-%d')
                    else:
                        if isinstance(v, dict):
                            data[k] = v.get('raw', v)
            [data.pop(k) for k in exclude_cols]
        return data

    # RETURN DICTIONARY
    @property
    def asset_profile(self):
        return self._retrieve_relevant_data(
            "assetProfile", ['maxAge'], convert_dates=[
                'governanceEpochDate', 'compensationAsOfEpochDate'])

    @property
    def esg_scores(self):
        return self._retrieve_relevant_data("esgScores", ['maxAge'])

    @property
    def financial_data(self):
        return self._retrieve_relevant_data("financialData", ['maxAge'])

    @property
    def fund_profile(self):
        return self._retrieve_relevant_data("fundProfile", ['maxAge'])

    @property
    def key_stats(self):
        return self._retrieve_relevant_data(
            "defaultKeyStatistics", ['maxAge'], convert_dates=[
                'sharesShortPreviousMonthDate', 'dateShortInterest',
                'lastFiscalYearEnd', 'nextFiscalYearEnd', 'fundInceptionDate',
                'lastSplitDate', 'mostRecentQuarter'])

    @property
    def price(self):
        return self._retrieve_relevant_data("price", ['maxAge'])

    @property
    def quote_type(self):
        return self._retrieve_relevant_data(
            "quoteType", ['maxAge'], convert_dates=['firstTradeDateEpochUtc'])

    @property
    def share_purchase_activity(self):
        return self._retrieve_relevant_data(
            "netSharePurchaseActivity", ['maxAge'])

    @property
    def summary_detail(self):
        return self._retrieve_relevant_data(
            "summaryDetail", ['maxAge'],
            convert_dates=['exDividendDate', 'expireDate', 'startDate'])

    @property
    def summary_profile(self):
        return self._retrieve_relevant_data("summaryProfile", ['maxAge'])

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
    def earnings_history(self):
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
        data = self._get_endpoint("majorHoldersBreakdown")
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.applymap(lambda x: x.get('raw') if isinstance(x, dict) else x)
        df.drop(['maxAge'], inplace=True)
        return df

    @property
    def earnings_trend(self):
        raise NotImplementedError()
        # return self._list_to_dataframe(
        #     endpoint="earningsTrend", key="trend", date_fields=[])

    # FUND SPECIFIC

    def _fund_dataframe(self, endpoint, key):
        data = self._get_endpoint(endpoint)[key]
        ls = []
        for item in data:
            for k, v in item.items():
                ls.append([k, v.get('raw')])
        return pd.DataFrame(ls, columns=['label', 'value'])

    @property
    def fund_category_holdings(self):
        data_dict = self._retrieve_relevant_data("topHoldings", ['maxAge'])
        for key in ["holdings", "bondRatings", "sectorWeightings"]:
            del data_dict[key]
        return pd.DataFrame.from_dict(data_dict, orient='index')

    @property
    def fund_top_holdings(self):
        return self._fund_dataframe(endpoint="topHoldings", key="holdings")

    @property
    def fund_bond_ratings(self):
        return self._fund_dataframe(endpoint="topHoldings", key="bondRatings")

    @property
    def fund_sector_weightings(self):
        return self._fund_dataframe(
            endpoint="topHoldings", key="sectorWeightings")

    # OPTIONS

    def _get_options(self):
        new_url = self._options_url
        json = self.fetch(new_url=new_url, other_params=())
        for exp_date in json['optionChain']['result'][0]['expirationDates']:
            self._expiration_dates[
                datetime.fromtimestamp(exp_date).strftime('%Y-%m-%d')] = \
                    exp_date

    def _options_to_dataframe(self, df, options):
        calls = pd.DataFrame(options['calls'])
        calls['optionType'] = 'call'
        puts = pd.DataFrame(options['puts'])
        puts['optionType'] = 'put'
        for df in [calls, puts]:
            df['expiration'] = df['expiration'].map(
                {v: k for k, v in self._expiration_dates.items()})
            df['lastTradeDate'] = pd.to_datetime(df['lastTradeDate'], unit='s')
        return df.append([calls, puts])

    def option_chain(self, expiration_date=None):
        new_url = self._options_url
        df = pd.DataFrame()
        if not self._expiration_dates:
            self._get_options()
        if not expiration_date:
            for date in self._expiration_dates.values():
                json = self.fetch(new_url=new_url, other_params={'date': date})
                options = json['optionChain']['result'][0]['options'][0]
                df = df.append(
                    self._options_to_dataframe(df, options), sort=False)
        elif expiration_date not in self._expiration_dates.keys():
            raise ValueError(f"""
                {expiration_date} is not a valid value.  Valid expiration
                dates are {', '.join(self.option_expiration_dates)}
            """)
        else:
            json = self.fetch(new_url=new_url, other_params={
                'date': self._expiration_dates[expiration_date]})
            options = json['optionChain']['result'][0]['options'][0]
            df = self._options_to_dataframe(df, options)
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
        new_base_url = self._CHART_BASE_URL
        new_url = self._chart_url
        if period not in self._PERIODS:
            raise ValueError("Period values must be one of {}".format(
                ', '.join(self._PERIODS)))
        if interval not in self._INTERVALS:
            raise ValueError("Interval values must be one of {}".format(
                ', '.join(self._INTERVALS)))
        data = self.fetch(
            new_base_url=new_base_url, new_url=new_url,
            other_params={**other_params, **self._chart_params})
        return data['chart']['result'][0]

    def _historical_data_to_dataframe(self, data):
        dates = [datetime.fromtimestamp(x) for x in data['timestamp']]
        df = pd.DataFrame(data['indicators']['quote'][0])
        df['dates'] = dates
        df.set_index('dates', inplace=True)
        return df

    def history(self, **kwargs):
        data = self._get_historical_data(**kwargs)
        df = self._historical_data_to_dataframe(data)
        return df
