import time
from urllib.parse import urlencode

def cleanNoneValue(d):
    out={}
    for i in d.keys():
        if d[i] is not None:
            out[i]=d[i]
    return out

def get_timestamp():
    return int(time.time()*1000)

def encoded_string(query):
    return urlencode(query)
