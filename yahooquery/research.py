# stdlib
import json
from datetime import datetime, timedelta

# third party
import pandas as pd

from yahooquery.base import _YahooFinance
from yahooquery.utils import convert_to_list


class Research(_YahooFinance):
    """Enable user interaction with research report and trade idea APIs

    Keyword Arguments:
        username (str): Yahoo username / email
        password (str): Yahoo password

    Note:
        The methods available through this class are only available for
        subscribers to Yahoo Finance Premium
    """

    _OPERATORS = ["lt", "lte", "gt", "gte", "btwn", "eq", "and", "or"]

    _DATA = {
        "report": {
            "sortType": "DESC",
            "sortField": "report_date",
            "offset": 0,
            "size": 100,
            "entityIdType": "argus_reports",
            "includeFields": [
                "report_date",
                "report_type",
                "report_title",
                "head_html",
                "ticker",
                "pdf_url",
                "snapshot_url",
                "sector",
                "id",
                "change_in_investment_rating",
                "investment_rating",
                "change_in_target_price",
                "change_in_earnings_per_share_estimate",
            ],
        },
        "trade": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "offset": 0,
            "size": 100,
            "entityIdType": "trade_idea",
            "includeFields": [
                "startdatetime",
                "term",
                "ticker",
                "rating",
                "price_target",
                "ror",
                "id",
                "image_url",
                "company_name",
                "price_timestamp",
                "current_price",
                "trade_idea_title",
                "highlights",
                "description",
            ],
        },
        "earnings": {
            "sortType": "ASC",
            "sortField": "companyshortname",
            "offset": 0,
            "size": 100,
            "entityIdType": "earnings",
            "includeFields": [
                "ticker",
                "companyshortname",
                "startdatetime",
                "startdatetimetype",
                "epsestimate",
                "epsactual",
                "epssurprisepct",
            ],
        },
        "splits": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "entityIdType": "splits",
            "includeFields": [
                "ticker",
                "companyshortname",
                "startdatetime",
                "optionable",
                "old_share_worth",
                "share_worth",
            ],
        },
        "ipo": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "entityIdType": "ipo_info",
            "includeFields": [
                "ticker",
                "companyshortname",
                "exchange_short_name",
                "filingdate",
                "startdatetime",
                "amendeddate",
                "pricefrom",
                "priceto",
                "offerprice",
                "currencyname",
                "shares",
                "dealtype",
            ],
        },
    }

    TRENDS = {"options": ["Bearish", "Bullish"], "multiple": True}

    SECTORS = {
        "options": [
            "Basic Materials",
            "Communication Services",
            "Consumer Cyclical",
            "Consumer Defensive",
            "Energy",
            "Financial Services",
            "Healthcare",
            "Industrial",
            "Real Estate",
            "Technology",
            "Utilities",
        ],
        "multiple": True,
    }

    REPORT_TYPES = {
        "options": [
            "Analyst Report",
            "Insider Activity",
            "Market Outlook",
            "Market Summary",
            "Market Update",
            "Portfolio Ideas",
            "Quantitative Report",
            "Sector Watch",
            "Stock Picks",
            "Technical Analysis",
            "Thematic Portfolio",
            "Top/Bottom Insider Activity",
        ],
        "multiple": True,
    }

    DATES = {
        "options": {"Last Week": 7, "Last Month": 30, "Last Year": 365},
        "multiple": False,
    }

    TERMS = {
        "field": "term",
        "options": ["Short term", "Mid term", "Long term"],
        "multiple": True,
    }

    _QUERY_OPTIONS = {
        "report": {
            "investment_rating": TRENDS,
            "sector": SECTORS,
            "report_type": REPORT_TYPES,
            "report_date": DATES,
        },
        "trade": {
            "trend": TRENDS,
            "sector": SECTORS,
            "term": TERMS,
            "startdatetime": DATES,
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _construct_date(self, n=0):
        return (datetime.now() - timedelta(days=n)).strftime("%Y-%m-%d")

    def _construct_query(self, research_type, **kwargs):
        operand_list = []
        for k, v in kwargs.items():
            v = convert_to_list(v, comma_split=True)
            if k not in self._QUERY_OPTIONS[research_type]:
                raise ValueError(f"{k} is an invalid argument for {research_type}")
            options = self._QUERY_OPTIONS[research_type][k]["options"]
            options = list(options.keys()) if isinstance(options, dict) else options
            if any(elem not in options for elem in v):
                raise ValueError(
                    "{} is an invalid option for {}.".format(", ".join(v), k)
                )
            if not self._QUERY_OPTIONS[research_type][k]["multiple"] and len(v) > 1:
                raise ValueError(f"Please provide only one value for {k}")
            operand_list.append(self._construct_operand(k, v, research_type))
        if len(operand_list) == 0:
            return {}
        if len(operand_list) == 1:
            return operand_list[0]
        return {"operands": operand_list, "operator": "and"}

    def _construct_operand(self, k, v, research_type):
        if len(v) == 1:
            if isinstance(self._QUERY_OPTIONS[research_type][k]["options"], dict):
                days = self._QUERY_OPTIONS[research_type][k]["options"][v[0]]
                return {
                    "operands": [k, self._construct_date(days), self._construct_date()],
                    "operator": "btwn",
                }
            return {"operands": [k, v[0]], "operator": "eq"}
        else:
            d = {"operands": [], "operator": "or"}
            for elem in v:
                d["operands"].append({"operands": [k, elem], "operator": "eq"})
            return d

    def _construct_urls(self, config, params, **kwargs):
        payloads = [
            dict(kwargs.get("payload"), offset=i)
            for i in range(0, kwargs.get("size"), 100)
        ]
        return [
            self.session.post(url=config["path"], params=params, json=payload)
            for payload in payloads
        ]

    def _get_symbol(self, response, params):
        body = response.request.body.decode("utf-8")
        return json.loads(body)["offset"]

    def _get_research(self, research_type, size, **kwargs):
        query = self._construct_query(research_type, **kwargs)
        payload = self._DATA[research_type]
        payload["query"] = query
        data = self._get_data("research", size=size, payload=payload)
        dataframes = []
        try:
            for key in data.keys():
                columns = [x["label"] for x in data[key]["documents"][0]["columns"]]
                dataframes.append(
                    pd.DataFrame(data[key]["documents"][0]["rows"], columns=columns)
                )
            return pd.concat(dataframes, ignore_index=True)
        except TypeError:
            return data

    def reports(self, size=100, **kwargs):
        """Retrieve research reports from Yahoo Finance

        Args:
            size (int, optional): Number of reports to return. Defaults to 100
            investment_rating (str or list, optional): Type of investment
                rating.  See :py:attr:`~TRENDS` for available options
            sector (str or list, optional): Sector
                See :py:attr:`~SECTORS` for available options
            report_type (str or list, optional): Report types
                See :py:attr:`~REPORT_TYPES` for available options
            report_date (str, optional): Date range
                See :py:attr:`~DATES' for available options

        Returns:
            pandas.DataFrame: DataFrame consisting of research reports

        Raises:
            ValueError: If invalid keyword argument is passed, if invalid
                option is passed for keyword argument, or if multiple values
                are passed and only a single value is accepted
        """
        return self._get_research("report", size, **kwargs)

    def trades(self, size=100, **kwargs):
        """Retrieve trade ideas from Yahoo Finance

        Args:
            size (int, optional): Number of trades to return. Defaults to 100
            trend (str or list, optional): Type of investment
                rating.  See :py:attr:`~TRENDS` for available options
            sector (str or list, optional): Sector
                See :py:attr:`~SECTORS` for available options
            term (str or list, optional): Term length (short, mid, long)
                See :py:attr:`~TERMS` for available options
            startdatetime (str, optional): Date range
                See :py:attr:`~DATES' for available options

        Returns:
            pandas.DataFrame: DataFrame consisting of trade ideas

        Raises:
            ValueError: If invalid keyword argument is passed, if invalid
                option is passed for keyword argument, or if multiple values
                are passed and only a single value is accepted
        """
        return self._get_research("trade", size, **kwargs)
