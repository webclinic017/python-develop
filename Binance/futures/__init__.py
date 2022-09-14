from Binance.api import API


class Futures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    from Binance.futures.market import ping
    from Binance.futures.market import time
    from Binance.futures.market import exchange_info
    from Binance.futures.market import depth
    from Binance.futures.market import trades
    from Binance.futures.market import historical_trades
    from Binance.futures.market import agg_trades
    from Binance.futures.market import klines
    from Binance.futures.market import mark_price
    from Binance.futures.market import funding_rate
    from Binance.futures.market import ticker_24hr_price_change
    from Binance.futures.market import ticker_price
    from Binance.futures.market import book_ticker
    from Binance.futures.market import open_interest
    from Binance.futures.market import open_interest_hist
    from Binance.futures.market import top_long_short_position_ratio
    from Binance.futures.market import top_long_short_account_ratio
    from Binance.futures.market import taker_long_short_ratio



