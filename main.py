from Strategy.Strategy import Strategy
import json
import time
import matplotlib.pyplot as plt
import math

api_key="c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
secret_key="zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
symbol="ETHUSDT"
strategy=Strategy(key=api_key,secret=secret_key)


strategy.update_klines(symbol=symbol)
klines=strategy.select_klines(symbol=symbol,interval="1h",limit=400)
strategy.plot_K(symbol=symbol,klines=klines)
