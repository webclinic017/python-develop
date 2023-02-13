import requests
from bs4 import BeautifulSoup

symbol="BTCUSDT"
interval="1m"
url="https://data.binance.vision/?prefix=data/futures/um/daily/klines/{}/{}/".format(symbol,interval)

print(url)
html=requests.get(url=url).text
print(html)
soup=BeautifulSoup(html,"html.parser")
for k in soup.find_all('a'):
    print(k)
