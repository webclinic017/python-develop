
from Binance.futures import Futures as Client
import json

api_key="iRgQ8jMcr1tUFOgtnKxtdLX20SUvt5buMHzm9RfXmsjDTL9TX6vfmNkPk7rcHw3U"


client=Client()

response=client.klines(symbol="BTCUSDT",interval="5m")
print(json.dumps(response,indent=2))