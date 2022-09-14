from Binance.api import API

class Spot(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.binance.com"
        super().__init__(key, secret, **kwargs)

    #market
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

    #trade
    from Binance.spot.trade import new_order
    from Binance.spot.trade import cancel_order
    from Binance.spot.trade import cancel_open_orders
    from Binance.spot.trade import get_order
    from Binance.spot.trade import cancel_and_replace
    from Binance.spot.trade import get_open_orders
    from Binance.spot.trade import get_order
    from Binance.spot.trade import new_oco_order
    from Binance.spot.trade import cancel_oco_order
    from Binance.spot.trade import get_oco_order
    from Binance.spot.trade import get_oco_orders
    from Binance.spot.trade import get_oco_open_orders
    from Binance.spot.trade import account
    from Binance.spot.trade import my_trades
    from Binance.spot.trade import get_order_rate_limit

    
