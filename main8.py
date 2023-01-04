from Binance.Futures import Futures as Client
import json

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"

client=Client(key=api_key,secret=secret_key)

info=client.exchange_info()["symbols"]

for i in info:
    response=client.change_leverage(symbol=i["symbol"],leverage=20)
    print(i["symbol"],response)






