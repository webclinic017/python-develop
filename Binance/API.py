import requests
from Binance.utils import cleanNoneValue
from Binance.utils import encoding_string

class API(object):
    def __init__(self,key=None,secret=None,base_url=None):
        self.key=key
        self.secret=secret
        self.base_url=base_url
        self.session=requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "binance-connector_Test",
                "X-MBX-APIKEY": key,
            }
        )

    def query(self,url_path,payload=None):
        return self.send_request("GET",url_path,payload=payload)

    def limit_request(self,http_method,url_path,payload=None):
        return self.send_request(http_method,url_path,payload)

    def send_request(self,http_method,url_path,payload=None):
        if payload is None:
            payload={}
        url=self.base_url+url_path
        print(url)
        params=cleanNoneValue({
            "url":url,
            "params":self._prepare_params(payload)
        })
        response=self._dispath_request(http_method)(**params)
        data=response.json()
        return data

    def _dispath_request(self,http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _prepare_params(self,payload):
        return encoding_string(cleanNoneValue(payload))

    