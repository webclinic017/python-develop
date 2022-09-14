
import hmac
import json
import hashlib
import requests

from Binance.utils import get_timestamp
from Binance.utils import cleanNoneValue
from Binance.utils import encoded_string

class API():
    def __init__(self,key=None,secret=None,base_url=None):
        self.key=key
        self.secret=secret
        self.session=requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "Binance-Test",
                "X-MBX-APIKEY": key,
            }
        )
        if(base_url):
            self.base_url=base_url

    def query(self,url_path,payload=None):
        return self.send_request("GET",url_path,payload=payload)

    def sign_request(self,http_method,url_path,payload=None):
        if payload is None:
            payload={}
        payload["timestamp"]=get_timestamp()
        query_string=self._prepare_params(payload)
        signature=self._get_sign(query_string)
        payload["signature"] = signature
        return self.send_request(http_method,url_path,payload)

    def send_request(self,http_method,url_path,payload=None):
        if payload is None:
            payload={}
        url=self.base_url+url_path
        params=cleanNoneValue(
            {
                "url":url,
                "params":self._prepare_params(payload)
            }
        )
        print(params)
        response=self._dispatch_request(http_method)(**params)
        data=response.json()
        return data

    def _dispatch_request(self, http_method):
        return {
            "GET":self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method,"GET")

    def _get_sign(self,data):
        m = hmac.new(self.secret.encode("utf-8"), data.encode("utf-8"), hashlib.sha256)
        return m.hexdigest()

    def _prepare_params(self, params):
        return encoded_string(cleanNoneValue(params))
