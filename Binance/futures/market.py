

def ping(self):
    url_path = "/fapi/v1/ping"
    return self.query(url_path)

def time(self):
    url_path = "/fapi/v1/time"
    return self.query(url_path)

def exchange_info(self):
    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)

def depth(self,symbol,**kwargs):
    url_path = "/fapi/v1/depth"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def trades(self,symbol,**kwargs):
    url_path = "/fapi/v1/trades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def historical_trades(self,symbol,**kwargs):
    url_path = "/fapi/v1/historicalTrades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def agg_trades(self,symbol,**kwargs):
    url_path = "/fapi/v1/aggTrades"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def klines(self,symbol,interval,**kwargs):
    url_path = "/fapi/v1/klines"
    params={
        "symbol":symbol,
        "interval":interval,
        **kwargs
    }
    return self.query(url_path,params)

def mark_price(self,symbol=None):
    url_path = "/fapi/v1/premiumIndex"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def funding_rate(self,symbol,**kwargs):
    url_path = "/fapi/v1/fundingRate"
    params={
        "symbol":symbol,
        **kwargs
    }
    return self.query(url_path,params)

def ticker_24hr_price_change(self,symbol=None):
    url_path = "/fapi/v1/ticker/24hr"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def ticker_price(self,symbol=None):
    url_path = "/fapi/v1/ticker/price"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def book_ticker(self,symbol=None):
    url_path = "/fapi/v1/ticker/bookTicker"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def open_interest(self,symbol):
    url_path = "/fapi/v1/openInterest"
    params={
        "symbol":symbol,
    }
    return self.query(url_path,params)

def open_interest_hist(self,symbol,interval,**kwargs):
    url_path = "/futures/data/openInterestHist"
    params={
        "symbol":symbol,
        "period":interval,
        **kwargs
    }
    return self.query(url_path,params)

def top_long_short_position_ratio(self,symbol,interval,**kwargs):
    url_path = "/futures/data/topLongShortPositionRatio"
    params={
        "symbol":symbol,
        "period":interval,
        **kwargs
    }
    return self.query(url_path,params)

def top_long_short_account_ratio(self,symbol,interval,**kwargs):
    url_path = "/futures/data/topLongShortAccountRatio"
    params={
        "symbol":symbol,
        "period":interval,
        **kwargs
    }
    return self.query(url_path,params)

def taker_long_short_ratio(self,symbol,interval,**kwargs):
    url_path = "/futures/data/takerlongshortRatio"
    params={
        "symbol":symbol,
        "period":interval,
        **kwargs
    }
    return self.query(url_path,params)