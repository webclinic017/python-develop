import pymysql
import datetime
import time
from operator import itemgetter

class Database(object):
    def __init__(self,HOST="localhost",USER="root",PASSWORD="123456",database="data",charset="utf8",autocommit=True):
        self.host=HOST
        self.user=USER
        self.password=PASSWORD
        self.database=database
        self.charset=charset
        self.autocommit=autocommit
        self.db = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=database, charset=charset,autocommit=autocommit)
        self.cursor = self.db.cursor()

    def insert_klines(self,symbol,interval,klines):
        table_name="{}_KLINES_{}".format(symbol,interval)
        exist=self.exist_table(table_name)
        if(not exist):
            self.new_table_klines(symbol,interval)
        insert_sql = "insert into {} values ".format(table_name)
        length=len(klines)
        for i in range(length-1):
            kline=klines[i]
            insert_sql+="('{}',{},{},{},{},{},{},{},{},{},{},{}),".format(self.to_datetime(kline[0]),kline[0],kline[1],kline[2],kline[3],kline[4],kline[5],kline[6],kline[7],kline[8],kline[9],kline[10])
        #print(length)
        kline = klines[length-1]
        insert_sql += "('{}',{},{},{},{},{},{},{},{},{},{},{});".format(self.to_datetime(kline[0]), kline[0], kline[1],kline[2], kline[3], kline[4], kline[5],kline[6], kline[7], kline[8], kline[9],kline[10])
        self.cursor.execute(insert_sql)
        print("Insert klines success")

    def insert_order(self,response):
        table_name = "ORDERS"
        exist = self.exist_table(table_name)
        if (not exist):
            self.new_table_orders()
        insert_sql="insert into {} values('{}',{},'{}','{}','{}','{}','{}',{},{},{})".format(table_name,self.to_datetime(int(response["updateTime"])),int(response["updateTime"]),response["symbol"],response["orderId"],response["clientOrderId"],response["positionSide"],response["side"],response["origQty"],response["price"],response["avgPrice"])
        #print(insert_sql)
        self.cursor.execute(insert_sql)

    def insert_trades(self,symbol,trades):
        table_name="{}_TRADE".format(symbol)
        exist=self.exist_table(table_name)
        if(not exist):
            self.new_table_trades(symbol)
        #print(trades)
        for trade in trades:
            #print(trade)
            insert_sql="insert into {} values('{}',{},{},{},{},{},{});".format(table_name,self.to_datetime(trade["time"]),trade["id"],trade["price"],trade["qty"],trade["quoteQty"],trade["time"],trade["isBuyerMaker"])
            self.cursor.execute(insert_sql)
        #print("Insert klines success")

    def batch_insert_trade(self,symbol,trades:list):
        if(len(trades)==0):
            print("Wrong")
            return
        table_name="{}_TRADE".format(symbol)
        exist=self.exist_table(table_name)
        if(not exist):
            self.new_table_trades(symbol)
        #print(trade)
        insert_sql="insert into {} values ".format(table_name)
        length=len(trades)
        for i in range(length-1):
            trade=trades[i]
            if("quote_qty" in trade.keys()):
                insert_sql+="('{}',{},{},{},{},{},{}),".format(self.to_datetime(int(trade["time"])),trade["id"],trade["price"],trade["qty"],trade["quote_qty"],trade["time"],trade["is_buyer_maker"])
            else:
                insert_sql += "('{}',{},{},{},{},{},{}),".format(self.to_datetime(int(trade["time"])), trade["id"],trade["price"], trade["qty"], trade["quoteQty"],trade["time"], trade["isBuyerMaker"])
        trade = trades[length-1]
        if("quote_qty" in trade.keys()):
            insert_sql += "('{}',{},{},{},{},{},{});".format(self.to_datetime(int(trade["time"])), trade["id"],trade["price"], trade["qty"], trade["quote_qty"],trade["time"], trade["is_buyer_maker"])
        else:
            insert_sql += "('{}',{},{},{},{},{},{});".format(self.to_datetime(int(trade["time"])), trade["id"],trade["price"], trade["qty"], trade["quoteQty"],trade["time"], trade["isBuyerMaker"])
        self.cursor.execute(insert_sql)


    def insert_trade(self,symbol,trade):
        table_name="{}_TRADE".format(symbol)
        exist=self.exist_table(table_name)
        if(not exist):
            self.new_table_trades(symbol)
        #print(trade)
        insert_sql="insert into {} values('{}',{},{},{},{},{},{});".format(table_name,self.to_datetime(int(trade["time"])),trade["id"],trade["price"],trade["qty"],trade["quote_qty"],trade["time"],trade["is_buyer_maker"])
        #insert_sql = "insert into {} values('{}',{},{},{},{},{},{});".format(table_name,
        #                                                                     self.to_datetime(int(trade["1654041602556"])),
         #                                                                    trade["1698207560"], trade["1941.68"], trade["0.592"],
         #                                                                    trade["1149.47"], trade["1654041602556"],
         #                                                                    trade["false"])
        try:
            self.cursor.execute(insert_sql)
        except Exception:
            1+1

    def count_trade(self,symbol,interval=10):
        sql = "select count(case when qty>=20 and qty<{} then 1 end) as \'20-{}\',".format(20+interval,20+interval)
        start=20+interval
        interval=interval*2
        while(True):
            sql=sql+("count(case when qty>={} and qty<{} then 1 end) as \'{}-{}\',".format(start,start+interval,start,start+interval))
            start+=interval
            interval=interval*2
            if(start>=5000):
                break
        sql=sql+"count(case when qty>={} then 1 end) as \'{}+\'".format(start,start)
        sql=sql+" from {}_TRADE;".format(symbol)
        #print(sql)
        start=time.time()
        self.cursor.execute(sql)
        end=time.time()
        print((end-start)/1000)
        data=list(self.cursor.fetchall()[0])
        print(data)
        return data

    def new_table_klines(self,symbol,interval):
        sql="create table {}_KLINES_{}(time timestamp,Open_time bigint primary key,Open double,High double,Low double,Close double,Volume double,Close_time bigint,Quote_asset_volume double,count int,taker_buy_volume double,taker_buy_quote_volume double);".format(symbol,interval)
        self.cursor.execute(sql)

    def new_table_orders(self):
        sql="create table ORDERS(time timestamp,updateTime bigint primary key,symbol varchar(20),orderId varchar(30),clientOrderId varchar(30),positionSide varchar(10),side varchar(10),origQty float,price float,avgPrice float);"
        self.cursor.execute(sql)

    def new_table_trades(self,symbol):
        sql="create table {}_TRADE(time timestamp,id bigint primary key,price float,qty float,quoteQty float,ttime bigint,isBuyerMaker varchar(20));".format(symbol)
        self.cursor.execute(sql)

    def exist_table(self,table_name):
        sql="SELECT count(*) FROM information_schema.TABLES WHERE table_name ='{}';".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()[0][0]
        return results==1

    def delete_maxOpenTime(self,symbol,interval,timestamp):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        sql="delete from {} where Open_time={}".format(table_name,timestamp)
        self.cursor.execute(sql)

    def select_klines(self,symbol,interval,limit):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        sql = "select Open_time,Open,High,Low,Close,Volume,Close_time,Quote_asset_volume from {} order by Open_time desc limit {}".format(table_name,limit)
        self.cursor.execute(sql)
        data=reversed(self.cursor.fetchall())
        klines=[]
        for i in data:
            klines.append(list(i))
        return klines

    def select_trade(self,symbol,minqty=300,desc=False,limit=100):
        if(desc==False):
            desc_f="ASC"
        else:
            desc_f="DESC"
        table_name = "{}_TRADE".format(symbol)
        sql = "select time,price,qty,quoteQty,isBuyerMaker from {} where qty>{} order by id {} limit {}".format(table_name,minqty,desc_f,limit)
        #print(sql)
        self.cursor.execute(sql)
        if(desc==True):
            data = reversed(self.cursor.fetchall())
        else:
            data = self.cursor.fetchall()
        trades=[]
        for i in data:
            trades.append(list(i))
        return trades

    def get_tardes_limit(self,symbol,starttime,count):
        symbol="ETHUSDTTEST"
        table_name = "{}_TRADE".format(symbol)
        sql = "select ttime,price,qty,isBuyerMaker from {} where ttime>{} order by qty desc limit {}".format(table_name, starttime,count)
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        trades=[]
        for data in datas:
            trade=[]
            trade.append(data[0])
            trade.append(data[1])
            trade.append(data[2] if data[3]=='1' else -data[2])
            trades.append(trade)
        return sorted(trades,key=itemgetter(0))

    def select_trade_to_csv(self,symbol,minqty=100,limit=10000):
        table_name = "{}_TRADE".format(symbol)
        sql = "select ttime,price,qty,isBuyerMaker from {} where qty>{} order by ttime desc limit {}".format(table_name,minqty,limit)
        self.cursor.execute(sql)
        data = reversed(self.cursor.fetchall())
        trades=[]
        for i in data:
            trades.append(list(i))
        return trades

    def get_last_order(self,symbol):
        table_name = "ORDERS"
        sql="select * from {} where symbol='{}' order by updateTime desc limit 1".format(table_name,symbol)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return list(results[0])

    def get_last_kline(self,symbol,interval="5m"):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        if(not self.exist_table(table_name=table_name)):
            return 0
        sql = "select max(Open_time) from {};".format(table_name)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results[0][0])
        return results[0][0] if results[0][0]!=None else 0

    def get_last_trade(self,symbol):
        table_name = "{}_TRADE".format(symbol)
        if(not self.exist_table(table_name=table_name)):
            return 0
        sql = "select max(id) from {};".format(table_name)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results[0][0])
        return results[0][0] if results[0][0]!=None else 0

    def get_maxOpenTime(self,symbol,interval):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        sql="select max(Open_time) from {};".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results[0][0]

    def to_datetime(self,timestamp)->(int):
        timestamp=int(timestamp)
        Time = datetime.datetime.utcfromtimestamp(timestamp // 1000 + 8 * 60 * 60)
        return Time

    def group_qty_sum(self,symbol):
        sql="select qty,isBuyerMaker,count(*) from {}_trade group by qty,isBuyerMaker order by qty;".format(symbol)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results





#select * from ethusdt_trade where qty<50 order by id desc limit 10;