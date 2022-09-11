from Binance.api import API

class Futures(API):
    def __init__(self,key=None,secret=None,**kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"]="https://fapi.binance.com"
        super().__init__(key,secret,**kwargs)

    from Binance.futures.market import ping
    from Binance.futures.market import time
    from Binance.futures.market import exchange_info
    from Binance.futures.market import depth
    from Binance.futures.market import trades
    from Binance.futures.market import historical_trades

