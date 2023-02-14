import pandas as pd
import mplfinance as mpf
import datetime
import time
import matplotlib.pyplot as plt

def plot_K(klines,symbol="TEST",trades=None,addplot=None):
    n=len(klines)
    fields="Open_time,Open,High,Low,Close,Volume,Close_time,Quote_asset_volume"
    coin_data=pd.DataFrame(klines,columns={"Open_time":0,"Open":1,"High":2,"Low":3,
                                           "Close":4,"Volume":5,"Close_time":6,"Quote_asset_volume":7})
    show_data=coin_data.loc[:,["Open_time","Open","High","Low","Close","Volume"]]
    temp_data=show_data["Open_time"]
    for i in range(n):
        show_data.loc[i,"Open_time"]=datetime.datetime.utcfromtimestamp(temp_data[i]//1000+8*60*60)    ### UTC时间加8小时
    show_data["Open_time"]=pd.to_datetime(show_data["Open_time"])
    show_data=show_data.set_index(["Open_time"],drop=True)
    if(addplot==None):
        mpf.plot(show_data, type="candle", style="yahoo", volume=True, title=symbol + "-Perpetual")
    else:
        mpf.plot(show_data,type="candle",style="yahoo",volume=True,title=symbol+"-Perpetual",addplot=addplot)

def plot_Depth(depths,symbol="TEST"):
    bid_prices=[]
    bid_vols=[]
    ask_prices = []
    ask_vols = []
    for bid in depths["bids"]:
        bid_prices.append(float(bid[0]))
        bid_vols.append(float(bid[1]))
        if (len(bid_vols) != 0):
            bid_vols[len(bid_vols) - 1] += bid_vols[len(bid_vols) - 2]
    bid_prices.reverse()
    bid_vols.reverse()
    for ask in depths["asks"]:
        ask_prices.append(float(ask[0]))
        ask_vols.append(float(ask[1]))
        if (len(ask_vols) != 0):
            ask_vols[len(ask_vols) - 1] += ask_vols[len(ask_vols) - 2]
    plt.plot(bid_prices,bid_vols,color='g')
    plt.plot(ask_prices, ask_vols, color='r')
    plt.title(symbol+" bid : "+str(bid_prices[len(bid_prices)-1])+" ask : "+str(ask_prices[0]))
    plt.show()

def todate(timestamp):
    timeArray = time.localtime(timestamp / 1000)
    otherStyleTime = time.strftime("%m-%d-%H:%M", timeArray)
    return otherStyleTime

def plot_open_interest(datas,symbol):
    n=len(datas)
    times = []
    sumInterest = []
    interestValue = []
    for data in datas:
        times.append(todate(data["time"]))
        sumInterest.append(data["sumOpenInterest"])
        interestValue.append(data["sumOpenInterestValue"])

    fig = plt.figure(figsize=(16, 9))
    ax1 = fig.add_subplot(111)

    ax1.set_title(symbol + "-openInterest")
    ax1.plot(times, sumInterest, c="green", label="sumOpenInterest")
    ax1.legend(loc=2)
    ax1.set_ylabel("sumOpenInterest")

    ax2 = ax1.twinx()
    ax2.plot(times, interestValue, c='red', label="sumOpenInterestValue")
    ax2.legend(loc=1)
    ax2.set_ylabel("sumOpenInterestValue")
    ax2.set_xlabel("Time")

    ax1.set_xticks(times[::1])
    ax1.set_xticklabels(times, rotation=45)

    plt.xticks(fontsize=7)
    plt.xticks(rotation=45)
    plt.xticks(range(0, n, n // 20))
    plt.show()

def plot_top_trader_ratio_accounts(datas,symbol):
    n=len(datas)
    '''for i in datas:
        print(i)'''
    times=[]
    long_account=[]
    short_account=[]
    long_short_ratio=[]
    for i in datas:
        times.append(todate(i["timestamp"]))
        long_account.append(i["longAccount"])
        short_account.append(i["shortAccount"])
        long_short_ratio.append(i["longShortRatio"])

    fig = plt.figure(figsize=(16, 9))
    ax1 = fig.add_subplot(111)

    ax1.set_title(symbol + "-top_trader_ratio_accounts")
    ax1.set_ylim(ymin=0,ymax=1)
    ax1.plot(times, long_account, c="green", label="long_account")
    ax1.plot(times, short_account, c="red", label="short_account")
    ax1.legend(loc=2)
    ax1.set_ylabel("long_short")

    ax2 = ax1.twinx()
    ax2.plot(times, long_short_ratio, c='blue', label="long_short_ratio")
    ax2.legend(loc=1)
    ax2.set_ylabel("long_short_ratio")
    ax2.set_xlabel("Time")

    ax1.set_xticks(times[::1])
    ax1.set_xticklabels(times, rotation=45)

    plt.xticks(fontsize=7)
    plt.xticks(rotation=45)
    plt.xticks(range(0, n, n // 20))
    plt.show()


def plot_taker_buy_sell_volume(datas,symbol):
    n=len(datas)
    buy_vol=[]
    sell_vol=[]
    times=[]
    for i in datas:
        buy_vol.append(i["buyVol"])
        sell_vol.append(i["sellVol"])
        times.append(todate(i["timestamp"]))
    fig = plt.figure(figsize=(16, 9))
    ax1 = fig.add_subplot(111)
    ax1.set_title(symbol + "-taker_buy_sell_volume")

    ax1.plot(times, buy_vol, c="green", label="Buy")
    ax1.plot(times, sell_vol, c="red", label="Sell")
    ax1.legend(loc=2)
    ax1.set_ylabel("Vol")

    plt.xticks(fontsize=7)
    plt.xticks(rotation=45)
    plt.xticks(range(0, n, n // 20))
    plt.show()

def plot_ma(close_ma,open_ma,times,intRes=3):
    start = 0
    n = len(times)
    for i in range(n):
        if ((times[i] // 1000) % (24 * 60 * 60) == 0):
            start = i
    start = start % intRes
    # print(todate(times[start]))
    end_n = (n - start) % intRes
    ma_res_close = []
    ma_res_open = []
    time_x = []
    close_price = []
    # print((n-start)//intRes,len(close_ma),len(open_ma))
    temp_n = len(close_ma)
    if (end_n != 0):
        temp_n -= 1
    for i in range(temp_n):
        for j in range(intRes):
            ma_res_close.append(close_ma[i])
            ma_res_open.append(open_ma[i])
    for i in range(end_n):
        ma_res_close.append(close_ma[-1])
        ma_res_open.append(open_ma[-1])
    for i in range(n):
        time_x.append(todate(times[i]))


    time_x=time_x[len(time_x)-len(ma_res_close):]
    #print(time_x[-1])
    fig = plt.figure(figsize=(16, 9))
    ax1 = fig.add_subplot(111)
    ax1.set_title("MA-Security")

    ax1.plot(time_x, ma_res_close, c="green", label="Close")
    ax1.plot(time_x, ma_res_open, c="red", label="Open")
    ax1.legend(loc=2)
    ax1.set_ylabel("Price")

    plt.xticks(fontsize=7)
    plt.xticks(rotation=45)
    plt.xticks(range(0, n, n // 20))
    plt.show()
