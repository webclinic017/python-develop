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

    #margin

    def margin_transfer(self, asset, amount, type, **kwargs):
        url_path = "/sapi/v1/margin/transfer"
        payload = {
            "asset": asset, 
            "amount": amount, 
            "type": type, 
            **kwargs
            }
        return self.sign_request("POST", url_path, payload)

    def margin_borrow(self, asset, amount, **kwargs):
        url_path = "/sapi/v1/margin/loan"
        payload = {
            "asset": asset, 
            "amount": amount, 
            **kwargs
            }
        return self.sign_request("POST", url_path, payload)

    def margin_repay(self, asset, amount, **kwargs):
        url_path = "/sapi/v1/margin/repay"
        payload = {
            "asset": asset, 
            "amount": amount, 
            **kwargs
            }
        return self.sign_request("POST", url_path, payload)

    def margin_asset(self, asset):
        url_path = "/sapi/v1/margin/asset"
        payload = {
            "asset": asset
            }
        return self.sign_request("GET", url_path, payload)

    def margin_pair(self, symbol):
        url_path = "/sapi/v1/margin/pair"
        payload = {
            "symbol": symbol
            }
        return self.sign_request("GET", url_path, payload)

    def margin_all_assets(self):
        url_path = "/sapi/v1/margin/allAssets"
        payload = {
            }
        return self.sign_request("GET", url_path, payload)

    def margin_all_pairs(self):
        url_path = "/sapi/v1/margin/allPairs"
        payload = {
            }
        return self.sign_request("GET", url_path, payload)

    def margin_pair_index(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/priceIndex"
        payload = {
            "symbol": symbol,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def new_margin_order(self, symbol, side, type, **kwargs):
        url_path = "/sapi/v1/margin/order"
        payload = {
            "symbol": symbol, 
            "side": side, 
            "type": type, 
            **kwargs
            }
        return self.sign_request("POST", url_path, payload)
    
    def cancel_margin_order(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/order"
        payload = {
            "symbol": symbol, 
            **kwargs
            }
        return self.sign_request("DELETE", url_path, payload)

    def margin_transfer_history(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/transfer"
        payload = {
            "asset": asset,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_load_record(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/loan"
        payload = {
            "asset": asset,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_repay_record(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/repay"
        payload = {
            "asset": asset,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_interest_history(self, **kwargs):
        url_path = "/sapi/v1/margin/interestHistory"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_force_liquidation_record(self, **kwargs):
        url_path = "/sapi/v1/margin/forceLiquidationRec"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_account(self, **kwargs):
        url_path = "/sapi/v1/margin/account"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_order(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/order"
        payload = {
            "symbol": symbol, 
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_open_orders(self, **kwargs):
        url_path = "/sapi/v1/margin/openOrders"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_open_orders_cancellation(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/openOrders"
        payload = {
            "symbol": symbol,
            **kwargs
            }
        return self.sign_request("DELETE", url_path, payload)

    def margin_all_orders(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/allOrders"
        payload = {
            "symbol": symbol,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_my_trades(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/myTrades"
        payload = {
            "symbol": symbol,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_max_borrowable(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/maxBorrowable"
        payload = {
            "asset": asset,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_max_transferable(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/maxTransferable"
        payload = {
            "asset": asset,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_transfer(self, asset, symbol, transFrom, transTo, amount, **kwargs):
        url_path = "/sapi/v1/margin/isolated/transfer"
        payload = {
            "asset": asset,
        "symbol": symbol,
        "transFrom": transFrom,
        "transTo": transTo,
        "amount": amount,
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_transfer_history(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/isolated/transfer"
        payload = {
        "symbol": symbol,
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_account(self, **kwargs):
        url_path = "/sapi/v1/margin/isolated/account"
        payload = {
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_pair(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/isolated/pair"
        payload = {
            "symbol": symbol,
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_all_pairs(self, **kwargs):
        url_path = "/sapi/v1/margin/isolated/allPairs"
        payload = {
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def toggle_bnbBurn(self, **kwargs):
        url_path = "/sapi/v1/bnbBurns"
        payload = {
        **kwargs,
            }
        return self.sign_request("POST", url_path, payload)

    def bnbBurn_status(self, **kwargs):
        url_path = "/sapi/v1/bnbBurn"
        payload = {
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def margin_interest_rate_history(self, asset, **kwargs):
        url_path = "/sapi/v1/margin/interestRateHistory"
        payload = {
            "asset": asset,
        **kwargs,
            }
        return self.sign_request("GET", url_path, payload)

    def cancel_isolated_margin_account(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/isolated/account"
        payload = {
            "symbol": symbol, 
            **kwargs
            }
        return self.sign_request("DELETE", url_path, payload)

    def enable_isolated_margin_account(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/isolated/account"
        payload = {
            "symbol": symbol, 
            **kwargs
            }
        return self.sign_request("POST", url_path, payload)

    def isolated_margin_account_limit(self, **kwargs):
        url_path = "/sapi/v1/margin/isolated/accountLimit"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_fee(self, **kwargs):
        url_path = "/sapi/v1/margin/crossMarginData"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_fee(self, **kwargs):
        url_path = "/sapi/v1/margin/isolatedMarginData"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def isolated_margin_tier(self, symbol, **kwargs):
        url_path = "/sapi/v1/margin/isolatedMarginTier"
        payload = {
            "symbol": symbol,
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_order_usage(self, **kwargs):
        url_path = "/sapi/v1/margin/rateLimit/order"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)

    def margin_dust_log(self, **kwargs):
        url_path = "/sapi/v1/margin/dribblet"
        payload = {
            **kwargs
            }
        return self.sign_request("GET", url_path, payload)