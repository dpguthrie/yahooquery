"""Python interface to unofficial Yahoo Finance API endpoints"""

name = "yahooquery"
__version__ = "2.4.1"


from .misc import (  # noqa
    get_currencies,
    get_exchanges,
    get_market_summary,
    get_trending,
    search,
)
from .research import Research  # noqa
from .screener import Screener  # noqa
from .ticker import Ticker  # noqa

__all__ = [
    "Research",
    "Screener",
    "Ticker",
    "get_currencies",
    "get_exchanges",
    "get_market_summary",
    "get_trending",
    "search",
]
