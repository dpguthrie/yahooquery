from .ticker import Ticker


class MultipleTicker(Ticker):
    def __init__(self, symbols=[], **kwargs):
        self.symbols = symbols
        super(MultipleTicker, self).__init__(**kwargs)

    @property
    def url(self):
        return [
            f"v10/finance/quoteSummary/{symbol}" for symbol in self.symbols]

    @property
    def _options_url(self):
        return [f'v7/finance/options/{symbol}' for symbol in self.symbols]

    @property
    def _chart_url(self):
        return [f'v8/finance/chart/{symbol}' for symbol in self.symbols]

    def _get_endpoint(self, endpoint, params={}, **kwargs):
        self.optional_params = params
        self.endpoints = [endpoint]
        data = {}
        for i, url in enumerate(self.url):
            json = self.fetch(new_url=url, **kwargs)
            try:
                data[self.symbols[i]] = \
                    json['quoteSummary']['result'][0][endpoint]
            except KeyError:
                data[self.symbols[i]] = json['chart']['result'][0]
        return data

    def _retrieve_relevant_data(
            self, endpoint, exclude_cols=[], convert_dates=[]):
        data = self._get_endpoint(endpoint)
        return data
