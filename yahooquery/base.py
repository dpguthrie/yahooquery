import requests

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

    def __init__(self, **kwargs):
        self.session = _init_session(kwargs.get("session"))
        self.output_format = kwargs.get("output_format", "json")

    @property
    def params(self):
        return {}

    @property
    def _urls(self):
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
                raise YahooQueryError(error.get('description'))
        except KeyError:
            if not any(k in response for k in ('chart', 'optionChain')):
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
        return self._execute_yahoo_query(url, **kwargs)
