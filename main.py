
from Binance.futures import Futures as Client
import json

client=Client()

response=client.klines(symbol="BTCUSDT",interval="5m")
print(json.dumps(response,indent=2))