from Binance.utils import convert_list_to_json_array


def ping(self):
    url_path = "/api/v3/ping"
    return self.query(url_path)

def time(self):
    url_path = "/api/v3/time"
    return self.query(url_path)

def exchange_info(self):
    url_path = "/api/v3/exchangeInfo"
    return self.query(url_path)

def depth(self,symbol,**kwargs):
    url_path = "/api/v3/depth"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

#################################33
def trades(self,symbol,**kwargs):
    url_path = "/api/v3/trades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def historical_trades(self,symbol,**kwargs):
    url_path = "/api/v3/historicalTrades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def agg_trades(self,symbol,**kwargs):
    url_path = "/api/v3/aggTrades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def klines(self,symbol,interval,**kwargs):
    url_path = "/api/v3/klines"
    params={
        "symbol":symbol,
        "interval":interval,
        **kwargs
    }
    return self.query(url_path,params)

def avg_price(self,symbol):
    url_path = "/api/v3/avgPrice"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def ticker_24hr(self,symbol=None,symbols=None):
    url_path = "/api/v3/ticker/24hr"
    params={
        "symbol":symbol,
        "symbols": convert_list_to_json_array(symbols)
    }
    return self.query(url_path,params)

def ticker_price(self,symbol=None,symbols=None):
    url_path = "/api/v3/ticker/price"
    params={
        "symbol":symbol,
        "symbols": convert_list_to_json_array(symbols)
    }
    return self.query(url_path,params)

def book_ticker(self,symbol=None,symbols=None):
    url_path = "/api/v3/ticker/bookTicker"
    params={
        "symbol":symbol,
        "symbols": convert_list_to_json_array(symbols)
    }
    return self.query(url_path,params)

def rolling_window_ticker(self, symbol=None, symbols=None,**kwargs):
    url_path = "/api/v3/ticker"
    params={
        "symbol":symbol,
        "symbols": convert_list_to_json_array(symbols),
        **kwargs
    }
    return self.query(url_path,params)
