from datetime import datetime


def _format_dates(value):
    if isinstance(value, dict):
        return value.get('fmt', v)
    else:
        return datetime.fromtimestamp(value).strftime('%Y-%m-%d')

def _format_number(key, value):
    if value.get('raw'):
        return value.get('raw')
    else:
        if isinstance(value, dict):
            return (key,{f'{key}{k.capitalize()}': v for (k, v) in value.items()}
        else:
            return value


    
