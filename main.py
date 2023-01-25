from Strategy.Strategy import Strategy
import json
import time

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
symbol="BTCUSDT"
strategy=Strategy(key=api_key,secret=secret_key)


#strategy.load_files_trades(symbol=symbol,minqty=2)
#strategy.update_trades(symbol=symbol)
strategy.plot_Trades_Scatter(symbol=symbol,minqty=50,limit=2000)

#strategy.update_klines(symbol=symbol)
#klines=strategy.select_klines(symbol=symbol,interval="15m",limit=300)
#strategy.plot_K(symbol=symbol,klines=klines)

'''
start=time.time()
depths=strategy.depth(symbol=symbol,limit=10)
bid=depths["bids"][6][0]
ask=depths["asks"][6][0]
#response=strategy.open_long(symbol=symbol,type="LIMIT",quantity=0.004,price=bid)
response=strategy.close_long(symbol=symbol,type="LIMIT",quantity=0.005,price=ask)
end=time.time()
print(end-start,"s")
print(json.dumps(response,indent=2))
'''

