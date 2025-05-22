# stdlib
import logging
import os
from concurrent.futures import as_completed
from datetime import datetime
from typing import ClassVar
from urllib import parse

# third party
from requests_futures.sessions import FuturesSession
from tqdm import tqdm

# first party
from yahooquery.constants import (
    CONFIG,
    COUNTRIES,
)
from yahooquery.headless import YahooFinanceHeadless, has_selenium
from yahooquery.session_management import get_crumb, initialize_session
from yahooquery.utils import convert_to_list

logger = logging.getLogger(__name__)


class _YahooFinance:
    CHUNK: ClassVar[int] = 1500

    def __init__(self, **kwargs):
        self.country = kwargs.pop("country", "united states").lower()
        self.formatted = kwargs.pop("formatted", False)
        self.progress = kwargs.pop("progress", False)
        self.username = kwargs.pop("username", os.getenv("YF_USERNAME", None))
        self.password = kwargs.pop("password", os.getenv("YF_PASSWORD", None))
        self._setup_url = kwargs.pop("setup_url", os.getenv("YF_SETUP_URL", None))
        self.session = initialize_session(kwargs.pop("session", None), **kwargs)
        if self.username and self.password:
            self.login()
        self.crumb = get_crumb(self.session)

    @property
    def symbols(self):
        """
        List of symbol(s) used to retrieve information
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = convert_to_list(symbols)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country.lower() not in COUNTRIES:
            raise ValueError(
                "{} is not a valid country.  Valid countries include {}".format(
                    country, ", ".join(COUNTRIES.keys())
                )
            )
        self._country = country.lower()
        self._country_params = COUNTRIES[self._country]

    @property
    def default_query_params(self):
        """
        Dictionary containing default query parameters that are sent with
        each request.  The dictionary contains four keys:  lang, region,
        corsDomain, and crumb

        Notes
        -----
        The query parameters will default to
        {'lang': 'en-US', 'region': 'US', 'corsDomain': 'finance.yahoo.com'}

        To change the default query parameters, set the country property equal
        to a valid country.
        """
        params = self._country_params
        if self.crumb is not None:
            params["crumb"] = self.crumb
        return params

    def login(self) -> None:
        if has_selenium:
            instance = YahooFinanceHeadless(self.username, self.password)
            instance.login()
            if instance.cookies:
                self.session.cookies = instance.cookies
                return

            else:
                logger.warning(
                    "Unable to login and/or retrieve the appropriate cookies.  This is "
                    "most likely due to Yahoo Finance instituting recaptcha, which "
                    "this package does not support."
                )

        else:
            logger.warning(
                "You do not have the required libraries to use this feature.  Install "
                "with the following: `pip install yahooquery[premium]`"
            )

    def _chunk_symbols(self, key, params=None, chunk=None, **kwargs):
        current_symbols = self.symbols
        all_data = [] if kwargs.get("list_result") else {}
        chunk = chunk or self.CHUNK
        for i in tqdm(range(0, len(current_symbols), chunk), disable=not self.progress):
            self._symbols = current_symbols[i : i + chunk]
            data = self._get_data(key, params, disable=True, **kwargs)
            if isinstance(data, str):
                self._symbols = current_symbols
                return data
            all_data.extend(data) if isinstance(all_data, list) else all_data.update(
                data
            )
        self.symbols = current_symbols
        return all_data

    def validate_symbols(self) -> tuple[list[str], list[str]]:
        """Symbol Validation

        Validate existence of given symbol(s) and modify the symbols property
        to include only the valid symbols.  If invalid symbols were passed,
        they will be stored in the `invalid_symbols` property.
        """
        data = self._chunk_symbols("validation")
        valid_symbols = []
        invalid_symbols = []
        for k, v in data.items():
            if v:
                valid_symbols.append(k)
            else:
                invalid_symbols.append(k)

        return valid_symbols, invalid_symbols

    def _format_data(self, obj, dates):
        for k, v in obj.items():
            if k in dates:
                if isinstance(v, dict):
                    obj[k] = v.get("fmt", v)
                elif isinstance(v, list):
                    try:
                        obj[k] = [item.get("fmt") for item in v]
                    except AttributeError:
                        obj[k] = [
                            datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:S")
                            for date in v
                        ]
                else:
                    try:
                        obj[k] = datetime.fromtimestamp(v).strftime("%Y-%m-%d %H:%M:%S")
                    except (TypeError, OSError):
                        obj[k] = v
            elif isinstance(v, dict):
                if "raw" in v:
                    obj[k] = v.get("raw")
                elif "min" in v:
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

    def _get_data(self, key, params=None, **kwargs):
        config = CONFIG[key]
        params = self._construct_params(config, params)
        urls = self._construct_urls(config, params, **kwargs)
        response_field = config["response_field"]
        try:
            if isinstance(self.session, FuturesSession):
                data = self._async_requests(response_field, urls, params, **kwargs)
            else:
                data = self._sync_requests(response_field, urls, params, **kwargs)
            return data
        except ValueError:
            return {"error": "HTTP 404 Not Found.  Please try again"}

    def _construct_params(self, config, params=None):
        params = params or {}
        required_params = [
            k
            for k in config["query"]
            if config["query"][k]["required"] and "symbol" not in k
        ]
        for required in required_params:
            if not params.get(required):
                params.update(
                    {
                        required: getattr(
                            self, required, config["query"][required]["default"]
                        )
                    }
                )
        optional_params = [
            k
            for k in config["query"]
            if not config["query"][k]["required"]
            and config["query"][k]["default"] is not None
        ]
        for optional in optional_params:
            params.update(
                {
                    optional: getattr(
                        self, optional, config["query"][optional]["default"]
                    )
                }
            )
        params.update(self.default_query_params)
        params = {
            k: str(v).lower() if v is True or v is False else v
            for k, v in params.items()
        }
        if "symbol" in config["query"]:
            return [dict(params, symbol=symbol) for symbol in self._symbols]
        return params

    def _construct_urls(self, config, params, **kwargs):
        """Construct URL requests"""
        if kwargs.get("method") == "post":
            urls = [
                self.session.post(
                    url=config["path"], params=params, json=kwargs.get("payload")
                )
            ]
        elif "symbol" in config["query"]:
            ls = (
                params
                if isinstance(self.session, FuturesSession)
                else tqdm(params, disable=not self.progress)
            )
            urls = [self.session.get(url=config["path"], params=p) for p in ls]
        elif "symbols" in config["query"]:
            params.update({"symbols": ",".join(self._symbols)})
            urls = [self.session.get(url=config["path"], params=params)]
        else:
            ls = (
                self._symbols
                if isinstance(self.session, FuturesSession)
                else tqdm(self._symbols, disable=not self.progress)
            )
            urls = [
                self.session.get(
                    url=config["path"].format(**{"symbol": symbol}), params=params
                )
                for symbol in ls
            ]
        return urls

    def _async_requests(self, response_field, urls, params, **kwargs):
        data = {}
        for future in tqdm(
            as_completed(urls),
            total=len(urls),
            disable=kwargs.get("disable", not self.progress),
        ):
            response = future.result()
            json = self._validate_response(response.json(), response_field)
            symbol = self._get_symbol(response, params)
            if symbol is not None:
                data[symbol] = self._construct_data(json, response_field, **kwargs)
            else:
                data = self._construct_data(json, response_field, **kwargs)
        return data

    def _sync_requests(self, response_field, urls, params, **kwargs):
        data = {}
        for response in urls:
            json = self._validate_response(response.json(), response_field)
            symbol = self._get_symbol(response, params)
            if symbol is not None:
                data[symbol] = self._construct_data(json, response_field, **kwargs)
            else:
                data = self._construct_data(json, response_field, **kwargs)
        return data

    def _validate_response(self, response, response_field):
        try:
            if response[response_field]["error"]:
                error = response[response_field]["error"]
                return error.get("description")
            if not response[response_field]["result"]:
                return "No data found"
            return response
        except KeyError:
            if "finance" in response:
                if response["finance"].get("error"):
                    return response["finance"]["error"]["description"]
                return response
            return {response_field: {"result": [response]}}

    def _get_symbol(self, response, params):
        if isinstance(params, list):
            query_params = dict(parse.parse_qsl(parse.urlsplit(response.url).query))
            return query_params["symbol"]
        if "symbols" in params:
            return None
        return parse.unquote(response.url.rsplit("/")[-1].split("?")[0])

    def _construct_data(self, json, response_field, **kwargs):
        try:
            addl_key = kwargs.get("addl_key")
            if addl_key:
                data = json[response_field]["result"][0][addl_key]
            elif kwargs.get("list_result", False):
                data = json[response_field]["result"]
            else:
                data = json[response_field]["result"][0]
        except KeyError:
            data = (
                json[response_field]["result"][addl_key]
                if addl_key
                else json[response_field]["result"]
            )
        except TypeError:
            data = json
        return data
