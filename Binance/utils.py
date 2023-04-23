import time
from urllib.parse import urlencode
import json


def get_timestamp():
    return int(time.time() * 1000)


def cleanNoneValue(d):
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def encoding_string(query):
    return urlencode(query)


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(" ", "")
