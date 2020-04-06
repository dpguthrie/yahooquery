import pandas as pd
import re

from yahooquery.utils import (
    _convert_to_list, _convert_to_timestamp, _history_dataframe, _flatten_list)
from yahooquery.base import _YahooFinance


class Ticker(_YahooFinance):
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
    When formatted is set to True, all quote_summary modules will return as
    dictionaries.  There are two reasons for this:

    1. Quantitative values are expressed as dictionaries.  For example:

       "totalPay": {
           "raw": 115554666,
           "fmt": "11.56M",
           "longFmt": "11,555,466"
       }

       When formatted is set to False, the _format_data method will return
       the value in the "raw" key.

    2. Dates are either expressed as timestamps:

       "governanceEpochDate": 1570147200

       Or as dictionaries:

        "exDividendDate": {
            "raw": 1573084800,
            "fmt": "2019-11-07"
        }

        When formatted is set to False, the _format_data method will return the
        date expressed in the format YYYY-MM-DD by either converting from the
        timestamp or retrieving the "fmt" key.
    """
    def __init__(self, symbols, **kwargs):
        self._symbols = _convert_to_list(symbols)
        super(Ticker, self).__init__(**kwargs)

    def _quote_summary(self, modules):
        kwargs = {}
        params = {'modules': ','.join(modules)}
        if len(modules) == 1:
            kwargs.update({'addl_key': modules[0]})
        data = self._get_data(key='quoteSummary', params=params, **kwargs)
        dates = _flatten_list(
            [self._MODULES_DICT[module]['convert_dates']
             for module in modules])
        return data if self.formatted else self._format_data(data, dates)

    def _quote_summary_dataframe(self, module, **kwargs):
        data = self._quote_summary([module])
        if not kwargs.get('data_filter'):
            data_filter = self._MODULES_DICT[module]['filter']
            kwargs.update({'data_filter': data_filter})
        return self._to_dataframe(data, **kwargs)

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = _convert_to_list(symbols)

    def _to_dataframe(self, data, **kwargs):
        if not self.formatted:
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
                    df = pd.concat(dataframes, axis=1)
                else:
                    df = pd.concat(
                        dataframes, keys=self.symbols, names=['symbol', 'row'],
                        sort=False)
                return df
            except TypeError:
                return data
        else:
            return data

    @property
    def all_modules(self):
        """
        Returns all quoteSummary modules, indexed by module title
        for each symbol

        Notes
        -----
        Only returns JSON
        """
        return self._quote_summary(
            self._CONFIG['quoteSummary']['query']['modules']['options'])

    def get_modules(self, modules):
        """
        Obtain specific quoteSummary modules for given symbol(s)

        Parameters
        ----------
        modules: list or str
            Desired modules for retrieval

        Notes
        -----
        Only returns JSON

        Raises
        ------
        ValueError
            If invalid module is specified
        """
        all_modules = \
            self._CONFIG['quoteSummary']['query']['modules']['options']
        if not isinstance(modules, list):
            modules = re.findall(r"[a-zA-Z]+", modules)
        if any(elem not in all_modules for elem in modules):
            raise ValueError("""
                One of {} is not a valid value.  Valid values are {}.
            """.format(
                ', '.join(modules),
                ', '.join(all_modules)
            ))
        return self._quote_summary(modules)

    @property
    def asset_profile(self):
        """Asset Profile

        Geographical and business summary data for given symbol(s).

        Returns
        -------
        dict
            assetProfile module data
        """
        return self._quote_summary(['assetProfile'])

    @property
    def calendar_events(self):
        """Calendar Events

        Earnings and Revenue expectations for upcoming earnings date for given
        symbol(s)

        Returns
        -------
        dict
            calendarEvents module data
        """
        return self._quote_summary(['calendarEvents'])

    @property
    def earnings(self):
        """Earnings

        Historical earnings data for given symbol(s)

        Returns
        -------
        dict
            earnings module data
        """
        return self._quote_summary(['earnings'])

    @property
    def earnings_trend(self):
        """Earnings Trend

        Historical trend data for earnings and revenue estimations for given
        symbol(s)

        Returns
        -------
        dict
            earningsTrend module data
        """
        return self._quote_summary(['earningsTrend'])

    @property
    def esg_scores(self):
        """ESG Scores

        Data related to a given symbol(s) environmental, social, and
        governance metrics

        Returns
        -------
        dict
            esgScores module data
        """
        return self._quote_summary(['esgScores'])

    @property
    def financial_data(self):
        """Financial Data

        Financial KPIs for given symbol(s)

        Returns
        -------
        dict
            financialData module data
        """
        return self._quote_summary(['financialData'])

    @property
    def news(self):
        """News articles related to given symbol(s)

        Obtain news articles related to a given symbol(s).  Data includes
        the title of the article, summary, url, author_name, publisher

        Notes
        -----
        It's recommended to use only one symbol for this property as the data
        returned does not distinguish between what symbol the news stories
        belong to

        Returns
        -------
        dict
        """
        return self._get_data(
            'news', {}, **{'list_result': True})

    @property
    def index_trend(self):
        """Index Trend

        Trend data related given symbol(s) index, specificially PE and PEG
        ratios

        Returns
        -------
        dict
            indexTrend module data
        """
        return self._quote_summary(['indexTrend'])

    @property
    def industry_trend(self):
        """Industry Trend

        Seems to be deprecated

        Returns
        -------
        dict
            industryTrend module data
        """
        return self._quote_summary(['industryTrend'])

    @property
    def key_stats(self):
        """Key Statistics

        KPIs for given symbol(s) (PE, enterprise value, EPS, EBITA, and more)

        Returns
        -------
        dict
            defaultKeyStatistics module data
        """
        return self._quote_summary(['defaultKeyStatistics'])

    @property
    def major_holders(self):
        """Major Holders

        Data showing breakdown of owners of given symbol(s), insiders,
        institutions, etc.

        Returns
        -------
        dict
            majorHoldersBreakdown module data
        """
        return self._quote_summary(['majorHoldersBreakdown'])

    @property
    def page_views(self):
        """Page Views

        Short, Mid, and Long-term trend data regarding a symbol(s) page views

        Returns
        -------
        dict
            pageViews module data
        """
        return self._quote_summary(['pageViews'])

    @property
    def price(self):
        """Price

        Detailed pricing data for given symbol(s), exchange, quote type,
        currency, market cap, pre / post market data, etc.

        Returns
        -------
        dict
            price module data
        """
        return self._quote_summary(['price'])

    @property
    def quote_type(self):
        """Quote Type

        Stock exchange specific data for given symbol(s)

        Returns
        -------
        dict
            quoteType module data
        """
        return self._quote_summary(['quoteType'])

    @property
    def recommendations(self):
        """Recommendations

        Retrieve the top 5 symbols that are similar to a given symbol

        Returns
        -------
        dict
        """
        return self._get_data('recommendations')

    @property
    def share_purchase_activity(self):
        """Share Purchase Activity

        High-level buy / sell data for given symbol(s) insiders

        Returns
        -------
        dict
            netSharePurchaseActivity module data
        """
        return self._quote_summary(['netSharePurchaseActivity'])

    @property
    def summary_detail(self):
        """Summary Detail

        Contains similar data to price endpoint

        Returns
        -------
        dict
            summaryDetail module data
        """
        return self._quote_summary(['summaryDetail'])

    @property
    def summary_profile(self):
        """Summary Profile

        Data related to given symbol(s) location and business summary

        Returns
        -------
        dict
            summaryProfile module data
        """
        return self._quote_summary(['summaryProfile'])

    @property
    def technical_insights(self):
        """Technical Insights

        Technical trading information as well as company metrics related
        to innovativeness, sustainability, and hiring.  Metrics can also
        be compared against the company's sector

        Returns
        -------
        dict
        """
        return self._get_data('insights')

    @property
    def validation(self):
        """Symbol Validation

        Validate existence of given symbol(s)

        Returns
        -------
        dict
        """
        return self._get_data('validation')

    def _financials(self, financials_type, frequency, premium=False):
        frequency = 'annual' if frequency[:1].lower() == 'a' else 'quarterly'
        key = 'fundamentals_premium' if premium else 'fundamentals'
        types = self._CONFIG[key]['query']['type']['options'][financials_type]
        prefixed_types = ['{}{}'.format(frequency, t) for t in types] + \
                         ['trailing{}'.format(t) for t in types]
        data = self._get_data(key, {'type': ','.join(prefixed_types)}, **{
            'list_result': True})
        dataframes = []
        for k in data.keys():
            if isinstance(data[k], str):
                return data
            else:
                dataframes.extend([
                    self._financials_dataframes(data[k][i])
                    for i in range(len(data[k]))])
        try:
            df = pd.concat(dataframes)
            for prefix in [frequency, 'trailing']:
                df['dataType'] = df['dataType'].apply(
                    lambda x: str(x).lstrip(prefix))
            df['asOfDate'] = pd.to_datetime(df['asOfDate'], format='%Y-%m-%d')
            df = df.pivot_table(
                index=['symbol', 'asOfDate'], columns='dataType',
                values='reportedValue')
            return pd.DataFrame(df.to_records()).set_index('symbol')
        except ValueError:
            return '{} data unavailable for {}'.format(
                financials_type.replace('_', ' ').title(),
                ', '.join(self._symbols))

    def _financials_dataframes(self, data):
        try:
            data_type = data['meta']['type'][0]
            symbol = data['meta']['symbol'][0]
        except KeyError:
            return data
        try:
            df = pd.DataFrame.from_records(data[data_type])
            df['reportedValue'] = \
                df['reportedValue'].apply(lambda x: x.get('raw'))
            df['dataType'] = data_type
            df['symbol'] = symbol
            return df
        except KeyError:
            # No data is available for that type
            pass

    def balance_sheet(self, frequency='a'):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('balance_sheet', frequency)

    def cash_flow(self, frequency='a'):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('cash_flow', frequency)

    @property
    def company_officers(self):
        """Company Officers

        Retrieves top executives for given symbol(s) and their total pay
        package.  Uses the assetProfile module to retrieve data

        Returns
        -------
        pandas.DataFrame
            assetProfile module data
        """
        data = self._quote_summary(["assetProfile"])
        return self._to_dataframe(data, data_filter="companyOfficers")

    @property
    def earning_history(self):
        """Earning History

        Data related to historical earnings (actual vs. estimate) for given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            earningsHistory module data
        """
        return self._quote_summary_dataframe('earningsHistory')

    @property
    def fund_ownership(self):
        """Fund Ownership

        Data related to top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            fundOwnership module data
        """
        return self._quote_summary_dataframe('fundOwnership')

    @property
    def grading_history(self):
        """Grading History

        Data related to upgrades / downgrades by companies for a given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            upgradeDowngradeHistory module data
        """
        return self._quote_summary_dataframe('upgradeDowngradeHistory')

    def income_statement(self, frequency='a'):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('income_statement', frequency)

    @property
    def insider_holders(self):
        """Insider Holders

        Data related to stock holdings of a given symbol(s) insiders

        Returns
        -------
        pandas.DataFrame
            insiderHolders module data
        """
        return self._quote_summary_dataframe('insiderHolders')

    @property
    def insider_transactions(self):
        """Insider Transactions

        Data related to transactions by insiders for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            insiderTransactions module data
        """
        return self._quote_summary_dataframe('insiderTransactions')

    @property
    def institution_ownership(self):
        """Institution Ownership

        Top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            institutionOwnership module data
        """
        return self._quote_summary_dataframe('institutionOwnership')

    @property
    def recommendation_trend(self):
        """Recommendation Trend

        Data related to historical recommendations (buy, hold, sell) for a
        given symbol(s)

        Returns
        -------
        pandas.DataFrame
            recommendationTrend module data
        """
        return self._quote_summary_dataframe('recommendationTrend')

    @property
    def sec_filings(self):
        """SEC Filings

        Historical SEC filings for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            secFilings endpoint data
        """
        return self._quote_summary_dataframe('secFilings')

    # FUND SPECIFIC

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
            topHoldings module data subset
        """
        return self._fund_holdings("bondHoldings")

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
            topHoldings module data subset
        """
        data_dict = self._quote_summary(["topHoldings"])
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
    def fund_equity_holdings(self):
        """Fund Equity Holdings

        Retrieves aggregated priceTo____ data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings module data subset
        """
        return self._fund_holdings("equityHoldings")

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
            fundPerformance module data
        """
        return self._quote_summary(["fundPerformance"])

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
        return self._quote_summary(["fundProfile"])

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
            topHoldings module data
        """
        return self._quote_summary(["topHoldings"])

    @property
    def fund_top_holdings(self):
        """Fund Top Holdings

        Retrieves Top 10 holdings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        return self._quote_summary_dataframe(
            'topHoldings', data_filter='holdings')

    @property
    def fund_bond_ratings(self):
        """Fund Bond Ratings

        Retrieves aggregated bond rating data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        return self._quote_summary_dataframe(
            'topHoldings', data_filter='bondRatings', from_dict=True)

    @property
    def fund_sector_weightings(self):
        """Fund Sector Weightings

        Retrieves aggregated sector weightings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        return self._quote_summary_dataframe(
            'topHoldings', data_filter='sectorWeightings', from_dict=True)

    # PREMIUM

    def p_balance_sheet(self, frequency='a'):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('balance_sheet', frequency, premium=True)

    def p_cash_flow(self, frequency='a'):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('cash_flow', frequency, premium=True)

    def p_income_statement(self, frequency='a'):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials('income_statement', frequency, premium=True)

    @property
    def p_company_360(self):
        return self._get_data('company360')

    @property
    def p_portal(self):
        return self._get_data('premium_portal')

    def p_reports(self, report_id):
        return self._get_data('reports', {'reportId': report_id})

    def p_ideas(self, idea_id):
        return self._get_data('trade_ideas', {'ideaId': idea_id})

    @property
    def p_technical_events(self):
        return self._get_data('technical_events')

    @property
    def p_value_analyzer(self):
        return self._get_data('value_analyzer')

    @property
    def p_value_analyzer_drilldown(self):
        return self._get_data('value_analyzer_drilldown')

    # HISTORICAL PRICE DATA

    def history(self, period='ytd', interval='1d', start=None, end=None):
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
        config = self._CONFIG['chart']
        periods = config['query']['range']['options']
        intervals = config['query']['interval']['options']
        if start or period is None or period.lower() == 'max':
            start = _convert_to_timestamp(start)
            end = _convert_to_timestamp(end, start=False)
            params = {'period1': start, 'period2': end}
        else:
            period = period.lower()
            if period not in periods:
                raise ValueError("Period values must be one of {}".format(
                    ', '.join(periods)))
            params = {'range': period}
        if interval not in intervals:
            raise ValueError("Interval values must be one of {}".format(
                ', '.join(intervals)))
        params['interval'] = interval.lower()
        data = self._get_data('chart', params)
        df = self._historical_data_to_dataframe(data)
        return df

    def _historical_data_to_dataframe(self, data):
        d = {}
        for symbol in self._symbols:
            if 'timestamp' in data[symbol]:
                d[symbol] = _history_dataframe(data, symbol)
            else:
                d[symbol] = data[symbol]
        if all(isinstance(d[key], pd.DataFrame) for key in d):
            if len(d) == 1:
                df = d[self._symbols[0]]
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

    @property
    def option_chain(self):
        data = self._get_data('options', {'getAllData': True})
        dataframes = []
        for symbol in self._symbols:
            try:
                if data[symbol]['options']:
                    dataframes.append(
                        self._option_dataframe(data[symbol]['options'], symbol)
                    )
            except TypeError:
                pass
        if dataframes:
            df = pd.concat(dataframes, sort=False)
            df.set_index(
                ['symbol', 'expiration', 'optionType'], inplace=True)
            df.rename_axis(
                ['symbol', 'expiration', 'optionType'], inplace=True)
            df.fillna(0, inplace=True)
            return df
        return 'No option chain data found'

    def _option_dataframe(self, data, symbol):
        dataframes = []
        for optionType in ['calls', 'puts']:
            df = pd.concat(
                [pd.DataFrame(data[i][optionType]) for i in range(len(data))])
            df['optionType'] = optionType
            dataframes.append(df)
        df = pd.concat(dataframes, sort=False)
        df['symbol'] = symbol
        try:
            df['expiration'] = pd.to_datetime(df['expiration'], unit='s')
            df['lastTradeDate'] = pd.to_datetime(df['lastTradeDate'], unit='s')
        except KeyError:
            pass
        return df
