import urllib.request as request
import json
import re

symbol="AVAXUSDT"
url="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/{}/5m/".format(symbol)
response=request.urlopen(url=url)
html=response.read().decode("utf-8")
print(json.dumps(html,indent=2))

reg=re.compile(r'<a href="https://data.binance.vision/data/futures/um/monthly/klines/AVAXUSDT/5m/AVAXUSDT-5m-2020-12.zip">AVAXUSDT-5m-2020-12.zip</a>',re.S)
items=re.findall(reg,html)
print(items)