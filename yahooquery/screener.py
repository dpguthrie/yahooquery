# stdlib
import re
from urllib import parse

from yahooquery.base import _YahooFinance
from yahooquery.constants import SCREENERS


class Screener(_YahooFinance):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _construct_params(self, config, params):
        new_params = {}
        optional_params = [
            k
            for k in config["query"]
            if not config["query"][k]["required"]
            and config["query"][k]["default"] is not None
        ]
        for optional in optional_params:
            new_params.update(
                {optional: params.get(optional, config["query"][optional]["default"])}
            )
        new_params.update(self.default_query_params)
        new_params = {
            k: str(v).lower() if v is True or v is False else v
            for k, v in new_params.items()
        }
        return [dict(new_params, scrIds=scrId) for scrId in params["scrIds"]]

    def _construct_urls(self, config, params):
        return [self.session.get(url=config["path"], params=p) for p in params]

    def _get_symbol(self, response, params, **kwargs):
        query_params = dict(parse.parse_qsl(parse.urlsplit(response.url).query))
        screener_id = query_params["scrIds"]
        key = next(k for k in SCREENERS if SCREENERS[k]["id"] == screener_id)
        return key

    def _check_screen_ids(self, screen_ids):
        all_screeners = list(SCREENERS.keys())
        if not isinstance(screen_ids, list):
            screen_ids = re.findall(r"[a-zA-Z0-9_]+", screen_ids)
        if any(elem not in all_screeners for elem in screen_ids):
            raise ValueError(
                "One of {} is not a valid screener.  \
                              Please check available_screeners".format(
                    ", ".join(screen_ids)
                )
            )
        return screen_ids

    @property
    def available_screeners(self):
        """Return list of keys available to pass to
        :func:`Screener.get_screeners`
        """
        return list(SCREENERS.keys())

    def get_screeners(self, screen_ids, count=25):
        """Return list of predefined screeners from Yahoo Finance

        Parameters:
        screen_ids (str or list): Keys corresponding to list
            screen_ids = 'most_actives day_gainers'
            screen_ids = ['most_actives', 'day_gainers']
        count (int): Number of items to return, default=25
        """
        valid_screen_ids = self._check_screen_ids(screen_ids)
        screen_ids = [SCREENERS[screener]["id"] for screener in valid_screen_ids]
        return self._get_data("screener", params={"scrIds": screen_ids, "count": count})
