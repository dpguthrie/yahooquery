from datetime import datetime
import pandas as pd
import re
import urllib.parse

from yahooquery.utils import (
    _convert_to_list, _convert_to_timestamp, _history_dataframe)
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


class Ticker(object):
    """
    Base class for interacting with Yahoo Finance API

    Attributes
    ----------
    symbols: str or list
        Symbol or list collection of symbols
    formatted: bool, default True, optional
        Format output prior to returning data.

    Notes
    -----
    When formatted is set to False, all base endpoints will return as
    dictionaries.  There are two reasons for this:

    1. Quantitative values are expressed as dictionaries.  For example:

       "totalPay": {
           "raw": 115554666,
           "fmt": "11.56M",
           "longFmt": "11,555,466"
       }

       When formatted is set to True, the _format_data method will return
       the value in the "raw" key.

    2. Dates are either expressed as timestamps:

       "governanceEpochDate": 1570147200

       Or as dictionaries:

        "exDividendDate": {
            "raw": 1573084800,
            "fmt": "2019-11-07"
        }

        When formatted is set to True, the _format_data method will return the
        date expressed in the format YYYY-MM-DD by either converting from the
        timestamp or retrieving the "fmt" key.
    """
    _BASE_API_URL = "https://query2.finance.yahoo.com"

    _CHART_API_URL = "https://query1.finance.yahoo.com"

    ENDPOINTS = [
        'assetProfile', 'incomeStatementHistory',
        'incomeStatementHistoryQuarterly',
        'balanceSheetHistory', 'balanceSheetHistoryQuarterly',
        'cashflowStatementHistory', 'cashflowStatementHistoryQuarterly',
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
        'price': {'convert_dates': []},
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

    INTERVALS = [
        '1m', '2m', '5m', '15m',
        '30m', '60m', '90m', '1h',
        '1d', '5d', '1wk', '1mo', '3mo'
    ]

    PERIODS = [
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
        self.session = FuturesSession(max_workers=kwargs.get('max_workers', 8))
        if kwargs.get('proxies'):
            self.session.proxies = kwargs.get('proxies')
        self.symbols = _convert_to_list(symbols)
        self.formatted = kwargs.get('formatted', True)
        self.endpoints = []
        self._expiration_dates = {}
        self._url_key = 'base'

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
                elif isinstance(v, list):
                    try:
                        obj[k] = [item.get('fmt') for item in v]
                    except AttributeError:
                        obj[k] = v
                else:
                    try:
                        obj[k] = datetime.fromtimestamp(v).strftime('%Y-%m-%d')
                    except (TypeError, OSError):
                        obj[k] = v
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

    def _validate_response(self, response):
        """Ensures response from API is valid

        Parameters
        ----------
        response: requests-futures.response
            A requests-futures.response object

        Returns
        -------
        response:  Parsed JSON
            A json-formatted response
        """
        if response[self._urls_dict[self._url_key]['key']]['error']:
            error = response[self._urls_dict[self._url_key]['key']]['error']
            return error.get('description')
        if not response[self._urls_dict[self._url_key]['key']]['result']:
            return 'No data found'
        return response

    def _get_endpoint(self, endpoint=None, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = endpoint if isinstance(endpoint, list) else [endpoint]
        formatted = kwargs.get('formatted', self.formatted)
        data = {}
        self._url_key = kwargs.pop('url_key', 'base')
        futures = [self.session.get(url=url, params=self.params)
                   for url in self._urls_dict[self._url_key]['urls']]
        for future in as_completed(futures):
            response = future.result()
            json = self._validate_response(response.json())
            symbol = urllib.parse.unquote(
                response.url.rsplit('/')[-1].rsplit('?')[0])
            try:
                d = json[self._urls_dict[self._url_key]['key']]['result'][0]
                if len(self.endpoints) > 1 or self.endpoints[0] is None:
                    data[symbol] = \
                        self._format_data(d) if formatted else d
                else:
                    data[symbol] = \
                        self._format_data(d[self.endpoints[0]]) if formatted \
                        else d[self.endpoints[0]]
            except TypeError:
                data[symbol] = json
        return data

    def _to_dataframe(self, endpoint=None, params={}, **kwargs):
        data = self._get_endpoint(endpoint, params, **kwargs)
        if self.formatted:
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
        else:
            return data

    def get_endpoints(self, endpoints, **kwargs):
        """
        Obtain specific endpoints for given symbol(s)

        Parameters
        ----------
        endpoints: list or str
            Desired endpoints for retrieval

        Notes
        -----
        Only returns JSON

        Raises
        ------
        ValueError
            If invalid endpoint is specified
        """
        if not isinstance(endpoints, list):
            endpoints = re.findall(r"[a-zA-Z]+", endpoints)
        if any(elem not in self.ENDPOINTS for elem in endpoints):
            raise ValueError("""
                One of {} is not a valid value.
                Valid values are {})""".format(
                    ', '.join(endpoints),
                    ', '.join(self.ENDPOINTS)
                ))
        return self._get_endpoint(endpoints, **kwargs)

    @property
    def all_endpoints(self):
        """
        Returns all base endpoints, indexed by endpoint title for each symbol

        Notes
        -----
        Only returns JSON
        """
        return self._get_endpoint(self.ENDPOINTS)

    # RETURN DICTIONARY
    @property
    def asset_profile(self):
        """Asset Profile

        Geographical and business summary data for given symbol(s).

        Returns
        -------
        dict
            assetProfile endpoint data
        """
        return self._get_endpoint("assetProfile")

    @property
    def calendar_events(self):
        """Calendar Events

        Earnings and Revenue expectations for upcoming earnings date for given
        symbol(s)

        Returns
        -------
        dict
            calendarEvents endpoint data
        """
        return self._get_endpoint("calendarEvents")

    @property
    def earnings(self):
        """Earnings

        Historical earnings data for given symbol(s)

        Returns
        -------
        dict
            earnings endpoint data
        """
        return self._get_endpoint("earnings")

    @property
    def earnings_trend(self):
        """Earnings Trend

        Historical trend data for earnings and revenue estimations for given
        symbol(s)

        Returns
        -------
        dict
            earningsTrend endpoint data
        """
        return self._get_endpoint("earningsTrend")

    @property
    def esg_scores(self):
        """ESG Scores

        Data related to a given symbol(s) environmental, social, and
        governance metrics

        Returns
        -------
        dict
            esgScores endpoint data
        """
        return self._get_endpoint("esgScores")

    @property
    def financial_data(self):
        """Financial Data

        Financial KPIs for given symbol(s)

        Returns
        -------
        dict
            financialData endpoint data
        """
        return self._get_endpoint("financialData")

    @property
    def index_trend(self):
        """Index Trend

        Trend data related given symbol(s) index, specificially PE and PEG
        ratios

        Returns
        -------
        dict
            indexTrend endpoint data
        """
        return self._get_endpoint("indexTrend")

    @property
    def industry_trend(self):
        """Industry Trend

        Seems to be deprecated

        Returns
        -------
        dict
            industryTrend endpoint data
        """
        return self._get_endpoint("industryTrend")

    @property
    def key_stats(self):
        """Key Statistics

        KPIs for given symbol(s) (PE, enterprise value, EPS, EBITA, and more)

        Returns
        -------
        dict
            defaultKeyStatistics endpoint data
        """
        return self._get_endpoint("defaultKeyStatistics")

    @property
    def major_holders(self):
        """Major Holders

        Data showing breakdown of owners of given symbol(s), insiders,
        institutions, etc.

        Returns
        -------
        dict
            majorHoldersBreakdown endpoint data
        """
        return self._get_endpoint("majorHoldersBreakdown")

    @property
    def price(self):
        """Price

        Detailed pricing data for given symbol(s), exchange, quote type,
        currency, market cap, pre / post market data, etc.

        Returns
        -------
        dict
            price endpoint data
        """
        return self._get_endpoint("price")

    @property
    def quote_type(self):
        """Quote Type

        Stock exchange specific data for given symbol(s)

        Returns
        -------
        dict
            quoteType endpoint data
        """
        return self._get_endpoint("quoteType")

    @property
    def share_purchase_activity(self):
        """Share Purchase Activity

        High-level buy / sell data for given symbol(s) insiders

        Returns
        -------
        dict
            netSharePurchaseActivity endpoint data
        """
        return self._get_endpoint("netSharePurchaseActivity")

    @property
    def summary_detail(self):
        """Summary Detail

        Contains similar data to price endpoint

        Returns
        -------
        dict
            summaryDetail endpoint data
        """
        return self._get_endpoint("summaryDetail")

    @property
    def summary_profile(self):
        """Summary Profile

        Data related to given symbol(s) location and business summary

        Returns
        -------
        dict
            summaryProfile endpoint data
        """
        return self._get_endpoint("summaryProfile")

    # RETURN DATAFRAMES
    def _financials(self, endpoint, data_filter, frequency):
        if frequency.lower() == "q":
            endpoint += "Quarterly"
        return self._to_dataframe(endpoint, data_filter=data_filter)

    def balance_sheet(self, frequency="A"):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.
        Returns
        -------
        pandas.DataFrame
            balanceSheetHistory, balanceSheetHistoryQuarterly endpoint data
        """
        return self._financials(
            "balanceSheetHistory", "balanceSheetStatements", frequency)

    def cash_flow(self, frequency="a"):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.
        Returns
        -------
        pandas.DataFrame
            cashflowStatementHistory, cashflowStatementHistoryQuarterly
            endpoint data
        """
        return self._financials(
            "cashflowStatementHistory", "cashflowStatements", frequency)

    @property
    def company_officers(self):
        """Company Officers

        Retrieves top executives for given symbol(s) and their total pay
        package.  Uses the assetProfile endpoint to retrieve data

        Returns
        -------
        pandas.DataFrame
            assetProfile endpoint data
        """
        return self._to_dataframe(
            "assetProfile", data_filter="companyOfficers")

    @property
    def earning_history(self):
        """Earning History

        Data related to historical earnings (actual vs. estimate) for given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            earningsHistory endpoint data
        """
        return self._to_dataframe("earningsHistory", data_filter="history")

    @property
    def fund_ownership(self):
        """Fund Ownership

        Data related to top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            fundOwnership endpoint data
        """
        return self._to_dataframe("fundOwnership", data_filter="ownershipList")

    @property
    def grading_history(self):
        """Grading History

        Data related to upgrades / downgrades by companies for a given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            upgradeDowngradeHistory endpoint data
        """
        return self._to_dataframe(
            "upgradeDowngradeHistory", data_filter="history")

    def income_statement(self, frequency="a"):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.
        Returns
        -------
        pandas.DataFrame
            incomeStatementHistory, incomeStatementHistoryQuarterly
            endpoint data
        """
        return self._financials(
            "incomeStatementHistory", "incomeStatementHistory", frequency)

    @property
    def insider_holders(self):
        """Insider Holders

        Data related to stock holdings of a given symbol(s) insiders

        Returns
        -------
        pandas.DataFrame
            insiderHolders endpoint data
        """
        return self._to_dataframe("insiderHolders", data_filter="holders")

    @property
    def insider_transactions(self):
        """Insider Transactions

        Data related to transactions by insiders for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            insiderTransactions endpoint data
        """
        return self._to_dataframe(
            "insiderTransactions", data_filter="transactions")

    @property
    def institution_ownership(self):
        """Institution Ownership

        Top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            institutionOwnership endpoint data
        """
        return self._to_dataframe(
            "institutionOwnership", data_filter="ownershipList")

    @property
    def recommendation_trend(self):
        """Recommendation Trend

        Data related to historical recommendations (buy, hold, sell) for a
        given symbol(s)

        Returns
        -------
        pandas.DataFrame
            recommendationTrend endpoint data
        """
        return self._to_dataframe("recommendationTrend", data_filter="trend")

    @property
    def sec_filings(self):
        """SEC Filings

        Historical SEC filings for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            secFilings endpoint data
        """
        return self._to_dataframe("secFilings", data_filter="filings")

    # FUND SPECIFIC

    @property
    def fund_category_holdings(self):
        """Fund Category Holdings

        High-level holding breakdown (cash, bonds, equity, etc.) for a given
        symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings endpoint data subset
        """
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
    def fund_performance(self):
        """Fund Performance

        Historical return data for a given symbol(s) and symbol(s) specific
        category

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            fundPerformance endpoint data
        """
        return self._get_endpoint("fundPerformance")

    @property
    def fund_profile(self):
        """Fund Profile

        Summary level information for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            fundProfile endpoint data
        """
        return self._get_endpoint("fundProfile")

    @property
    def fund_holding_info(self):
        """Fund Holding Information

        Contains information for a funds top holdings, bond ratings, bond
        holdings, equity holdings, sector weightings, and category breakdown

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings endpoint data
        """
        return self._get_endpoint("topHoldings")

    @property
    def fund_top_holdings(self):
        """Fund Top Holdings

        Retrieves Top 10 holdings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings endpoint data subset
        """
        return self._to_dataframe("topHoldings", data_filter="holdings")

    @property
    def fund_bond_ratings(self):
        """Fund Bond Ratings

        Retrieves aggregated bond rating data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings endpoint data subset
        """
        return self._to_dataframe(
            "topHoldings", data_filter="bondRatings", from_dict=True)

    @property
    def fund_sector_weightings(self):
        """Fund Sector Weightings

        Retrieves aggregated sector weightings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings endpoint data subset
        """
        return self._to_dataframe(
            "topHoldings", data_filter="sectorWeightings", from_dict=True)

    def _fund_holdings(self, holding_type):
        data = self.fund_holding_info
        for symbol in self.symbols:
            try:
                data[symbol] = data[symbol][holding_type]
            except TypeError:
                pass
        return data

    @property
    def fund_bond_holdings(self):
        """Fund Bond Holdings

        Retrieves aggregated maturity and duration information for a given
        symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings endpoint data subset
        """
        return self._fund_holdings("bondHoldings")

    @property
    def fund_equity_holdings(self):
        """Fund Equity Holdings

        Retrieves aggregated priceTo____ data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings endpoint data subset
        """
        return self._fund_holdings("equityHoldings")

    # OPTIONS

    def _get_options(self):
        data = self._get_endpoint(
            url_key='options', formatted=False)
        for symbol in self.symbols:
            self._expiration_dates[symbol] = {}
            try:
                for exp_date in data[symbol]['expirationDates']:
                    self._expiration_dates[symbol][exp_date] = \
                        pd.to_datetime(exp_date, unit='s')
            except TypeError:
                # No data
                pass

    def _options_to_dataframe(self, options, symbol, date):
        dataframes = []
        for optionType in ['calls', 'puts']:
            df = pd.DataFrame(options[optionType])
            df['optionType'] = optionType
            dataframes.append(df)
        df = pd.concat(dataframes, sort=False)
        df['symbol'] = symbol
        df['expirationDate'] = self._expiration_dates[symbol][int(date)]
        try:
            df['lastTradeDate'] = pd.to_datetime(df['lastTradeDate'], unit='s')
        except KeyError:
            pass
        return df

    @property
    def option_chain(self):
        """Option Chain

        Retrieves calls and puts for each expiration date for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            option chain for each expiration date
        """
        dataframes = []
        futures = []
        if not self._expiration_dates:
            self._get_options()
        for url in self._urls_dict['options']['urls']:
            symbol = url.rsplit('/')[-1]
            futures.extend(
                [self.session.get(url=url, params={
                    'date': date})
                 for date in list(self._expiration_dates[symbol].keys())])
        for future in as_completed(futures):
            response = future.result()
            json = self._validate_response(response.json())
            symbol = urllib.parse.unquote(
                response.url.rsplit("/")[-1].rsplit('?')[0])
            date = response.url.rsplit("=")[-1]
            data = json['optionChain']['result'][0]
            df = self._options_to_dataframe(
                data['options'][0], symbol, date)
            dataframes.append(df)
        if dataframes:
            df = pd.concat(dataframes, sort=False)
            df.set_index(['symbol', 'expirationDate', 'optionType'],
                         inplace=True)
            df.rename_axis(['symbol', 'expirationDate', 'optionType'],
                           inplace=True)
            df.fillna(0, inplace=True)
            return df
        else:
            return "No option chain data found"

    # HISTORICAL PRICE DATA

    def _get_historical_data(self, period, interval, start, end, **kwargs):
        if start or period is None or period.lower() == 'max':
            start = _convert_to_timestamp(start)
            end = _convert_to_timestamp(end, start=False)
            params = {'period1': start, 'period2': end}
        else:
            period = period.lower()
            if period not in self.PERIODS:
                raise ValueError("Period values must be one of {}".format(
                    ', '.join(self.PERIODS)))
            params = {'range': period}
        if interval not in self.INTERVALS:
            raise ValueError("Interval values must be one of {}".format(
                ', '.join(self.INTERVALS)))
        params['interval'] = interval.lower()
        data = self._get_endpoint(
            url_key='chart', params=params, formatted=False)
        return data

    def _historical_data_to_dataframe(self, data, **kwargs):
        d = {}
        for symbol in self.symbols:
            if 'timestamp' in data[symbol]:
                d[symbol] = _history_dataframe(data, symbol)
            else:
                d[symbol] = data[symbol]
        if all(isinstance(d[key], pd.DataFrame) for key in d):
            if len(d) == 1:
                df = d[self.symbols[0]]
            else:
                df = pd.concat(list(d.values()), keys=list(d.keys()),
                               names=['symbol', 'date'], sort=False)
            columns = list(df.columns)
            if 'dividends' in columns:
                df[['dividends']] = df[['dividends']].fillna(value=0)
                columns.remove('dividends')
            if 'splits' in columns:
                df[['splits']] = df[['splits']].fillna(value=0)
                columns.remove('splits')
            try:
                df[columns] = df.groupby(['symbol'])[columns].ffill()
            except (KeyError, ValueError):
                df.fillna(method='ffill', inplace=True)
            return df
        return d

    def history(
            self, period='ytd', interval='1d', start=None, end=None, **kwargs):
        """
        Historical pricing data

        Pulls historical pricing data for a given symbol(s)

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

        Returns
        -------
        pandas.DataFrame
            historical pricing data
        """
        data = self._get_historical_data(
            period, interval, start, end, **kwargs)
        df = self._historical_data_to_dataframe(data, **kwargs)
        return df
