
from Binance.spot import Spot as Client
import json

api_key="iRgQ8jMcr1tUFOgtnKxtdLX20SUvt5buMHzm9RfXmsjDTL9TX6vfmNkPk7rcHw3U"


client=Client(key=api_key)

response=client.rolling_window_ticker(symbol="BTCUSDT")
print(json.dumps(response,indent=2))