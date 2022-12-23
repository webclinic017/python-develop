from Binance.API import API
from Binance.utils import convert_list_to_json_array

class Futures(API):
    def __init__(self,key=None,secret=None,**kwargs):
        if("base_url" not in kwargs):
            kwargs["base_url"]="https://fapi.binance.com"
            super().__init__(key,secret,**kwargs)

    #market
    def ping(self):
        url_path="/fapi/v1/ping"
        return self.query(url_path)
    
    def time(self):
        url_path = "/fapi/v1/time"
        return self.query(url_path)

    def exchange_info(self):
        url_path = "/fapi/v1/exchangeInfo"
        return self.query(url_path)

    def depth(self,symbol,**kwargs):
        url_path = "/fapi/v3/depth"
        params={
            "symbol":symbol,
            **kwargs
        }
        return self.query(url_path,params)

    def trades(self,symbol,**kwargs):
        url_path = "/fapi/v3/trades"
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

    def klines(self, symbol, interval, **kwargs):
        url_path = "/fapi/v1/klines"
        params = {
            "symbol": symbol, 
            "interval": interval, 
            **kwargs
            }
        return self.query(url_path, params)

    def mark_price(self, symbol = None):
        url_path = "/fapi/v1/premiumIndex"
        params = {
        "symbol": symbol
        }
        return self.query(url_path, params)

    def funding_rate(self, symbol, **kwargs):
        url_path = "/fapi/v1/fundingRate"
        params = {
        "symbol": symbol,
        **kwargs
        }
        return self.query(url_path, params)

    def ticker_24hr_price_change(self, symbol = None):
        url_path = "/fapi/v1/ticker/24hr"
        params = {
        "symbol": symbol
        }
        return self.query(url_path, params)

    def ticker_price(self, symbol = None):
        url_path = "/fapi/v1/ticker/price"
        params = {
            "symbol": symbol
        }
        return self.query(url_path, params)

    def book_ticker(self, symbol = None):
        url_path = "/fapi/v1/ticker/bookTicker"
        params = {
            "symbol": symbol
        }
        return self.query(url_path, params)

    def open_interest(self, symbol):
        url_path = "/fapi/v1/openInterest"
        params = {
            "symbol": symbol
        }
        return self.query(url_path, params)

    def open_interest_hist(self, symbol, period, **kwargs):
        url_path = "/futures/data/openInterestHist"
        params = {
            "symbol": symbol,
            "period": period, 
            **kwargs
        }
        return self.query(url_path, params)

    def top_long_short_position_ratio(self, symbol, period, **kwargs):
        url_path = "/futures/data/topLongShortPositionRatio"
        params = {
            "symbol": symbol,
            "period": period, 
            **kwargs
        }
        return self.query(url_path, params)

    def long_short_account_ratio(self, symbol, period, **kwargs):
        url_path = "/futures/data/globalLongShortAccountRatio"
        params = {
            "symbol": symbol,
            "period": period, 
            **kwargs
        }
        return self.query(url_path, params)

    def top_long_short_account_ratio(self, symbol, period, **kwargs):
        url_path = "/futures/data/topLongShortAccountRatio"
        params = {
            "symbol": symbol,
            "period": period, 
            **kwargs
        }
        return self.query(url_path, params)

    def taker_long_short_ratio(self, symbol, period, **kwargs):
        url_path = "/futures/data/takerlongshortRatio"
        params = {
            "symbol": symbol,
            "period": period, 
            **kwargs
        }
        return self.query(url_path, params)
    
    #trade
    def new_order(self,symbol,side,type,**kwargs):
        url_path = "/api/v3/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": type,
            **kwargs
        }
        return self.sign_request("POST",url_path, params)

    def cancel_order(self, symbol: str, **kwargs):
        url_path = "/api/v3/order"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE",url_path, params)

    def cancel_open_orders(self, symbol: str, **kwargs):
        url_path = "/api/v3/openOrders"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE",url_path, params)

    def get_order(self, symbol, **kwargs):
        url_path = "/api/v3/order"
        payload = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE",url_path, payload)

    def cancel_and_replace(self, symbol, side, type, cancelReplaceMode, **kwargs):
        url_path = "/api/v3/order/cancelReplace"
        payload = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "cancelReplaceMode": cancelReplaceMode,
        **kwargs,
        }
        return self.sign_request("POST", url_path, payload)

    def get_open_orders(self, symbol=None, **kwargs):
        url_path = "/api/v3/openOrders"
        payload = {
        "symbol": symbol,
        **kwargs,
        }
        return self.sign_request("GET", url_path, payload)

    def get_orders(self, symbol, **kwargs):
        url_path = "/api/v3/allOrders"
        payload = {
        "symbol": symbol,
        **kwargs,
        }
        return self.sign_request("GET", url_path, payload)

    def account(self, **kwargs):
        url_path = "/api/v3/account"
        payload = {
        **kwargs,
        }
        return self.sign_request("GET", url_path, payload)

    def my_trades(self, symbol, **kwargs):
        url_path = "/api/v3/myTrades"
        payload = {
        "symbol": symbol,
        **kwargs,
        }
        return self.sign_request("GET", url_path, payload)

    def get_order_rate_limit(self, **kwargs):
        url_path = "/api/v3/rateLimit/order"
        payload = {
        **kwargs,
        }
        return self.sign_request("GET", url_path, payload)
        