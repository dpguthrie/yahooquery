import datetime
import itertools
import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal, assert_index_equal, assert_series_equal

from yahooquery import Ticker
from yahooquery.utils import history_dataframe

TICKERS = [
    Ticker(
        "aapl", username=os.getenv("YFF_USERNAME"), password=os.getenv("YFF_PASSWORD")
    ),
    Ticker("aapl ^GSPC btcusd=x brk-b logo.is l&tfh.ns", asynchronous=True),
    Ticker("aaapl"),
    Ticker("hasgx"),
    Ticker("btcusd=x", formatted=True, validate=True),
]

FINANCIALS = [
    "cash_flow",
    "income_statement",
    "balance_sheet",
    "p_cash_flow",
    "p_income_statement",
    "p_balance_sheet",
    "all_financial_data",
    "p_all_financial_data",
    "p_valuation_measures",
]

SEPERATE_ENDPOINTS = [
    *FINANCIALS,
    "option_chain",
    "history",
    "all_modules",
    "get_modules",
    "symbols",
    "p_portal",
    "p_value_analyzer",
]


def props(cls):
    return [
        i
        for i in cls.__dict__.keys()
        if i[:1] != "_" and i[:2] != "p_" and i not in SEPERATE_ENDPOINTS
    ]


def premium_props(cls):
    return [i for i in cls.__dict__.keys() if i[:2] == "p_"]


@pytest.mark.parametrize("prop", premium_props(Ticker))
def test_premium(ticker, prop):
    assert getattr(ticker, prop) is not None


@pytest.fixture(params=TICKERS)
def ticker(request):
    return request.param


def test_symbols_change(ticker):
    ticker.symbols = "aapl msft fb"
    assert ticker.symbols == ["aapl", "msft", "fb"]


def test_p_reports(ticker):
    assert ticker.p_reports("26426_Technical Analysis_1584057600000")


def test_p_ideas(ticker):
    assert ticker.p_ideas("tc_USvyGmAAlpfwAygABAACAAAD6CYg")


def test_option_chain(ticker):
    assert ticker.option_chain is not None


def test_bad_multiple_modules_wrong(ticker):
    with pytest.raises(ValueError):
        assert ticker.get_modules(["asetProfile", "summaryProfile"])


def test_multiple_modules(ticker):
    assert ticker.get_modules(["assetProfile", "summaryProfile"]) is not None


def test_multiple_modules_str(ticker):
    assert ticker.get_modules("assetProfile summaryProfile") is not None


def test_news(ticker):
    assert ticker.news() is not None


def test_news_start(ticker):
    assert ticker.news(start="2020-01-01", count=100) is not None


def test_all_modules(ticker):
    assert ticker.all_modules is not None
    data = ticker.all_modules
    assert sorted(list(data.keys())) == sorted(ticker.all_modules)


@pytest.mark.parametrize("module", props(Ticker))
def test_modules(ticker, module):
    assert getattr(ticker, module) is not None


@pytest.mark.parametrize(
    "module, frequency", [el for el in itertools.product(FINANCIALS, ["q", "a"])]
)
def test_financials(ticker, frequency, module):
    assert getattr(ticker, module)(frequency) is not None


def test_bad_financials_arg():
    with pytest.raises(KeyError):
        assert Ticker("aapl").income_statement("r")


def test_get_financial_data(ticker):
    assert (
        ticker.get_financial_data("GrossProfit NetIncome TotalAssets ForwardPeRatio")
        is not None
    )


def test_p_get_financial_data(ticker):
    assert (
        ticker.p_get_financial_data("GrossProfit NetIncome TotalAssets ForwardPeRatio")
        is not None
    )


@pytest.mark.parametrize(
    "period, interval",
    [
        (p, i)
        for p, i in zip(
            ["1d", "1mo", "1y", "5y", "max"], ["1m", "1m", "1d", "1wk", "3mo"]
        )
    ],
)
def test_history(ticker, period, interval):
    assert isinstance(ticker.history(period, interval), pd.DataFrame)


def test_dividend_history(ticker):
    df = ticker.dividend_history(start="1970-01-01")
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "start, end",
    [
        (start, end)
        for start, end in zip(
            [datetime.datetime(2019, 1, 1), "2019-01-01"],
            ["2019-12-30", datetime.datetime(2019, 12, 30)],
        )
    ],
)
def test_history_start_end(ticker, start, end):
    assert ticker.history(start=start, end=end) is not None


@pytest.mark.parametrize(
    "period, interval", [(p, i) for p, i in zip(["2d", "1mo"], ["1m", "3m"])]
)
def test_history_bad_args(ticker, period, interval):
    with pytest.raises(ValueError):
        assert ticker.history(period, interval)


def test_adj_ohlc(ticker):
    assert ticker.history(period="max", adj_ohlc=True) is not None


class TestHistoryDataframe:
    """Tests for `utils.history_dataframe` and dependencies."""

    @pytest.fixture
    def tz_us(self):
        yield "America/New_York"

    @pytest.fixture
    def tz_oz(self):
        yield "Australia/Sydney"

    @pytest.fixture
    def tz_hk(self):
        yield "Asia/Hong_Kong"

    @pytest.fixture
    def utc(self):
        yield "UTC"

    @pytest.fixture
    def timestamps_daily(self, utc, tz_oz, tz_us, tz_hk):
        """Timestamps representing fictional open datetimes and expected mapped days.

        Expected conversions to specific timezones explicitly declared and asserted.

        Yields
        -------
        tuple[list[int]
            [0] [list[int]]
                Unix timestamps, i.e. format as used by Yahoo API. Timestamps represent
                datetimes of session opens in terms of UTC.

            [1] pd.Index dtype 'object', values as type datetime.date
                Expected days that timestamps would map to if local timezone were
                'America/New_York'. In this case all timestamps are expected to map to
                the day of the date of the timestamp.

            [2] pd.Index dtype 'object', values as type datetime.date
                Expected days that timestamps would map to if local timezone were
                'Australia/Sydney'. In this case all timestamps are expected to map to
                the day after the date of the timestamp.

            [3] pd.Index dtype 'object', values as type datetime.date
                Expected days that timestamps would map to if local timezone were 'UTC'.
                The first timestamp is expected to map to day of the date of the
                timestamp. All other timestamps are expected to map to the day after.
        """
        tss = [
            1667568600,
            1667831400,
            1667917800,
            1668004200,
            1668090600,
            1668177000,
            1668436200,
            1668522600,
            1668609000,
            1668695400,
            1668781800,
            1669041000,
            1669127400,
            1669213800,
        ]

        expected_utc = pd.DatetimeIndex(
            [
                "2022-11-04 13:30:00",
                "2022-11-07 14:30:00",
                "2022-11-08 14:30:00",
                "2022-11-09 14:30:00",
                "2022-11-10 14:30:00",
                "2022-11-11 14:30:00",
                "2022-11-14 14:30:00",
                "2022-11-15 14:30:00",
                "2022-11-16 14:30:00",
                "2022-11-17 14:30:00",
                "2022-11-18 14:30:00",
                "2022-11-21 14:30:00",
                "2022-11-22 14:30:00",
                "2022-11-23 14:30:00",
            ],
            tz=utc,
        )
        dti = pd.to_datetime(tss, unit="s")
        dti_utc = dti.tz_localize(utc)
        assert_index_equal(dti_utc, expected_utc)
        expected_utc_days = pd.Index(
            [
                datetime.date(2022, 11, 4),
                datetime.date(2022, 11, 8),
                datetime.date(2022, 11, 9),
                datetime.date(2022, 11, 10),
                datetime.date(2022, 11, 11),
                datetime.date(2022, 11, 12),
                datetime.date(2022, 11, 15),
                datetime.date(2022, 11, 16),
                datetime.date(2022, 11, 17),
                datetime.date(2022, 11, 18),
                datetime.date(2022, 11, 19),
                datetime.date(2022, 11, 22),
                datetime.date(2022, 11, 23),
                datetime.date(2022, 11, 24),
            ]
        )

        expected_oz = pd.DatetimeIndex(
            [
                "2022-11-05 00:30:00",
                "2022-11-08 01:30:00",
                "2022-11-09 01:30:00",
                "2022-11-10 01:30:00",
                "2022-11-11 01:30:00",
                "2022-11-12 01:30:00",
                "2022-11-15 01:30:00",
                "2022-11-16 01:30:00",
                "2022-11-17 01:30:00",
                "2022-11-18 01:30:00",
                "2022-11-19 01:30:00",
                "2022-11-22 01:30:00",
                "2022-11-23 01:30:00",
                "2022-11-24 01:30:00",
            ],
            tz=tz_oz,
        )
        dti_oz = dti_utc.tz_convert(tz_oz)
        assert_index_equal(dti_oz, expected_oz)
        expected_oz_days = pd.Index(
            [
                datetime.date(2022, 11, 5),
                datetime.date(2022, 11, 8),
                datetime.date(2022, 11, 9),
                datetime.date(2022, 11, 10),
                datetime.date(2022, 11, 11),
                datetime.date(2022, 11, 12),
                datetime.date(2022, 11, 15),
                datetime.date(2022, 11, 16),
                datetime.date(2022, 11, 17),
                datetime.date(2022, 11, 18),
                datetime.date(2022, 11, 19),
                datetime.date(2022, 11, 22),
                datetime.date(2022, 11, 23),
                datetime.date(2022, 11, 24),
            ]
        )
        assert_index_equal(pd.Index(dti_oz.date), expected_oz_days)

        expected_us = pd.DatetimeIndex(
            [
                "2022-11-04 09:30:00",
                "2022-11-07 09:30:00",
                "2022-11-08 09:30:00",
                "2022-11-09 09:30:00",
                "2022-11-10 09:30:00",
                "2022-11-11 09:30:00",
                "2022-11-14 09:30:00",
                "2022-11-15 09:30:00",
                "2022-11-16 09:30:00",
                "2022-11-17 09:30:00",
                "2022-11-18 09:30:00",
                "2022-11-21 09:30:00",
                "2022-11-22 09:30:00",
                "2022-11-23 09:30:00",
            ],
            tz=tz_us,
        )
        dti_us = dti_utc.tz_convert(tz_us)
        assert_index_equal(dti_us, expected_us)
        expected_us_days = pd.Index(
            [
                datetime.date(2022, 11, 4),
                datetime.date(2022, 11, 7),
                datetime.date(2022, 11, 8),
                datetime.date(2022, 11, 9),
                datetime.date(2022, 11, 10),
                datetime.date(2022, 11, 11),
                datetime.date(2022, 11, 14),
                datetime.date(2022, 11, 15),
                datetime.date(2022, 11, 16),
                datetime.date(2022, 11, 17),
                datetime.date(2022, 11, 18),
                datetime.date(2022, 11, 21),
                datetime.date(2022, 11, 22),
                datetime.date(2022, 11, 23),
            ]
        )
        assert_index_equal(pd.Index(dti_us.date), expected_us_days)

        expected_hk = pd.DatetimeIndex(
            [
                "2022-11-04 21:30",
                "2022-11-07 22:30",
                "2022-11-08 22:30",
                "2022-11-09 22:30",
                "2022-11-10 22:30",
                "2022-11-11 22:30",
                "2022-11-14 22:30",
                "2022-11-15 22:30",
                "2022-11-16 22:30",
                "2022-11-17 22:30",
                "2022-11-18 22:30",
                "2022-11-21 22:30",
                "2022-11-22 22:30",
                "2022-11-23 22:30",
            ],
            tz=tz_hk,
        )
        dti_hk = dti_utc.tz_convert(tz_hk)
        assert_index_equal(dti_hk, expected_hk)
        expected_hk_days = expected_oz_days  # same, both should map to next day
        assert_index_equal(
            pd.Index(dti_hk.date + datetime.timedelta(1)), expected_hk_days
        )

        yield (
            tss,
            expected_us_days,
            expected_oz_days,
            expected_hk_days,
            expected_utc_days,
        )

    @pytest.fixture
    def quote(self):
        """Fictional mock OHLCV data for 14 datapoints.

        Yields both unordered data and dictionary representing expected
        order of return.
        """
        opens = list(range(2, 16))
        lows = list(range(1, 15))
        highs = list(range(4, 18))
        closes = list(range(3, 17))
        volumes = list(range(50, 64))
        data = {
            "volume": volumes,
            "close": closes,
            "open": opens,
            "high": highs,
            "low": lows,
        }
        expected = {
            "open": opens,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": volumes,
        }
        yield data, expected

    @pytest.fixture
    def adjclose(self):
        """Fictional mock adjclose data for 14 datapoints."""
        yield [i + 0.25 for i in range(3, 17)]

    @staticmethod
    def get_dividends(tss):
        """Get fictional mock dividends data for 2 timestamps of `tss`.

        Returns
        -------
        tuple[dict[str, dict[str, float | int]], list[float]]
            [0] dict[str, dict[str, float | int]]
                Mock data for symbol_data["events"]["dividends"]. Data
                includes dividends for two timestamps of `tss`.
            [1] list[float]
                Expected contents of dividends column of DataFrame created
                for `tss` and with data that includes [0].
        """
        indices = (2, 8)
        amount = 0.12
        d = {str(tss[i]): {"amount": amount, "date": tss[i]} for i in indices}
        expected = [amount if i in indices else float("nan") for i in range(14)]
        return d, expected

    @pytest.fixture
    def dividends_daily(self, timestamps_daily):
        """Mock data and expected col values for daily dividends.

        See `get_dividends.__doc__`
        """
        yield self.get_dividends(timestamps_daily[0])

    @staticmethod
    def get_splits(tss):
        """Get fictional mock splits data for 1 timestamps of `tss`.

        Returns
        -------
        tuple[dict[str, dict[str, int | str]], list[float]]
            [0] dict[str, dict[str, float | int]]
                Mock data for symbol_data["events"]["splits"]. Data
                includes splits for one timestamp of `tss`.
            [1] list[float]
                Expected contents of splits column of DataFrame created
                for `tss` and with data that includes [0].
        """
        indice = 11
        ts = tss[indice]
        d = {
            str(ts): {"data": ts, "numerator": 3, "denominator": 1, "splitRatio": "3:1"}
        }
        expected = [3 if i == indice else float("nan") for i in range(14)]
        return d, expected

    @pytest.fixture
    def splits_daily(self, timestamps_daily):
        """Mock data and expected col values for daily splits.

        See `get_splits.__doc__`
        """
        yield self.get_splits(timestamps_daily[0])

    @staticmethod
    def build_mock_data(
        tss, tz, quote, adjclose=None, splits=None, dividends=None, last_trade=None
    ):
        """Get mock data for a symbol from which to create dataframe.

        Return can be passed as `data` parameter of `history_dataframe`.
        """
        if last_trade is None:
            last_trade = 1669237204
            expected_ts = pd.Timestamp("2022-11-23 21:00:04", tz="UTC")
            assert pd.Timestamp.fromtimestamp(last_trade, tz="UTC") == expected_ts
        meta = {
            "regularMarketTime": last_trade,
            "exchangeTimezoneName": tz,
        }

        indicators = {"quote": [quote.copy()]}
        if adjclose is not None:
            indicators["adjclose"] = [{"adjclose": adjclose}]

        events = {"fake_event": {"1667568600": {"fake_event_key": 66.6}}}
        for key, event_data in zip(("dividends", "splits"), (dividends, splits)):
            if event_data is None:
                continue
            events[key] = event_data

        return dict(meta=meta, indicators=indicators, timestamp=tss, events=events)

    @staticmethod
    def create_expected(expected_index, quote, dividends, splits, adjclose=None):
        """Create expected return from column parts."""
        df = pd.DataFrame(quote, index=expected_index)
        if adjclose is not None:
            df["adjclose"] = adjclose
        df["dividends"] = dividends
        df["splits"] = splits
        return df

    @staticmethod
    def verify_expected_daily_row_11(df, indice):
        """Hard coded sanity check on specific row of expected dataframe."""
        i = 11
        expected = pd.Series(
            dict(open=13, high=15, low=12, close=14, volume=61, adjclose=14.25),
            name=indice,
        )
        assert_series_equal(df.iloc[i].iloc[:-2], expected)
        assert pd.isna(df.iloc[i].iloc[-2])  # no dividends
        assert df.iloc[i].iloc[-1] == 3  # splits
        return df

    @pytest.fixture
    def expected_daily_utc(
        self, timestamps_daily, quote, dividends_daily, splits_daily, adjclose
    ):
        """Expected return if timestamps interpreted with local tz as utc."""
        df = self.create_expected(
            timestamps_daily[4], quote[1], dividends_daily[1], splits_daily[1], adjclose
        )
        self.verify_expected_daily_row_11(df, datetime.date(2022, 11, 22))
        yield df

    @pytest.fixture
    def expected_daily_us(
        self, timestamps_daily, quote, dividends_daily, splits_daily, adjclose
    ):
        """Expected return if timestamps interpreted with local tz as us."""
        df = self.create_expected(
            timestamps_daily[1], quote[1], dividends_daily[1], splits_daily[1], adjclose
        )
        self.verify_expected_daily_row_11(df, datetime.date(2022, 11, 21))
        yield df

    @pytest.fixture
    def expected_daily_us_bare(self, timestamps_daily, quote):
        """As `expected_daily_us` with only ohlcv columns."""
        df = pd.DataFrame(quote[1], index=timestamps_daily[1])
        # Hard coded sanity check for specific row
        i = 11
        expected = pd.Series(
            dict(open=13, high=15, low=12, close=14, volume=61),
            name=datetime.date(2022, 11, 21),
        )
        assert_series_equal(df.iloc[i], expected)
        yield df

    @pytest.fixture
    def expected_daily_oz(
        self, timestamps_daily, quote, dividends_daily, splits_daily, adjclose
    ):
        """Expected return if timestamps interpreted with local tz as oz."""
        df = self.create_expected(
            timestamps_daily[2], quote[1], dividends_daily[1], splits_daily[1], adjclose
        )
        self.verify_expected_daily_row_11(df, datetime.date(2022, 11, 22))
        yield df

    @pytest.fixture
    def expected_daily_hk(
        self, timestamps_daily, quote, dividends_daily, splits_daily, adjclose
    ):
        """Expected return if timestamps interpreted with local tz as oz."""
        df = self.create_expected(
            timestamps_daily[3], quote[1], dividends_daily[1], splits_daily[1], adjclose
        )
        self.verify_expected_daily_row_11(df, datetime.date(2022, 11, 22))
        yield df

    def test_daily(
        self,
        timestamps_daily,
        quote,
        adjclose,
        dividends_daily,
        splits_daily,
        expected_daily_utc,
        expected_daily_us,
        expected_daily_oz,
        expected_daily_hk,
        utc,
        tz_us,
        tz_oz,
        tz_hk,
    ):
        """Test for expected returns for mock data reflecting a daily period."""

        def f(data, adj_timezone):
            return history_dataframe(data, daily=True, adj_timezone=adj_timezone)

        tss = timestamps_daily[0]
        quote_, _ = quote
        adjclose_ = adjclose
        splits, _ = splits_daily
        dividends, _ = dividends_daily

        expecteds = (
            expected_daily_utc,
            expected_daily_us,
            expected_daily_oz,
            expected_daily_hk,
        )
        tzs = (utc, tz_us, tz_oz, tz_hk)
        for expected, tz in zip(expecteds, tzs):
            data = self.build_mock_data(tss, tz, quote_, adjclose_, splits, dividends)
            for adj_timezone in (True, False):
                # tz makes no difference as daily and there is no live indice
                rtrn = f(data, adj_timezone=adj_timezone)
                assert_frame_equal(rtrn, expected)

        # check effect if there are no dividends and/or splits
        expected = expected_daily_us
        tz = tz_us
        adj_timezone = False
        # no dividends
        dividends_srs = expected.pop("dividends")
        data = self.build_mock_data(tss, tz, quote_, adjclose_, splits=splits)
        rtrn = f(data, adj_timezone)
        assert_frame_equal(rtrn, expected)
        # no splits
        expected.pop("splits")
        expected["dividends"] = dividends_srs
        data = self.build_mock_data(tss, tz, quote_, adjclose_, dividends=dividends)
        rtrn = f(data, adj_timezone)
        assert_frame_equal(rtrn, expected)
        # neither dividends nor splits
        expected.pop("dividends")
        data = self.build_mock_data(tss, tz, quote_, adjclose_)
        rtrn = f(data, adj_timezone)
        assert_frame_equal(rtrn, expected)

    def test_live_indice(
        self, timestamps_daily, expected_daily_us_bare, tz_us, utc, quote
    ):
        """Test daily data with live indice."""
        live_indice = 1669231860
        expected_li_ts = pd.Timestamp("2022-11-23 19:31", tz="UTC")
        assert pd.Timestamp.fromtimestamp(live_indice, tz="UTC") == expected_li_ts

        tss, expected_days, *_ = timestamps_daily
        tss = tss[:-1]
        tss.append(live_indice)

        expected_df = expected_daily_us_bare
        data = self.build_mock_data(tss, tz_us, quote[0], last_trade=live_indice)

        # verify live indice has utc timezone when adj_timezone True
        rtrn = history_dataframe(data, daily=True, adj_timezone=False)
        expected_li = pd.Timestamp("2022-11-23 19:31", tz=utc).to_pydatetime()
        expected_index = expected_days[:-1]
        expected_index = expected_index.insert(len(expected_index), expected_li)
        expected_df.index = expected_index
        assert_frame_equal(rtrn, expected_df)

        # verify live indice has local timezone when adj_timezone True
        rtrn = history_dataframe(data, daily=True, adj_timezone=True)
        expected_li = pd.Timestamp("2022-11-23 14:31", tz=tz_us).to_pydatetime()
        expected_index = expected_index[:-1].insert(
            len(expected_index) - 1, expected_li
        )
        expected_df.index = expected_index
        assert_frame_equal(rtrn, expected_df)

    def test_duplicate_live_indice(
        self, timestamps_daily, expected_daily_us_bare, tz_us, quote
    ):
        """Test live indice removed if day already represented."""
        live_indice = 1669237204
        expected_li_ts = pd.Timestamp("2022-11-23 21:00:04", tz="UTC")
        assert pd.Timestamp.fromtimestamp(live_indice, tz="UTC") == expected_li_ts

        tss = timestamps_daily[0]
        # to get it all to fit to 14 indices, lose the first ts
        tss = tss[1:]
        tss.append(live_indice)

        data = self.build_mock_data(tss, tz_us, quote[0], last_trade=live_indice)
        rtrn = history_dataframe(data, daily=True, adj_timezone=False)

        # create expected
        expected_template = expected_daily_us_bare
        expected_index = expected_template.index[1:]
        assert expected_index[-1] == datetime.date(2022, 11, 23)
        # last row, live indice, expected to be removed as day already represented
        expected_df = expected_template[:-1]
        expected_df.index = expected_index
        assert_frame_equal(rtrn, expected_df)

    @pytest.fixture
    def timestamps_intraday(self, utc):
        """Timestamps representing fictional datetimes and expected mapped indices.

        Timestamps cover two days with change in DST observance.

        Yields
        -------
        tuple[list[int]
            [0] [list[int]]
                Unix timestamps, i.e. format as used by Yahoo API. Timestamps represent
                datetimes of hourly indices in terms of UTC.

            [1] pd.DatetimeIndex dtype 'datetime64[ns, UTC]'
                Expected indices that timestamps would map to if local timezone were
                'UTC'.
        """
        tss = [
            1667568600,
            1667572200,
            1667575800,
            1667579400,
            1667583000,
            1667586600,
            1667590200,
            1667831400,
            1667835000,
            1667838600,
            1667842200,
            1667845800,
            1667849400,
            1667853000,
        ]

        expected_index_utc = pd.DatetimeIndex(
            [
                "2022-11-04 13:30:00",
                "2022-11-04 14:30:00",
                "2022-11-04 15:30:00",
                "2022-11-04 16:30:00",
                "2022-11-04 17:30:00",
                "2022-11-04 18:30:00",
                "2022-11-04 19:30:00",
                "2022-11-07 14:30:00",
                "2022-11-07 15:30:00",
                "2022-11-07 16:30:00",
                "2022-11-07 17:30:00",
                "2022-11-07 18:30:00",
                "2022-11-07 19:30:00",
                "2022-11-07 20:30:00",
            ],
            tz=utc,
        )
        dti = pd.to_datetime(tss, unit="s")
        dti_utc = dti.tz_localize(utc)
        assert_index_equal(dti_utc, expected_index_utc)

        yield tss, expected_index_utc

    @pytest.fixture
    def dividends_intraday(self, timestamps_intraday):
        """Get mock data and expected col values for intraday dividends.

        The Yahoo API attaches any dividends to the first intraday indice
        of each session. This mock does not respect this alignment, which
        is inconsequential for the test purposes.

        See `get_dividends.__doc__`.
        """
        yield self.get_dividends(timestamps_intraday[0])

    @pytest.fixture
    def splits_intraday(self, timestamps_intraday):
        """Mock data and expected col values for intraday splits.

        The Yahoo API attaches any dividends to the first intraday indice
        of each session. This mock does not respect this alignment, which
        is inconsequential for the test purposes.

        See `get_splits.__doc__`.
        """
        yield self.get_splits(timestamps_intraday[0])

    @pytest.fixture
    def expected_intraday(
        self, timestamps_intraday, quote, dividends_intraday, splits_intraday
    ):
        """Expected return for intraday timestamps."""
        _, expected_utc = timestamps_intraday
        df = self.create_expected(
            expected_utc, quote[1], dividends_intraday[1], splits_intraday[1]
        )
        # hard coded sanity check on specific row
        i = 8
        expected = pd.Series(
            dict(open=10, high=12, low=9, close=11, volume=58, dividends=0.12),
            name=pd.Timestamp("2022-11-7 15:30", tz="UTC"),
        )
        assert_series_equal(df.iloc[i][:-1], expected)
        assert pd.isna(df.iloc[i][-1])
        yield df

    def test_intraday(
        self,
        timestamps_intraday,
        tz_us,
        quote,
        splits_intraday,
        dividends_intraday,
        expected_intraday,
    ):
        """Test for expected returns for mock data reflecting a daily period."""

        def f(data, adj_timezone):
            return history_dataframe(data, daily=False, adj_timezone=adj_timezone)

        tz = tz_us
        tss, _ = timestamps_intraday
        quote_, _ = quote
        splits, _ = splits_intraday
        dividends, _ = dividends_intraday

        data = self.build_mock_data(tss, tz, quote_, splits=splits, dividends=dividends)
        rtrn = f(data, adj_timezone=False)
        expected = expected_intraday
        assert_frame_equal(rtrn, expected)
        rtrn = f(data, adj_timezone=True)
        expected.index = expected.index.tz_convert(tz)
        assert_frame_equal(rtrn, expected)

        # no dividends
        dividends_srs = expected.pop("dividends")
        data = self.build_mock_data(tss, tz, quote_, splits=splits)
        rtrn = f(data, adj_timezone=True)
        assert_frame_equal(rtrn, expected)
        # no splits
        expected.pop("splits")
        expected["dividends"] = dividends_srs
        data = self.build_mock_data(tss, tz, quote_, dividends=dividends)
        rtrn = f(data, adj_timezone=True)
        assert_frame_equal(rtrn, expected)
        # neither dividends nor splits
        expected.pop("dividends")
        data = self.build_mock_data(tss, tz, quote_)
        rtrn = f(data, adj_timezone=True)
        assert_frame_equal(rtrn, expected)
