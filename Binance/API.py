import requests
import hmac
import hashlib
from Binance.utils import cleanNoneValue
from Binance.utils import encoding_string
from Binance.utils import get_timestamp


class API(object):
    def __init__(self, key=None, secret=None, base_url=None):
        self.key = key
        self.secret = secret
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "binance-connector_Test",
                "X-MBX-APIKEY": key,
            }
        )

    def query(self, url_path, payload=None):
        return self.send_request("GET", url_path, payload=payload)

    def limit_request(self, http_method, url_path, payload=None):
        return self.send_request(http_method, url_path, payload)

    def sign_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        payload["timestamp"] = get_timestamp()
        query_string = self._prepare_params(payload)
        signature = self._get_sign(query_string)
        payload["signature"] = signature
        return self.send_request(http_method, url_path, payload)

    def send_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        url = self.base_url + url_path
        # print(url)
        params = cleanNoneValue({
            "url": url,
            "params": self._prepare_params(payload),
            # "timeout": self.timeout,
            # "proxies": self.proxies,
        })
        response = self._dispath_request(http_method)(**params)
        print(response.url)
        data = response.json()
        return data

    def _get_sign(self, data):
        m = hmac.new(self.secret.encode("utf-8"), data.encode("utf-8"), hashlib.sha256)
        return m.hexdigest()

    def _dispath_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _prepare_params(self, payload):
        return encoding_string(cleanNoneValue(payload))

