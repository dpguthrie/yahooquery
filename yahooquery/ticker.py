# stdlib
import re
from datetime import datetime, timedelta

# third party
import pandas as pd

# first party
from yahooquery.base import _YahooFinance
from yahooquery.constants import (
    CONFIG,
    CORPORATE_EVENTS,
    FUND_DETAILS,
    FUNDAMENTALS_OPTIONS,
    FUNDAMENTALS_TIME_ARGS,
    MODULES_DICT,
)
from yahooquery.utils import convert_to_timestamp, flatten_list, history_dataframe


class Ticker(_YahooFinance):
    """
    Base class for interacting with Yahoo Finance API

    Arguments
    ----------
    symbols: str or list
        Symbol or list collection of symbols

    Keyword Arguments
    -----------------
    asynchronous: bool, default False, optional
        Defines whether the requests are made synchronously or asynchronously.
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    formatted: bool, default False, optional
        Quantitative values are given as dictionaries with at least two
        keys:  'raw' and 'fmt'.  The 'raw' key expresses value numerically
        and the 'fmt' key expresses the value as a string.  See Notes for more
        detail
    max_workers: int, default 8, optional
        Defines the number of workers used to make asynchronous requests.
        This only matters when asynchronous=True
    proxies: dict, default None, optional
        Allows for the session to use a proxy when making requests
    timeout: int, default 5, optional
        Stop waiting for a response after a given number of seconds
    user_agent: str, default random.choice, optional
        A browser's user-agent string that is sent with the headers on each
        request
    validate: bool, default False, optional
        Validate existence of symbols during instantiation
    verify: bool or str, default True, optional
        Used to verify SSL certificates for HTTPS requests.  Can either be
        a boolean, in which case it controsl whether we verify the server's
        TLS certificate, or a string in which case it must be a path to a CA
        bundle to use.

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
        validate = kwargs.pop("validate", False)
        super().__init__(**kwargs)
        self.symbols = symbols
        self.invalid_symbols = None
        if validate:
            self.symbols, self.invalid_symbols = self.validate_symbols()

    def _quote_summary(self, modules):
        kwargs = {}
        params = {"modules": ",".join(modules)}
        if len(modules) == 1:
            kwargs.update({"addl_key": modules[0]})
        data = self._get_data(key="quoteSummary", params=params, **kwargs)
        dates = flatten_list(
            [MODULES_DICT[module]["convert_dates"] for module in modules]
        )
        return data if self.formatted else self._format_data(data, dates)

    def _quote_summary_dataframe(self, module, **kwargs):
        data = self._quote_summary([module])
        if not kwargs.get("data_filter"):
            data_filter = MODULES_DICT[module]["filter"]
            kwargs.update({"data_filter": data_filter})
        return self._to_dataframe(data, **kwargs)

    def _to_dataframe(self, data, **kwargs):
        if not self.formatted:
            dataframes = []
            for symbol in self.symbols:
                try:
                    final_data = (
                        data[symbol][kwargs.get("data_filter")]
                        if kwargs.get("data_filter")
                        else data[symbol]
                    )
                except TypeError:
                    pass
                else:
                    if kwargs.get("from_dict"):
                        df = pd.DataFrame(
                            [(k, v) for d in final_data for k, v in d.items()]
                        )
                        df.set_index(0, inplace=True)
                        df.columns = [symbol]
                    else:
                        df = pd.DataFrame(final_data)
                    dataframes.append(df)
            try:
                if kwargs.get("from_dict", False):
                    df = pd.concat(dataframes, axis=1)
                else:
                    df = pd.concat(
                        dataframes,
                        keys=self.symbols,
                        names=["symbol", "row"],
                        sort=False,
                    )
            except ValueError:
                df = pd.DataFrame()
            finally:
                return df
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
            CONFIG["quoteSummary"]["query"]["modules"]["options"]
        )

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
        all_modules = CONFIG["quoteSummary"]["query"]["modules"]["options"]
        if not isinstance(modules, list):
            modules = re.findall(r"[a-zA-Z]+", modules)
        if any(elem not in all_modules for elem in modules):
            raise ValueError(
                """
                One of {} is not a valid value.  Valid values are {}.
            """.format(", ".join(modules), ", ".join(all_modules))
            )
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
        return self._quote_summary(["assetProfile"])

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
        return self._quote_summary(["calendarEvents"])

    @property
    def earnings(self):
        """Earnings

        Historical earnings data for given symbol(s)

        Returns
        -------
        dict
            earnings module data
        """
        return self._quote_summary(["earnings"])

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
        return self._quote_summary(["earningsTrend"])

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
        return self._quote_summary(["esgScores"])

    @property
    def financial_data(self):
        """Financial Data

        Financial KPIs for given symbol(s)

        Returns
        -------
        dict
            financialData module data
        """
        return self._quote_summary(["financialData"])

    def news(self, count=25, start=None):
        """News articles related to given symbol(s)

        Obtain news articles related to a given symbol(s).  Data includes
        the title of the article, summary, url, author_name, publisher

        Parameters
        ----------
        count: int
            Desired number of news items to return
        start: str or datetime
            Date to begin retrieving news items.  If date is a str, utilize
            the following format: YYYY-MM-DD.

        Notes
        -----
        It's recommended to use only one symbol for this property as the data
        returned does not distinguish between what symbol the news stories
        belong to

        Returns
        -------
        dict
        """
        if start:
            start = convert_to_timestamp(start)
        return self._chunk_symbols(
            "news", params={"count": count, "start": start}, list_result=True
        )

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
        return self._quote_summary(["indexTrend"])

    @property
    def industry_trend(self):
        """Industry Trend

        Seems to be deprecated

        Returns
        -------
        dict
            industryTrend module data
        """
        return self._quote_summary(["industryTrend"])

    @property
    def key_stats(self):
        """Key Statistics

        KPIs for given symbol(s) (PE, enterprise value, EPS, EBITA, and more)

        Returns
        -------
        dict
            defaultKeyStatistics module data
        """
        return self._quote_summary(["defaultKeyStatistics"])

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
        return self._quote_summary(["majorHoldersBreakdown"])

    @property
    def page_views(self):
        """Page Views

        Short, Mid, and Long-term trend data regarding a symbol(s) page views

        Returns
        -------
        dict
            pageViews module data
        """
        return self._quote_summary(["pageViews"])

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
        return self._quote_summary(["price"])

    @property
    def quote_type(self):
        """Quote Type

        Stock exchange specific data for given symbol(s)

        Returns
        -------
        dict
            quoteType module data
        """
        return self._quote_summary(["quoteType"])

    @property
    def quotes(self):
        """Quotes

        Retrieve quotes for multiple symbols with one call

        Notes
        -----
        There will be more than one request if passing in more than 1,500
        symbols.  A 414 error code (URI Too long) will occur otherwise.

        Returns
        -------
        dict
        """
        data = self._chunk_symbols("quotes", list_result=True)
        try:
            return {item.pop("symbol"): item for item in data}
        except AttributeError:
            return data

    @property
    def recommendations(self):
        """Recommendations

        Retrieve the top 5 symbols that are similar to a given symbol

        Returns
        -------
        dict
        """
        return self._get_data("recommendations")

    @property
    def share_purchase_activity(self):
        """Share Purchase Activity

        High-level buy / sell data for given symbol(s) insiders

        Returns
        -------
        dict
            netSharePurchaseActivity module data
        """
        return self._quote_summary(["netSharePurchaseActivity"])

    @property
    def summary_detail(self):
        """Summary Detail

        Contains similar data to price endpoint

        Returns
        -------
        dict
            summaryDetail module data
        """
        return self._quote_summary(["summaryDetail"])

    @property
    def summary_profile(self):
        """Summary Profile

        Data related to given symbol(s) location and business summary

        Returns
        -------
        dict
            summaryProfile module data
        """
        return self._quote_summary(["summaryProfile"])

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
        return self._get_data("insights")

    def _financials(
        self, financials_type, frequency=None, premium=False, types=None, trailing=True
    ):
        try:
            time_dict = FUNDAMENTALS_TIME_ARGS[frequency[:1].lower()]
            prefix = time_dict["prefix"]
            period_type = time_dict["period_type"]
        except KeyError as e:
            raise (e)
        except TypeError:
            prefix = ""
            period_type = ""
        key = "fundamentals_premium" if premium else "fundamentals"
        types = types or CONFIG[key]["query"]["type"]["options"][financials_type]
        if trailing:
            prefixed_types = [f"{prefix}{t}" for t in types] + [
                f"trailing{t}" for t in types
            ]
        else:
            prefixed_types = [f"{prefix}{t}" for t in types]
        data = self._get_data(
            key, {"type": ",".join(prefixed_types)}, **{"list_result": True}
        )
        dataframes = []
        try:
            for k in data.keys():
                if isinstance(data[k], str) or data[k][0].get("description"):
                    return data
                dataframes.extend(
                    [
                        self._financials_dataframes(data[k][i], period_type)
                        for i in range(len(data[k]))
                    ]
                )
        except AttributeError:
            return data
        try:
            df = pd.concat(dataframes, sort=False)
            if prefix:
                ls = [prefix, "trailing"] if trailing else [prefix]
                for p in ls:
                    df["dataType"] = df["dataType"].apply(lambda x: str(x).lstrip(p))
                df["asOfDate"] = pd.to_datetime(df["asOfDate"], format="%Y-%m-%d")
                index = ["symbol", "asOfDate", "periodType"]
                if financials_type != "valuation":
                    index.append("currencyCode")
                df = df.pivot_table(
                    index=index,
                    columns="dataType",
                    values="reportedValue",
                )
                return pd.DataFrame(df.to_records()).set_index("symbol")
            else:
                df["sourceDate"] = pd.to_datetime(df["sourceDate"], format="%Y-%m-%d")
                df.rename(columns={"sourceDate": "date"}, inplace=True)
                df.set_index(["symbol", "date"], inplace=True)
                return df
        except ValueError:
            return "{} data unavailable for {}".format(
                financials_type.replace("_", " ").title(), ", ".join(self._symbols)
            )

    def _financials_dataframes(self, data, period_type):
        data_type = data["meta"]["type"][0]
        symbol = data["meta"]["symbol"][0]
        try:
            df = pd.DataFrame.from_records(data[data_type])
            if period_type:
                df["reportedValue"] = df["reportedValue"].apply(
                    lambda x: x.get("raw") if isinstance(x, dict) else x
                )
                df["dataType"] = data_type
                df["symbol"] = symbol
            else:
                df["symbol"] = symbol
                df["parentTopics"] = df["parentTopics"].apply(
                    lambda x: x[0].get("topicLabel")
                )
            return df
        except KeyError:
            # No data is available for that type
            pass

    def all_financial_data(self, frequency="a"):
        """
        Retrieve all financial data, including income statement,
        balance sheet, cash flow, and valuation measures.

        Notes
        -----
        The trailing twelve month (TTM) data is not available through this
        method

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        """
        types = flatten_list(
            [FUNDAMENTALS_OPTIONS[option] for option in FUNDAMENTALS_OPTIONS]
        )
        return self._financials("cash_flow", frequency, types=types, trailing=False)

    def get_financial_data(self, types, frequency="a", trailing=True):
        """
        Obtain specific data from either cash flow, income statement,
        balance sheet, or valuation measures.

        Notes
        -----
        See available options to pass to method through FUNDAMENTALS_OPTIONS

        Parameters
        ----------
        types: list or str
            Desired types of data for retrieval
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Raises
        ------
        ValueError
            If invalid type is specified
        """
        if not isinstance(types, list):
            types = re.findall(r"[a-zA-Z]+", types)
        return self._financials("cash_flow", frequency, types=types, trailing=trailing)

    @property
    def corporate_events(self):
        return self._financials(
            "cash_flow", frequency=None, types=CORPORATE_EVENTS, trailing=False
        )

    @property
    def corporate_guidance(self):
        """"""
        return self._financials(
            "cash_flow",
            frequency=None,
            types=["sigdev_corporate_guidance"],
            trailing=False,
        )

    @property
    def valuation_measures(self):
        """Valuation Measures
        Retrieves valuation measures for most recent four quarters as well
        as the most recent date

        Notes
        -----
        Only quarterly data is available for non-premium subscribers
        """
        return self._financials("valuation", "q")

    def balance_sheet(self, frequency="a"):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials("balance_sheet", frequency)

    def cash_flow(self, frequency="a", trailing=True):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials("cash_flow", frequency, trailing=trailing)

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
        return self._quote_summary_dataframe("earningsHistory")

    @property
    def fund_ownership(self):
        """Fund Ownership

        Data related to top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            fundOwnership module data
        """
        return self._quote_summary_dataframe("fundOwnership")

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
        return self._quote_summary_dataframe("upgradeDowngradeHistory")

    def income_statement(self, frequency="a", trailing=True):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials("income_statement", frequency, trailing=trailing)

    @property
    def insider_holders(self):
        """Insider Holders

        Data related to stock holdings of a given symbol(s) insiders

        Returns
        -------
        pandas.DataFrame
            insiderHolders module data
        """
        return self._quote_summary_dataframe("insiderHolders")

    @property
    def insider_transactions(self):
        """Insider Transactions

        Data related to transactions by insiders for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            insiderTransactions module data
        """
        return self._quote_summary_dataframe("insiderTransactions")

    @property
    def institution_ownership(self):
        """Institution Ownership

        Top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            institutionOwnership module data
        """
        return self._quote_summary_dataframe("institutionOwnership")

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
        return self._quote_summary_dataframe("recommendationTrend")

    @property
    def sec_filings(self):
        """SEC Filings

        Historical SEC filings for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            secFilings endpoint data
        """
        return self._quote_summary_dataframe("secFilings")

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
            for key in FUND_DETAILS:
                try:
                    del data_dict[symbol][key]
                except TypeError:
                    return data_dict
        return pd.DataFrame(
            [pd.Series(data_dict[symbol]) for symbol in self.symbols],
            index=self.symbols,
        )

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
        return self._quote_summary_dataframe("topHoldings", data_filter="holdings")

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
            "topHoldings", data_filter="bondRatings", from_dict=True
        )

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
            "topHoldings", data_filter="sectorWeightings", from_dict=True
        )

    @property
    def p_fair_value(self):
        return self._get_data("yfp_fair_value")

    # PREMIUM
    def p_all_financial_data(self, frequency="a"):
        """
        Retrieve all financial data, including income statement,
        balance sheet, cash flow, and valuation measures.

        Notes
        -----
        The trailing twelve month (TTM) data is not available through this
        method

        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        """
        types = flatten_list(
            [FUNDAMENTALS_OPTIONS[option] for option in FUNDAMENTALS_OPTIONS]
        )
        return self._financials(
            "cash_flow", frequency, premium=True, types=types, trailing=False
        )

    def p_get_financial_data(self, types, frequency="a", trailing=True):
        """
        Obtain specific data from either cash flow, income statement,
        balance sheet, or valuation measures.

        Notes
        -----
        See available options to pass to method through FUNDAMENTALS_OPTIONS

        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Parameters
        ----------
        types: list or str
            Desired types of data for retrieval
        frequency: str, default 'a', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned
        """
        if not isinstance(types, list):
            types = re.findall(r"[a-zA-Z]+", types)
        return self._financials(
            "cash_flow", frequency, True, types=types, trailing=trailing
        )

    def p_balance_sheet(self, frequency="a"):
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
        return self._financials("balance_sheet", frequency, premium=True)

    def p_cash_flow(self, frequency="a", trailing=True):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials("cash_flow", frequency, premium=True, trailing=trailing)

    @property
    def p_corporate_events(self):
        return self._financials(
            "cash_flow",
            frequency=None,
            premium=True,
            types=CORPORATE_EVENTS,
            trailing=False,
        )

    def p_income_statement(self, frequency="a", trailing=True):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        return self._financials(
            "income_statement", frequency, premium=True, trailing=trailing
        )

    @property
    def p_company_360(self):
        return self._get_data("company360")

    @property
    def p_technical_insights(self):
        return self._get_data("premium_insights")

    @property
    def p_portal(self):
        return self._chunk_symbols("premium_portal")

    def p_reports(self, report_id):
        return self._get_data("reports", {"reportId": report_id})

    def p_ideas(self, idea_id):
        return self._get_data("trade_ideas", {"ideaId": idea_id})

    @property
    def p_technical_events(self):
        return self._get_data("technical_events")

    def p_valuation_measures(self, frequency="q"):
        """Valuation Measures
        Retrieves valuation measures for all available dates for given
        symbol(s)
        """
        return self._financials("valuation", frequency, premium=True)

    @property
    def p_value_analyzer(self):
        return self._chunk_symbols("value_analyzer")

    @property
    def p_value_analyzer_drilldown(self):
        return self._get_data("value_analyzer_drilldown")

    # HISTORICAL PRICE DATA
    def dividend_history(self, start, end=None):
        """
        Historical dividend data

        Pulls historical dividend data for a given symbol(s)

        Parameters
        ----------
        start: str or datetime.datetime
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
        df = self.history(start=start, end=end)
        if "dividends" in df:
            return df[df["dividends"] != 0].loc[:, ["dividends"]]

        return pd.DataFrame(columns=["symbol", "date", "dividends"]).set_index(
            ["symbol", "date"]
        )["dividends"]

    def history(
        self,
        period="ytd",
        interval="1d",
        start=None,
        end=None,
        adj_timezone=True,
        adj_ohlc=False,
    ):
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
        adj_timezone: bool, default True, optional
            Specify whether or not to apply the GMT offset to the timestamp
            received from the API.  If True, the datetimeindex will be adjusted
            to the specified ticker's timezone.
        adj_ohlc: bool, default False, optional
            Calculates an adjusted open, high, low and close prices according
            to split and dividend information

        Returns
        -------
        pandas.DataFrame
            Historical pricing data. Indexed with a pd.MultiIndex with two
            levels 'symbol' and 'dates'.

            If `interval` is intraday then 'dates' level will be
            represented with a `pd.DatetimeIndex`.

            If `interval` is '1d' or higher then 'dates' level will be
            represented with a `pd.Index` with dtype 'object'. Rows
            relating to closed sessions are indexed with `datatime.date`.
            If the 'close' of the last row represents the latest price of
            an open session then this last row will be indexed with a
            `datatime.datetime` object giving the time of the last trade
            that the 'close' price relates to.
        """
        config = CONFIG["chart"]
        intervals = config["query"]["interval"]["options"]
        if start or period is None or period.lower() == "max":
            start = convert_to_timestamp(start)
            end = convert_to_timestamp(end, start=False)
            params = {"period1": start, "period2": end}
        else:
            params = {"range": period.lower()}
        if interval not in intervals:
            raise ValueError(
                "Interval values must be one of {}".format(", ".join(intervals))
            )
        params["interval"] = interval.lower()
        if params["interval"] == "1m" and period == "1mo":
            df = self._history_1m(adj_timezone, adj_ohlc)
        else:
            data = self._get_data("chart", params)
            df = self._historical_data_to_dataframe(data, params, adj_timezone)
        if adj_ohlc and "adjclose" in df:
            df = self._adjust_ohlc(df)
        return df

    def _history_1m(self, adj_timezone=True, adj_ohlc=False):
        params = {"interval": "1m"}
        today = datetime.today()
        dates = [
            convert_to_timestamp((today - timedelta(7 * x)).date()) for x in range(5)
        ]
        dataframes = []
        for i in range(len(dates) - 1):
            params["period1"] = dates[i + 1]
            params["period2"] = dates[i]
            data = self._get_data("chart", params)
            dataframes.append(
                self._historical_data_to_dataframe(data, params, adj_timezone)
            )
        df = pd.concat(dataframes, sort=True)
        df.sort_values(by=["symbol", "date"], inplace=True)
        df.fillna(value=0, inplace=True)
        return df

    def _historical_data_to_dataframe(self, data, params, adj_timezone):
        d = {}
        for symbol in self._symbols:
            if "timestamp" in data[symbol]:
                daily = params["interval"][-1] not in ["m", "h"]
                d[symbol] = history_dataframe(data[symbol], daily, adj_timezone)
            else:
                d[symbol] = data[symbol]
        d = {k: v for k, v in d.items() if isinstance(v, pd.DataFrame)}
        try:
            df = pd.concat(d, names=["symbol", "date"], sort=False)
        except ValueError:
            df = pd.DataFrame(columns=["high", "low", "volume", "open", "close"])
        else:
            if "dividends" in df.columns:
                df.fillna({"dividends": 0}, inplace=True)
            if "splits" in df.columns:
                df.fillna({"splits": 0}, inplace=True)
        return df

    def _adjust_ohlc(self, df):
        adjust = df["close"] / df["adjclose"]
        for col in ["open", "high", "low"]:
            df[col] = df[col] / adjust
        del df["close"]
        df.rename(columns={"adjclose": "close"}, inplace=True)
        return df

    @property
    def option_chain(self):
        data = self._get_data("options", {"getAllData": True})
        dataframes = []
        for symbol in self._symbols:
            try:
                if data[symbol]["options"]:
                    dataframes.append(
                        self._option_dataframe(data[symbol]["options"], symbol)
                    )
            except TypeError:
                pass
        if dataframes:
            df = pd.concat(dataframes, sort=False)
            df.set_index(["symbol", "expiration", "optionType"], inplace=True)
            df.rename_axis(["symbol", "expiration", "optionType"], inplace=True)
            df.fillna(0, inplace=True)
            df.sort_index(level=["symbol", "expiration", "optionType"], inplace=True)
            return df
        return "No option chain data found"

    def _option_dataframe(self, data, symbol):
        dataframes = []
        for option_type in ["calls", "puts"]:
            df = pd.concat(
                [pd.DataFrame(data[i][option_type]) for i in range(len(data))],
                sort=False,
            )
            df["optionType"] = option_type
            dataframes.append(df)
        df = pd.concat(dataframes, sort=False)
        df["symbol"] = symbol
        try:
            df["expiration"] = pd.to_datetime(df["expiration"], unit="s")
            df["lastTradeDate"] = pd.to_datetime(df["lastTradeDate"], unit="s")
        except ValueError:
            df["expiration"] = [d.get("fmt") for d in df["expiration"]]
        except KeyError:
            pass
        return df
