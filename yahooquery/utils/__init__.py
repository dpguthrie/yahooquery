import requests
import urllib3

import pandas as pd
import pandas.compat as compat

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _init_session(session):
    if session is None:
        session = requests.session()
    return session


def _handle_lists(l, mult=True, err_msg=None):
    if isinstance(l, (compat.string_types, int)):
        return [l] if mult is True else l
    elif isinstance(l, pd.DataFrame) and mult is True:
        return list(l.index)
    elif mult is True:
        return list(l)
    else:
        raise ValueError(err_msg or "Only 1 symbol/market parameter allowed.")


def no_pandas(out):
    return out

