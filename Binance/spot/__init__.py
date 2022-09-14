from Binance.api import API

class Spot(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.binance.com"
        super().__init__(key, secret, **kwargs)

    from Binance.spot.market import ping
    from Binance.spot.market import time
    from Binance.spot.market import exchange_info
    from Binance.spot.market import depth
    from Binance.spot.market import trades
    from Binance.spot.market import historical_trades
    from Binance.spot.market import agg_trades
    from Binance.spot.market import klines
    from Binance.spot.market import avg_price
    from Binance.spot.market import ticker_24hr
    from Binance.spot.market import ticker_price
    from Binance.spot.market import book_ticker
    from Binance.spot.market import rolling_window_ticker