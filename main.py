from Strategy.Strategy import Strategy
import json
import time
import matplotlib.pyplot as plt
import math
#import backtrader as bp

def load():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    symbol = "BTCUSDT"
    strategy = Strategy(key=api_key, secret=secret_key)
    strategy.load_files_trades(symbol=symbol,minqty=0)

def main():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    symbol = "ETHUSDT"
    strategy = Strategy(key=api_key, secret=secret_key)
    #strategy.update_klines(symbol=symbol)
    klines=strategy.select_klines(symbol=symbol,interval="1h",limit=300)
    #strategy.plot_K(klines=klines,symbol=symbol)
    starttime=klines[0][0]
    trades=strategy.get_tardes_limit(symbol=symbol,starttime=starttime,count=100)
    strategy.plot_K(klines=klines, symbol=symbol,trades=trades)

if __name__=="__main__":
    start_time=time.time()
    main()
    #load()
    end_time=time.time()
    print((int(end_time-start_time))//60,"min",(int(end_time-start_time))%60,"s")