

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