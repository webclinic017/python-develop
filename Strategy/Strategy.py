from Binance.Futures import Futures
from Database.Database import Database
from . import Plot
import time
import json
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime
import pandas as pd

class Strategy(object):
    def __init__(self,key=None,secret=None,**kwargs):
        self.futures=Futures(key=key,secret=secret,**kwargs)
        self.database=Database()

    def get_last_order(self,symbol):
        data=self.database.get_last_order(symbol=symbol)
        return data

    def query_order(self, symbol, orderId=None, origClientOrderId=None, **kwargs):
        response=self.futures.query_order(symbol=symbol,orderId=orderId,origClientOrderId=origClientOrderId,**kwargs)
        return response

    def open_short(self,symbol,type,quantity,**kwargs):
        if (type == "MARKET"):
            response=self.futures.new_order(symbol=symbol,side="SELL",positionSide="SHORT",type=type,quantity=quantity,**kwargs)
            response["avgPrice"] = self.futures.query_order(symbol=symbol, orderId=response["orderId"])["avgPrice"]
        else:
            response = self.futures.new_order(symbol=symbol, side="SELL", positionSide="SHORT", type=type,quantity=quantity, timeInForce="GTC", **kwargs)
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def close_short(self, symbol, type, quantity, **kwargs):
        if (type == "MARKET"):
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="SHORT", type=type,quantity=quantity, **kwargs)
            response["avgPrice"] = self.futures.query_order(symbol=symbol, orderId=response["orderId"])["avgPrice"]
        else:
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="SHORT", type=type, quantity=quantity,timeInForce="GTC",**kwargs)
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def open_long(self,symbol,type,quantity,**kwargs):
        if(type=="MARKET"):
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="LONG", type=type,quantity=quantity, **kwargs)
            response["avgPrice"]=self.futures.query_order(symbol=symbol,orderId=response["orderId"])["avgPrice"]
        else:
            response=self.futures.new_order(symbol=symbol,side="BUY",positionSide="LONG",type=type,quantity=quantity,timeInForce="GTC",**kwargs)
        #print(json.dumps(response,indent=2))
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def close_long(self, symbol, type, quantity,**kwargs):
        if (type == "MARKET"):
            response = self.futures.new_order(symbol=symbol, side="SELL", positionSide="LONG", type=type, quantity=quantity,**kwargs)
            #print(json.dumps(response,indent=2))
            response["avgPrice"] = self.futures.query_order(symbol=symbol, orderId=response["orderId"])["avgPrice"]
        else:
            response = self.futures.new_order(symbol=symbol, side="SELL", positionSide="LONG", type=type,quantity=quantity, timeInForce="GTC", **kwargs)
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def cancel_order(self, symbol, orderId=None, origClientOrderId=None, **kwargs):
        response=self.futures.cancel_order(symbol=symbol,orderId=orderId,origClientOrderId=origClientOrderId,**kwargs)
        return response

    def plot_K(self,klines, symbol="TEST"):
        Plot.plot_K(klines=klines,symbol=symbol)

    def plot_Trades_Scatter(self,symbol,minqty=20, limit=200, desc=True):
        trades = self.database.select_trade(symbol=symbol, minqty=minqty, limit=limit, desc=desc)
        x = []
        y = []
        z = []
        length = len(trades)
        for i in range(0, length):
            x.append(i)
            y.append(trades[i][1])
            if (trades[i][4] == '1'):
                z.append("green")
            else:
                z.append("red")
        plt.scatter(x, y, c=z)
        #print(z)
        plt.show()

    def plot_date_trades(self, symbol, minqty=2, limit=200, desc=True):
        trades = self.database.select_trade(symbol=symbol, minqty=minqty, desc=desc, limit=limit)
        times = []
        price = []
        qty = []
        for trade in trades:
            times.append(trade[0])
            price.append(trade[1])
            temp = trade[2] if trade[4] == "1" else -trade[2]
            if (len(qty) == 0):
                qty.append(temp)
            else:
                qty.append(temp + qty[len(qty) - 1])
        print(trades[0][0])
        plt.plot_date(times, qty)
        plt.show()

    def select_klines(self,symbol,interval,limit):
        if(interval=="5m"):
            return self.database.select_klines(symbol,interval,limit)
        count=self.__count__klines(interval=interval)
        klines=self.database.select_klines(symbol=symbol,interval="5m",limit=limit*count)
        start_k=0
        for kline in klines:
            if((kline[0]//1000)%(24*60*60)==0):
                start_k=klines.index(kline)
                break
        start_k=start_k%count
        print(start_k)
        return_klines=[]
        for i in range(start_k,len(klines),count):
            temp=klines[i]
            for j in range(i+1,i+count if i+count<len(klines) else len(klines)):
                temp[5]+=klines[j][5]
                temp[7]+=klines[j][7]
                temp[2]=temp[2] if temp[2]>klines[j][2] else klines[j][2]
                temp[3] = temp[3] if temp[3] < klines[j][3] else klines[j][3]
                temp[4]=klines[j][4]
            temp[6]=temp[0]+count*(5*60*1000)-1
            return_klines.append(temp)
        return return_klines


    def __count__klines(self,interval):
        if(interval=="15m"):
            return 3
        elif(interval=="30m"):
            return 6
        elif (interval == "1h"):
            return 12
        elif (interval == "2h"):
            return 24
        elif (interval == "4h"):
            return 48
        elif (interval == "8h"):
            return 96
        elif (interval == "12h"):
            return 144
        elif (interval == "1d"):
            return 288
        else:
            return 1

    def update_klines(self,symbol):
        self.__update_klines_5m(symbol=symbol,interval="5m")

    def __update_klines_5m(self,symbol, interval, **kwargs):
        response = self.futures.exchange_info()
        symbols = response["symbols"]
        onboardDate = 1
        for i in symbols:
            if i["symbol"] == symbol:
                onboardDate = i["onboardDate"]
        startTime = onboardDate
        table_klines_name = "{}_KLINES_{}".format(symbol, interval)
        if (self.database.exist_table(table_name=table_klines_name)):
            startTime = self.database.get_maxOpenTime(symbol=symbol, interval=interval)
            self.database.delete_maxOpenTime(symbol=symbol, interval=interval, timestamp=startTime)
        while (startTime < time.time() * 1000):
            response = self.futures.klines(symbol=symbol, interval=interval, startTime=startTime, limit=500)
            self.database.insert_klines(symbol=symbol, interval=interval, klines=response)
            if (len(response) == 1):
                break
            startTime = self.database.get_maxOpenTime(symbol=symbol, interval=interval)
            self.database.delete_maxOpenTime(symbol=symbol, interval=interval, timestamp=startTime)

    def update_trades(self,symbol,minqty=2):
        startid = self.database.get_last_trade(symbol=symbol) + 1
        items = []
        while (True):
            response = self.futures.historical_trades(symbol=symbol, fromId=startid, limit=1000)
            if (len(response) == 0):
                break
            startid += 1000
            for item in response:
                if (float(item["qty"]) >= minqty):
                    items.append(item)
            print(len(items), items)
            if (len(items) == 0):
                continue
            self.database.batch_insert_trade(symbol=symbol, trades=items)
            items = []
            if (len(response) < 500):
                break

    def klines(self, symbol, interval, **kwargs):
        return self.futures.klines(symbol, interval, **kwargs)

    def get_symbols(self):
        response = self.futures.exchange_info()
        symbols = []
        for symbol in response["symbols"]:
            symbols.append(symbol["symbol"])
        return symbols

    def balance(self, **kwargs):
        responses=self.futures.balance()
        data=[]
        for response in responses:
            if(float(response["balance"])!=0):
                data.append(response)
        return data

    def account(self, **kwargs):
        responses=self.futures.account()
        data={}
        data["totalInitialMargin"]=responses["totalInitialMargin"]
        data["totalMaintMargin"]=responses["totalMaintMargin"]
        data["totalWalletBalance"]=responses["totalWalletBalance"]
        data["totalUnrealizedProfit"]=responses["totalUnrealizedProfit"]
        data["totalMarginBalance"]=responses["totalMarginBalance"]
        data["totalPositionInitialMargin"]=responses["totalPositionInitialMargin"]
        data["totalOpenOrderInitialMargin"]=responses["totalOpenOrderInitialMargin"]
        data["totalCrossWalletBalance"]=responses["totalCrossWalletBalance"]
        data["totalCrossUnPnl"]=responses["totalCrossUnPnl"]
        data["availableBalance"]=responses["availableBalance"]
        data["maxWithdrawAmount"]=responses["maxWithdrawAmount"]
        assets=[]
        for asset in responses["assets"]:
            if(float(asset["walletBalance"])!=0):
                assets.append(asset)
        data["assets"]=assets
        positions=[]
        for position in responses["positions"]:
            if(float(position["positionInitialMargin"])!=0):
                positions.append(position)
        data["positions"]=positions
        return data

    def __load_trades_csv(self,file_path,symbol):
        i=1
        qty=2
        flag=False
        last_trade=self.database.get_last_trade(symbol=symbol)
        #print(last_trade)
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            items = []
            for item in reader:
                if (float(item["qty"]) >= qty):
                    if(not flag and int(item["id"])>last_trade):
                        flag=True
                    elif(not flag):
                        continue
                    items.append(item)
                    #print(item)
                    i += 1
                    if (i % 10000 == 0):
                        self.database.batch_insert_trade(symbol=symbol, trades=items)
                        items = []
                        print("YES", i)
            if (len(items) != 0):
                self.database.batch_insert_trade(symbol=symbol, trades=items)
                print(file_path,"end",i,"\n")

    def load_files_trades(self,symbol,files_path="E:\\data"):
        files = os.listdir(files_path)
        for file in files:
            file_path=files_path+"\\{}".format(file)
            print("load file:",file_path)
            self.__load_trades_csv(file_path=file_path,symbol=symbol)

    def write_datebase_to_csv(self,symbol,minqty,limit,out_file="E:\\csv"):
        sel = self.database.select_trade_to_csv(symbol=symbol, minqty=minqty, limit=limit)
        times = []
        prices = []
        qtys = []
        for i in sel:
            ti = datetime.datetime.utcfromtimestamp(i[0] // 1000 + 8 * 60 * 60)
            price = i[1]
            qty = i[2]
            if (i[3] == '0'):
                qty = -i[2]
            times.append(ti)
            prices.append(price)
            qtys.append(qty)
        dataframe = pd.DataFrame({'time': times, 'price': prices, 'qty': qtys})
        out="{}\\{}.csv".format(out_file,symbol)
        dataframe.to_csv(out, index=False, sep=',')

    def change_all_lever(self,leverage=20):
        info = self.futures.exchange_info()["symbols"]
        for i in info:
            response = self.futures.change_leverage(symbol=i["symbol"], leverage=leverage)
            if('code' in response.keys()):
                response = self.futures.change_leverage(symbol=i["symbol"], leverage=leverage//2)
                if ('code' in response.keys()):
                    response = self.futures.change_leverage(symbol=i["symbol"], leverage=leverage//4)
            print(i["symbol"], response,len(info),info.index(i))