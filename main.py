
from Binance.futures import Futures as Client
import json

client=Client()

response=client.historical_trades(symbol="BTCUSDT")
print(json.dumps(response,indent=2))