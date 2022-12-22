from Binance.Spot import Spot as Client
import json

api_key="iRgQ8jMcr1tUFOgtnKxtdLX20SUvt5buMHzm9RfXmsjDTL9TX6vfmNkPk7rcHw3U"
secret_key="4JL7ODDj1kkJhovsRsj95soYvM4dQLcoUVr5S32p0bJu9KdYHsTRaW2Phf2OoaOC"

temp=["BTCUSDT","ETHUSDT"]
res=json.dumps(temp)
print(res)


client=Client(key=api_key,secret=secret_key)
response=client.agg_trades(symbol="ETHUSDT")
print(response)
