import pymysql
import datetime
import time

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
        for kline in klines:
            insert_sql="insert into {} values('{}',{},{},{},{},{},{},{},{});".format(table_name,self.to_datetime(kline[0]),kline[0],kline[1],kline[2],kline[3],kline[4],kline[5],kline[6],kline[7])
            self.cursor.execute(insert_sql)
        print("Insert klines success")

    def insert_order(self,symbol,interval,response):
        table_name = "{}_ORDER_{}".format(symbol, interval)
        exist = self.exist_table(table_name)
        if (not exist):
            self.new_table_orders(symbol, interval)
        insert_sql="insert into {} value('{}',{},{},'{}','{}',{},{})".format(table_name,self.to_datetime(int(response["updateTime"])),int(response["updateTime"]),int(response["orderId"]),response["positionSide"],response["side"],response["origQty"],response["price"])
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
        table_name="{}_TRADE".format(symbol)
        exist=self.exist_table(table_name)
        if(not exist):
            self.new_table_trades(symbol)
        #print(trade)
        insert_sql="insert into {} values ".format(table_name)
        length=len(trades)
        for i in range(length-1):
            trade=trades[i]
            insert_sql+="('{}',{},{},{},{},{},{}),".format(self.to_datetime(int(trade["time"])),trade["id"],trade["price"],trade["qty"],trade["quote_qty"],trade["time"],trade["is_buyer_maker"])
        trade = trades[length-1]
        insert_sql += "('{}',{},{},{},{},{},{});".format(self.to_datetime(int(trade["time"])), trade["id"],trade["price"], trade["qty"], trade["quote_qty"],trade["time"], trade["is_buyer_maker"])

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
        sql="create table {}_KLINES_{}(time timestamp,Open_time bigint primary key,Open double,High double,Low double,Close double,Volume double,Close_time bigint,Quote_asset_volume double);".format(symbol,interval)
        self.cursor.execute(sql)

    def new_table_orders(self,symbol,interval):
        sql="create table {}_ORDER_{}(time timestamp,updateTime bigint primary key,orderId bigint,positionSide varchar(20),side varchar(20),origQty float,price float);".format(symbol,interval)
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

    def select_trade(self,symbol,minqty=3000000):
        table_name = "{}_TRADE".format(symbol)
        sql = "select time,price,qty,quoteQty,isBuyerMaker from {} where quoteQty>{}".format(table_name,minqty)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        trades=[]
        for i in data:
            trades.append(list(i))
        return trades

    def select_trade_to_csv(self,symbol,minqty=100,limit=10000):
        table_name = "{}_TRADE".format(symbol)
        sql = "select ttime,price,qty,isBuyerMaker from {} where qty>{} order by ttime desc limit {}".format(table_name,minqty,limit)
        self.cursor.execute(sql)
        data = reversed(self.cursor.fetchall())
        trades=[]
        for i in data:
            trades.append(list(i))
        return trades

    def get_last_order(self,symbol,interval):
        table_name = "{}_ORDER_{}".format(symbol, interval)
        sql="select * from {} order by id desc limit 1".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results

    def get_last_trade(self,symbol):
        table_name = "{}_TRADE".format(symbol)
        sql = "select max(id) from {};".format(table_name)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results[0][0])
        return results[0][0]

    def get_maxOpenTime(self,symbol,interval):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        sql="select max(Open_time) from {};".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results[0][0]

    def to_datetime(self,timestamp)->(int):
        Time = datetime.datetime.utcfromtimestamp(timestamp // 1000 + 8 * 60 * 60)
        return Time




#select * from ethusdt_trade where qty<50 order by id desc limit 10;