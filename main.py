from Strategy.Strategy import Strategy
import json
import time
import matplotlib.pyplot as plt
import math
#import backtrader as bp

def load():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    symbol = "ETHUSDTTEST"
    strategy = Strategy(key=api_key, secret=secret_key)
    strategy.load_files_trades(symbol=symbol,minqty=0)

def load_klines():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    strategy = Strategy(key=api_key, secret=secret_key)
    symbols=strategy.get_symbols()
    symbol="ETHUSDT"
    interval="1m"
    strategy.update_load_klines(symbol=symbol,interval=interval)

def select_klines():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    strategy = Strategy(key=api_key, secret=secret_key)
    symbol = "ETHUSDT"
    interval = "1m"
    strategy.update_klines(symbol=symbol)
    klines=strategy.select_klines(symbol=symbol,interval=interval,limit=200)
    strategy.plot_K(klines=klines,symbol=symbol)

def main():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    symbol = "ETHUSDT"
    interval="15m"
    strategy = Strategy(key=api_key, secret=secret_key)
    #strategy.update_all_symbols_klines()
    #strategy.update_klines(symbol=symbol)
    limit=13*24*4
    klines=strategy.select_klines(symbol=symbol,interval=interval,limit=limit,startTimestamp=1675209600000)
    #strategy.plot_K(klines=klines,symbol=symbol)
    #print(klines)
    starttime=klines[0][0]
    endtime=starttime+strategy.count__klines(interval)*60*1000*limit
    trades=strategy.get_tardes_limit(symbol=symbol,starttime=starttime,endtime=endtime,count=1000)
    strategy.plot_K(klines=klines, symbol=symbol,trades=trades)

def main1():
    api_key = "pNn32OUxkScMve5fhJugP9b65nPhfcImnv0FuiVpxJ0IXxnrLxcRh2N0cE5kY9lM"
    secret_key = "yvtaF4cBNL8I3INbYrNvCGFlQPWrxNsKirveyVJeO7hdRRej5jFwoWOtdeXrveQW"
    symbol = "ETHUSDTTEST"
    interval = "15m"
    strategy = Strategy(key=api_key, secret=secret_key)

    strategy.plot_tarde_price(symbol=symbol)

if __name__=="__main__":
    start_time=time.time()
    #main()
    #load()
    #load_klines()
    #select_klines()
    main1()
    end_time=time.time()
    print((int(end_time-start_time))//60,"min",(int(end_time-start_time))%60,"s")