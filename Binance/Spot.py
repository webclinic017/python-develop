from Binance.API import API
from Binance.utils import convert_list_to_json_array


class Spot(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if ("base_url" not in kwargs):
            kwargs["base_url"] = "https://api.binance.com"
            super().__init__(key, secret, **kwargs)

    # market
    def ping(self):
        url_path = "/api/v3/ping"
        return self.query(url_path)

    def time(self):
        url_path = "/api/v3/time"
        return self.query(url_path)

    def exchange_info(self, symbol=None, symbols=None):
        url_path = "/api/v3/exchangeInfo"
        params = {
            "symbol": symbol,
            "symbols": convert_list_to_json_array(symbols),
        }
        return self.query(url_path, params)

    def depth(self, symbol, **kwargs):
        url_path = "/api/v3/depth"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def trades(self, symbol, **kwargs):
        url_path = "/api/v3/trades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def historical_trades(self, symbol, **kwargs):
        url_path = "/api/v3/historicalTrades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def agg_trades(self, symbol, **kwargs):
        url_path = "/api/v3/aggTrades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def klines(self, symbol, interval, **kwargs):
        url_path = "/api/v3/klines"
        params = {
            "symbol": symbol,
            "interval": interval,
            **kwargs}
        return self.query(url_path, params)

    def avg_price(self, symbol):
        url_path = "/api/v3/avgPrice"
        params = {
            "symbol": symbol,
        }
        return self.query(url_path, params)

    def ticker_24hr(self, symbol=None, symbols=None):
        url_path = "/api/v3/ticker/24hr"
        params = {
            "symbol": symbol,
            "symbols": convert_list_to_json_array(symbols),
        }
        return self.query(url_path, params)

    def ticker_price(self, symbol=None, symbols=None):
        url_path = "/api/v3/ticker/price"
        params = {
            "symbol": symbol,
            "symbols": convert_list_to_json_array(symbols),
        }
        return self.query(url_path, params)

    def book_ticker(self, symbol=None, symbols=None):
        url_path = "/api/v3/ticker/bookTicker"
        params = {
            "symbol": symbol,
            "symbols": convert_list_to_json_array(symbols),
        }
        return self.query(url_path, params)

    def rolling_window_ticker(self, symbol=None, symbols=None, **kwargs):
        url_path = "/api/v3/ticker"
        params = {
            "symbol": symbol,
            "symbols": convert_list_to_json_array(symbols),
            **kwargs
        }
        return self.query(url_path, params)

    # trade
    def new_order(self, symbol, side, type, **kwargs):
        url_path = "/api/v3/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": type,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def cancel_order(self, symbol: str, **kwargs):
        url_path = "/api/v3/order"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE", url_path, params)

    def cancel_open_orders(self, symbol: str, **kwargs):
        url_path = "/api/v3/openOrders"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE", url_path, params)

    def get_order(self, symbol, **kwargs):
        url_path = "/api/v3/order"
        payload = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE", url_path, payload)

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
