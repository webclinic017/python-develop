
from Binance.spot import Spot as Client
import json

api_key="iRgQ8jMcr1tUFOgtnKxtdLX20SUvt5buMHzm9RfXmsjDTL9TX6vfmNkPk7rcHw3U"
secret_key="4JL7ODDj1kkJhovsRsj95soYvM4dQLcoUVr5S32p0bJu9KdYHsTRaW2Phf2OoaOC"


client=Client(key=api_key,secret=secret_key)

response = client.historical_trades(symbol="BTCUSDT",limit=1,fromId=1803836204)
print(json.dumps(response,indent=2))
