from Binance.Futures import Futures as Client
import json
from Database.Database import Database

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"

symbol="ETHUSDT"
client=Client(key=api_key,secret=secret_key)
database=Database()

startid=database.get_last_trade(symbol=symbol)+1

items=[]
while(True):
    response=client.historical_trades(symbol=symbol,fromId=startid,limit=1000)
    if(len(response)==0):
        break
    startid+=1000
    for item in response:
        if (float(item["qty"]) >= 20):
            items.append(item)
    #print(response)
    print(len(items),items)
    if(len(items)==0):
        continue
    database.batch_insert_trade(symbol=symbol, trades=items)
    items = []
    if(len(response)<500):
        break







