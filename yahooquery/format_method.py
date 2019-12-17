import collections.abc
from datetime import datetime

def map_nested_dicts(obj):
    for k, v in obj.items():
        if isinstance(v, collections.abc.Mapping):
            if k in ['convert_dates']:
                if isinstance(v, collections.abc.Mapping):
                    obj[k] = v.get('fmt', v)
                else:
                    obj[k] = datetime.fromtimestamp(v).strftime('%Y-%m-%d')
            elif v.get('raw'):
                obj[k] = v.get('raw')
            elif v.get('min'):
                obj[k] = v
            else:
                map_nested_dicts(v)
        elif isinstance(v, list):
            if isinstance(v[0], collections.abc.Mapping):
                obj[k] = [map_nested_dicts(elem) for elem in v]
                print(obj[k])
            else:
                obj[k] = v
        else:
            obj[k] = v


data = aapl.fetch(aapl._base_urls[0])['quoteSummary']['result'][0]