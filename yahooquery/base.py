import requests
# import urllib3
import os

from yahooquery.utils import _init_session
from yahooquery.utils.exceptions import YahooQueryError


class _YahooBase(object):
    """
    Base class for retrieving security information from Yahoo Finance.
    Conducts query operations and output for data retrieved from API
    """

    # Base URL
    _YAHOO_API_URL = "https://query2.finance.yahoo.com"

    _CHART_API_URL = "https://query1.finance.yahoo.com"

    _VALID_FORMATS = ('json', 'pandas')

    def __init__(self, **kwargs):
        self.session = _init_session(kwargs.get("session"))
        self.output_format = kwargs.get(
            "output_format", os.getenv("YQ_OUTPUT_FORMAT", 'json'))

    @property
    def params(self):
        return {}

    @property
    def urls(self):
        pass

    def _validate_response(self, response):
        """Ensures response from API is valid

        Parameters
        ----------
        response: requests.response
            A requests.response object

        Returns
        -------
        response:  Parsed JSON
            A json-formatted response

        Raises
        ------
        YahooQueryError
            If security is not found

        """
        try:
            if response['quoteSummary']['error']:
                error = response['quoteSummary']['error']
                raise YahooQueryError(
                    error.get('code'), error.get('description'))
        except KeyError:
            if not response.get('chart', None):
                if not response.get('optionChain'):
                    raise YahooQueryError()
        return response

    def _execute_yahoo_query(self, url, **kwargs):
        """Executes HTTP Request

        Given a URL, execute HTTP request from Yahoo server.

        Parameters
        ----------
        url: str
            A properly-formatted url

        Returns
        -------
        response: request.response
            Sends requests.response object to validator

        Raises
        ------
        YahooQueryError
            If problems arise when making the query
        """
        if 'other_params' in kwargs:
            response = self.session.get(
                url=url, params=kwargs.get('other_params'))
        else:
            response = self.session.get(url=url, params=self.params)
        if response.status_code == requests.codes.ok:
            return self._validate_response(response.json())
        for key in ['quoteSummary', 'chart']:
            if response.json().get(key):
                error = response.json().get(key).get('error')
        if error:
            return error.get('description')
        raise YahooQueryError()

    def fetch(self, url, **kwargs):
        data = self._execute_yahoo_query(url, **kwargs)
        return data

    def _output_format(self, data, **kwargs):
        if self.output_format == 'json':
            return data
        else:
            return self._format_pandas(data, **kwargs)

    def _format_pandas(self, data, **kwargs):
        return data
