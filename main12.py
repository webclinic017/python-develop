from Strategy.Strategy import Strategy
import json
import os
import time

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"

strategy=Strategy(key=api_key,secret=secret_key)

symbol="BTCUSDT"
interval="4h"

strategy.update_klines(symbol=symbol)
klines=strategy.select_klines(symbol=symbol,interval=interval,limit=200)
##print(len(klines))
strategy.plot_K(klines=klines,symbol=symbol)

#strategy.update_klines(symbol=symbol,interval=interval)

#strategy.change_all_lever(leverage=20)

#strategy.write_datebase_to_csv(symbol=symbol,minqty=20,limit=1000)

#strategy.plot_Trades_Scatter(symbol=symbol,minqty=10,limit=200,desc=True)

#strategy.load_files_trades(symbol=symbol)

#response=strategy.open_short(symbol=symbol,type="MARKET",quantity=0.004)
#data=strategy.get_last_order(symbol=symbol)
#quantity=data[7]
#print(quantity)
#response=strategy.close_long(symbol=symbol,type="MARKET",quantity=quantity)
#response=strategy.query_order(symbol=symbol,orderId=8389765571918907148)
#print(json.dumps(response,indent=2))
#print(data)


#strategy.update_klines(symbol=symbol,interval=interval)
#klines=strategy.select_klines(symbol=symbol,interval=interval,limit=500)
#strategy.plot_K(klines,symbol=symbol)

'''
#order1=strategy.open_long(symbol=symbol,type="LIMIT",quantity=0.1,price=1200)
order1=strategy.cancel_order(symbol=symbol,orderId=8389765571905164419)
#order2=strategy.open_short(symbol=symbol,type="LIMIT",quantity=0.1,price=1700)
order2=strategy.cancel_order(symbol=symbol,orderId=8389765571905164839)
print(json.dumps(order1,indent=2))
print(json.dumps(order2,indent=2))
'''