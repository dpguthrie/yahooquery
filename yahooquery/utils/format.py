from datetime import datetime
import pandas as pd


class _Format:

    def __init__(self, dictionary, ticker):
        self.dictionary = dictionary
        self.ticker = ticker

    @property
    def format(self):
        if len(self.dictionary.keys()) > 1:
            self._format_multiple_endpoints(self.ticker.endpoints)
            return self.dictionary
        else:
            self._format_endpoint(self.ticker.endpoints[0])
            return self.dictionary[self.ticker.endpoints[0]]

    def _format_endpoint(self, endpoint):
        convert_dates = self.ticker._ENDPOINT_DICT[endpoint]['convert_dates']
        for k, v in self.dictionary[endpoint].items():
            if k.lower() in [x.lower() for x in convert_dates]:
                self.dictionary[endpoint][k] = self._format_date(v)
            elif v:
                data_type = type(v).__name__
                function_name = f'_format_{data_type}'
                fun = getattr(self, function_name, None)
                fun(k, v, endpoint, convert_dates=convert_dates)
        exclude_cols = self.ticker._ENDPOINT_DICT[endpoint]['exclude_cols']
        [self.dictionary[endpoint].pop(k) for k in exclude_cols]

    def _format_multiple_endpoints(self, endpoints):
        for endpoint in endpoints:
            self._format_endpoint(endpoint)

    def _format_date(self, value):
        if isinstance(value, dict):
            return value.get('fmt', value)
        else:
            return datetime.fromtimestamp(value).strftime('%Y-%m-%d')

    def _format_dict(self, key, value, endpoint, **kwargs):
        if kwargs.get('key2'):
            key2 = kwargs.get('key2')
            item = kwargs.get('item')
            if key2.lower() in [x.lower() for x in kwargs.get('convert_dates')]:
                self.dictionary[endpoint][key][item][key2] = \
                    self._format_date(value)
            else:
                self.dictionary[endpoint][key][item][key2] = \
                    value.get('raw', value)
        else:
            if key.lower() in [x.lower() for x in kwargs.get('convert_dates')]:
                self._format_date(value)
            else:
                self.dictionary[endpoint][key] = value.get('raw', value)

    def _format_list(self, key, value, endpoint, **kwargs):
        if type(value[0]) == dict:
            for i, list_item in enumerate(value):
                for k, v in list_item.items():
                    data_type = type(v).__name__
                    function_name = f'_format_{data_type}'
                    fun = getattr(self, function_name, None)
                    fun(key, v, endpoint, key2=k, item=i, **kwargs)

    def _format_str(self, key, value, endpoint, **kwargs):
        pass

    def _format_int(self, key, value, endpoint, **kwargs):
        pass

    def _format_bool(self, key, value, endpoint, **kwargs):
        pass

    def _format_float(self, key, value, endpoint, **kwargs):
        pass


class _Dataframe:
    def __init__(self, data, data_filter=None):
        self.data = data
        self.filter = data_filter

    def dataframe(self):
        dataframes = []
        for key in self.data.keys():
            df = pd.DataFrame(self.data[key][self.filter])
            if len(self.data.keys()) > 1:
                df['ticker'] = key.upper()
            dataframes.append(df)
        return df
