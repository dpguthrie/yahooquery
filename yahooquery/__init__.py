"""Python interface to unofficial Yahoo Finance API endpoints"""

name = "yahooquery"
__version__ = "2.3.2"

from .research import Research  # noqa
from .ticker import Ticker  # noqa
from .screener import Screener  # noqa
from .misc import (  # noqa
    get_currencies,
    get_exchanges,
    get_market_summary,
    get_trending,
    search,
)
