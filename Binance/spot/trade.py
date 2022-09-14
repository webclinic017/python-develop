

def new_order(self,symbol,side,type,**kwargs):
    url_path = "/api/v3/order"
    params = {
        "symbol": symbol, 
        "side": side, 
        "type": type, 
        **kwargs
    }
    return self.sign_request("POST", url_path, params)

def cancel_order(self, symbol, **kwargs):
    url_path = "/api/v3/order"
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return self.sign_request("DELETE", url_path, payload)

def cancel_open_orders(self, symbol, **kwargs):
    url_path = "/api/v3/openOrders"
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return self.sign_request("DELETE", url_path, payload)

def get_order(self, symbol, **kwargs):
    url_path = "/api/v3/order"
    payload = {
        "symbol": symbol, 
        **kwargs
    }
    return self.sign_request("GET", url_path, payload)

def cancel_and_replace(self, symbol, side, type, cancelReplaceMode, **kwargs):
    url_path = "/api/v3/order/cancelReplace"
    params = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "cancelReplaceMode": cancelReplaceMode,
        **kwargs,
    }
    return self.sign_request("POST", url_path, params)

def get_open_orders(self, symbol, **kwargs):
    url_path = "/api/v3/openOrders"
    payload = {
        "symbol":symbol,
        **kwargs
    }
    return self.sign_request("GET", url_path, payload)

def get_orders(self, symbol, **kwargs):
    url_path = "/api/v3/allOrders"
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return self.sign_request("GET", url_path, payload)

def new_oco_order(self,symbol,side,quantity,price,stopPrice,**kwargs):
    url_path = "/api/v3/order/oco"
    params = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stopPrice": stopPrice,
        **kwargs,
    }
    return self.sign_request("POST", url_path, params)

def cancel_oco_order(self, symbol, **kwargs):
    url_path = "/api/v3/orderList"
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return self.sign_request("DELETE", url_path, payload)

def get_oco_order(self, **kwargs):
    url_path = "/api/v3/orderList"
    return self.sign_request("GET", url_path, {**kwargs})

def get_oco_orders(self, **kwargs):
    url_path = "/api/v3/allOrderList"
    return self.sign_request("GET", url_path, {**kwargs})

def get_oco_open_orders(self, **kwargs):
    url_path = "/api/v3/openOrderList"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    url_path = "/api/v3/account"
    return self.sign_request("GET", url_path, **kwargs)

def my_trades(self, symbol, **kwargs):
    url_path = "/api/v3/myTrades"
    payload = {
        "symbol": symbol,
        **kwargs
    }
    return self.sign_request("GET", url_path, payload)

def get_order_rate_limit(self, **kwargs):
    url_path = "/api/v3/rateLimit/order"
    return self.sign_request("GET", url_path, {**kwargs})