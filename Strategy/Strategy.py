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
            response = self.futures.new_order(symbol=symbol, side="SELL", positionSide="SHORT", type=type,quantity=quantity, timeInForce="GTX", **kwargs)
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def close_short(self, symbol, type, quantity, **kwargs):
        if (type == "MARKET"):
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="SHORT", type=type,quantity=quantity, **kwargs)
            response["avgPrice"] = self.futures.query_order(symbol=symbol, orderId=response["orderId"])["avgPrice"]
        else:
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="SHORT", type=type, quantity=quantity,timeInForce="GTX",**kwargs)
        if (type == "MARKET" and not "code" in response.keys()):
            self.database.insert_order(response=response)
        return response

    def open_long(self,symbol,type,quantity,**kwargs):
        if(type=="MARKET"):
            response = self.futures.new_order(symbol=symbol, side="BUY", positionSide="LONG", type=type,quantity=quantity, **kwargs)
            response["avgPrice"]=self.futures.query_order(symbol=symbol,orderId=response["orderId"])["avgPrice"]
        else:
            response=self.futures.new_order(symbol=symbol,side="BUY",positionSide="LONG",type=type,quantity=quantity,timeInForce="GTX",**kwargs)
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
            response = self.futures.new_order(symbol=symbol, side="SELL", positionSide="LONG", type=type,quantity=quantity, timeInForce="GTX", **kwargs)
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
        #print(start_k)
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

    def update_load_klines(self,symbol):
        self.__update_load_klines_5m(symbol=symbol,interval="5m")

    def __update_load_klines_5m(self,symbol, interval,files_path="C:\\data"):
        string="open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,taker_buy_quote_volume,ignore\n"
        files = os.listdir(files_path)
        for file in files:
            file_path = files_path + "\\{}".format(file)
            print("load file:", file_path)
            line=""
            with open(file_path,"r+") as f:
                line=f.readline()
                f.seek(0,0)
                content = f.read()
                if(line != string):
                    f.seek(0, 0)
                    f.write(string+content)
            self.__load_klines_csv(file_path=file_path, symbol=symbol)

    def __load_klines_csv(self,file_path,symbol):
        last_kline = self.database.get_last_kline(symbol=symbol)
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            klines=[]
            for item in reader:
                if(int(item["open_time"])>last_kline):
                    kline=[]
                    for i in item.values():
                        kline.append(i)
                    kline.pop()
                    klines.append(kline)
            if(len(klines)!=0):
                self.database.insert_klines(symbol=symbol,interval="5m",klines=klines)


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

    def __load_trades_csv(self,file_path,symbol,minqty):
        i=1
        qty=minqty
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

    def load_files_trades(self,symbol,files_path="C:\\data",minqty=2):
        files = os.listdir(files_path)
        for file in files:
            file_path=files_path+"\\{}".format(file)
            print("load file:",file_path)
            self.__load_trades_csv(file_path=file_path,symbol=symbol,minqty=minqty)

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

    def depth(self,symbol,limit=100):
        response=self.futures.depth(symbol=symbol,limit=limit)
        return response

    def plot_Depth(self,depths,symbol):
        Plot.plot_Depth(depths=depths,symbol=symbol)

    def get_order_history(self,symbol,orderId,**kwargs):
        response=self.futures.query_order(symbol=symbol,orderId=orderId,**kwargs)
        return response

    def group_qty_sum(self, symbol):
        results=self.database.group_qty_sum(symbol)
        return results

    def plot_trades(self,symbol):
        results = self.group_qty_sum(symbol=symbol)
        dicts = {}
        for i in results:
            try:
                dicts[str(i[0])] = dicts[str(i[0])] + (i[2] if i[1] == '1' else -i[2])
            except:
                dicts[str(i[0])] = (i[2] if i[2] == 1 else -i[2])
        qtys = []
        nums = []
        for k, y in dicts.items():
            qtys.append(float(k))
            nums.append(y * float(k))
        plt.scatter(qtys, nums)
        plt.show()

    def get_klines_pandas(self,klines):
        n = len(klines)
        fields = "Open_time,Open,High,Low,Close,Volume,Close_time,Quote_asset_volume"
        coin_data = pd.DataFrame(klines, columns={"Open_time": 0, "Open": 1, "High": 2, "Low": 3,
                                                  "Close": 4, "Volume": 5, "Close_time": 6, "Quote_asset_volume": 7})
        show_data = coin_data.loc[:, ["Open_time", "Open", "High", "Low", "Close", "Volume"]]
        temp_data = show_data["Open_time"]
        for i in range(n):
            show_data.loc[i, "Open_time"] = datetime.datetime.utcfromtimestamp(
                temp_data[i] // 1000 + 8 * 60 * 60)  ### UTC时间加8小时
        show_data["Open_time"] = pd.to_datetime(show_data["Open_time"])
        show_data = show_data.set_index(["Open_time"], drop=True)
        return show_data
