from Binance.API import API
from Binance.utils import convert_list_to_json_array


class Futures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if ("base_url" not in kwargs):
            kwargs["base_url"] = "https://fapi.binance.com"
            super().__init__(key, secret, **kwargs)

    # market
    def ping(self):
        url_path = "/fapi/v1/ping"
        return self.query(url_path)

    def time(self):
        url_path = "/fapi/v1/time"
        return self.query(url_path)

    def exchange_info(self):
        url_path = "/fapi/v1/exchangeInfo"
        return self.query(url_path)

    def depth(self, symbol, **kwargs):
        url_path = "/fapi/v3/depth"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def trades(self, symbol, **kwargs):
        url_path = "/fapi/v3/trades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def historical_trades(self, symbol, **kwargs):
        url_path = "/fapi/v1/historicalTrades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def agg_trades(self, symbol, **kwargs):
        url_path = "/fapi/v1/aggTrades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.query(url_path, params)

    def klines(self, symbol, interval, **kwargs):
        url_path = "/fapi/v1/klines"
        params = {
            "symbol": symbol,
            "interval": interval,
            **kwargs
        }
        return self.query(url_path, params)

    def mark_price(self, symbol=None):
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

    def ticker_24hr_price_change(self, symbol=None):
        url_path = "/fapi/v1/ticker/24hr"
        params = {
            "symbol": symbol
        }
        return self.query(url_path, params)

    def ticker_price(self, symbol=None):
        url_path = "/fapi/v1/ticker/price"
        params = {
            "symbol": symbol
        }
        return self.query(url_path, params)

    def book_ticker(self, symbol=None):
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

    # account and trade

    def change_position_mode(self, dualSidePosition, **kwargs):
        url_path = "/fapi/v1/positionSide/dual"
        params = {
            "dualSidePosition": dualSidePosition,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def get_position_mode(self, **kwargs):
        url_path = "/fapi/v1/positionSide/dual"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def change_multi_asset_mode(self, multiAssetsMargin, **kwargs):
        url_path = "/fapi/v1/multiAssetsMargin"
        params = {
            "multiAssetsMargin": multiAssetsMargin,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def get_multi_asset_mode(self, **kwargs):
        url_path = "/fapi/v1/multiAssetsMargin"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def new_order(self, symbol, side, type, **kwargs):
        url_path = "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": type,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def new_batch_order(self, batchOrders: list):
        url_path = "/fapi/v1/batchOrders"
        params = {
            "batchOrders": batchOrders
        }
        return self.sign_request("POST", url_path, params)

    def query_order(self, symbol, orderId=None, origClientOrderId=None, **kwargs):
        url_path = "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "orderId": orderId,
            "origClientOrderId": origClientOrderId,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def cancel_order(self, symbol, orderId=None, origClientOrderId=None, **kwargs):
        url_path = "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "orderId": orderId,
            "origClientOrderId": origClientOrderId,
            **kwargs
        }
        return self.sign_request("DELETE", url_path, params)

    def cancel_open_orders(self, symbol, **kwargs):
        url_path = "/fapi/v1/allOpenOrders"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("DELETE", url_path, params)

    def cancel_batch_order(self, symbol, orderIdList: list = None, origClientOrderIdList: list = None, **kwargs):
        url_path = "/fapi/v1/batchOrders"
        params = {
            "symbol": symbol,
            "orderIdList": convert_list_to_json_array(orderIdList),
            "origClientOrderIdList": convert_list_to_json_array(origClientOrderIdList),
            **kwargs
        }
        return self.sign_request("DELETE", url_path, params)

    def get_open_orders(self, symbol, orderId=None, origClientOrderId=None, **kwargs):
        url_path = "/fapi/v1/openOrder"
        params = {
            "symbol": symbol,
            "orderId": orderId,
            "origClientOrderId": origClientOrderId,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def get_orders(self, **kwargs):
        url_path = "/fapi/v1/openOrders"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def get_all_orders(self, symbol: str, **kwargs):
        url_path = "/fapi/v1/allOrders"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def balance(self, **kwargs):
        url_path = "/fapi/v2/balance"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def account(self, **kwargs):
        url_path = "/fapi/v2/account"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def change_leverage(self, symbol, leverage, **kwargs):
        url_path = "/fapi/v1/leverage"
        params = {
            "symbol": symbol,
            "leverage": leverage,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def change_margin_type(self, symbol, marginType, **kwargs):
        url_path = "/fapi/v1/marginType"
        params = {
            "symbol": symbol,
            "marginType": marginType,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def modify_isolated_position_margin(self, symbol, amount, type, **kwargs):
        url_path = "/fapi/v1/positionMargin"
        params = {
            "symbol": symbol,
            "amount": amount,
            "type": type,
            **kwargs
        }
        return self.sign_request("POST", url_path, params)

    def get_position_margin_history(self, symbol, **kwargs):
        url_path = "/fapi/v1/positionMargin/history"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def get_position_risk(self, **kwargs):
        url_path = "/fapi/v2/positionRisk"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def get_account_trades(self, symbol, **kwargs):
        url_path = "/fapi/v1/userTrades"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def get_income_history(self, **kwargs):
        url_path = "/fapi/v1/income"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def leverage_brackets(self, **kwargs):
        url_path = "/fapi/v1/leverageBracket"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def adl_quantile(self, **kwargs):
        url_path = "/fapi/v1/adlQuantile"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def force_orders(self, **kwargs):
        url_path = "/fapi/v1/forceOrders"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def api_trading_status(self, **kwargs):
        url_path = "/fapi/v1/apiTradingStatus"
        params = {
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def commission_rate(self, symbol, **kwargs):
        url_path = "/fapi/v1/commissionRate"
        params = {
            "symbol": symbol,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def download_transactions_asyn(self, startTime, endTime, **kwargs):
        url_path = "/fapi/v1/income/asyn"
        params = {
            "startTime": startTime,
            "endTime": endTime,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)

    def aysnc_download_info(self, downloadId, **kwargs):
        url_path = "/fapi/v1/income/asyn/id"
        params = {
            "downloadId": downloadId,
            **kwargs
        }
        return self.sign_request("GET", url_path, params)
