from Strategy.Strategy import Strategy
import json
import time
import matplotlib.pyplot as plt
import math
#import backtrader as bp

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
symbol="BTCUSDT"
strategy=Strategy(key=api_key,secret=secret_key)

#strategy.load_files_trades(symbol=symbol,minqty=0)


#strategy.update_load_klines(symbol=symbol)
strategy.update_klines(symbol=symbol)
klines=strategy.select_klines(symbol=symbol,interval="4h",limit=400)
#print(klines)
strategy.plot_K(symbol=symbol,klines=klines)
