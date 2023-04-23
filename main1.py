from Strategy.Strategy import Strategy
import time
import pandas as pd
from Strategy.Plot import *
import numpy as np
import statsmodels.api as sm
import threading
from multiprocessing import Process
from multiprocessing import Pool


def main():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    symbol = "ETHUSDT"

    strategy = Strategy(key=api_key, secret=secret_key)
    # strategy.update_klines(symbol=symbol)
    limit = 1000
    interval = "30m"
    history = 9
    klines_temp, vol_price_temp = strategy.select_klines_vol_price(symbol=symbol, interval=interval,
                                                                   limit=limit * (1 + history))
    print(len(klines_temp))
    klines = []
    vol_price = []
    for i in range(len(klines_temp) - limit, len(klines_temp)):
        klines.append(klines_temp[i])
        vol_price.append(vol_price_temp[i])
    print("klines", len(klines), len(vol_price))
    strategy.plot_K_Resistence(klines=klines, symbol=symbol, save=False, price_vol=vol_price)


def main1(symbol, startTimestamp, plotFlag=False, save=True, update=False):
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    # symbol = "BTCUSDT"
    limit = 10000
    interval = "5m"
    # startTimestamp = 1672531200000
    strategy = Strategy(key=api_key, secret=secret_key)
    if (update):
        strategy.update_klines(symbol=symbol)
    select_klines = strategy.select_klines(symbol=symbol, limit=limit, interval=interval, startTimestamp=startTimestamp)
    klinesTemp = pd.DataFrame(select_klines, columns={"Open_time": 0, "Open": 1, "High": 2, "Low": 3,
                                                      "Close": 4, "Volume": 5, "Close_time": 6,
                                                      "Quote_asset_volume": 7, "taker_buy_volume": 8})
    klines = klinesTemp[["Open_time", "Open", "High", "Low", "Close", "Volume", "taker_buy_volume"]]
    show_data = klines.loc[:, ["Open_time", "Open", "High", "Low", "Close", "Volume"]]
    taker = 2 * klines["taker_buy_volume"] - klines["Volume"]
    takers = taker.cumsum()
    buy_taker = klines["taker_buy_volume"]
    sell_taker = klines["taker_buy_volume"] - klines["Volume"]
    buy_takers = buy_taker.cumsum().tolist()
    sell_takers = sell_taker.cumsum().tolist()
    if (plotFlag):
        # plot_Kline(klines=show_data,symbol=symbol,resistence=takers,save=save)
        pass
    strategy.plot_K_Vol_Price(klines=select_klines, symbol=symbol)
    return klines


def desc_num_feature(klines, feature_name, bins=4000, edgecolor='k', **kwargs):
    fig, ax = plt.subplots(figsize=(8, 4))
    plt.grid(c='g')
    plt.hist(klines[feature_name], bins=bins, edgecolor=edgecolor)
    ax.set_title(feature_name, size=15)
    plt.show()


class MyThreadUpdate(threading.Thread):
    def __init__(self, symbol):
        threading.Thread.__init__(self)
        self.symbol = symbol

    def run(self):
        main1(symbol=self.symbol, startTimestamp=None, update=True, save=False, plotFlag=False)


def showAll():
    api_key = "c9UnWFmWxaY9gSl0eZ3H9a3EeNNutBmy6F9JGb7HKalGdqKUA5xViSrCbqhe144v"
    secret_key = "zcrWtNNTIiv7ydHV82zM0mI0tDhcEn3AMDm0X5fvGD6ANppxdMjphLAaFaoneaoL"
    strategy = Strategy(key=api_key, secret=secret_key)
    symbols = strategy.get_prefers()
    threads = []
    for symbol in symbols:
        print("Plot klines:", symbol)
        threads.append(MyThreadUpdate(symbol))
    for t in threads:
        t.start()


if __name__ == "__main__":
    pd.options.display.max_columns = None
    start_time = time.time()

    klines = main1("BTCUSDT", startTimestamp=None, plotFlag=True, save=False, update=False)
    # print(klines)
    '''
    pools=Pool(20)
    for start in range(1577836800000, int(time.time() * 1000), 500 * 5 * 60 * 1000):
        #main1("ETHUSDT", startTimestamp=start,plotFlag=True,save=True)
        pools.apply_async(main1, args=("ETHUSDT", start,True,True))

    pools.close()
    pools.join()
    '''

    # showAll()

    end_time = time.time()
    print((int(end_time - start_time)) // 60, "min", (int(end_time - start_time)) % 60, "s")
