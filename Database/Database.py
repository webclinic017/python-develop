import pymysql
import datetime

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

    def new_table_klines(self,symbol,interval):
        sql="create table {}_KLINES_{}(time timestamp,Open_time bigint primary key,Open double,High double,Low double,Close double,Volume double,Close_time bigint,Quote_asset_volume double);".format(symbol,interval)
        self.cursor.execute(sql)

    def new_table_orders(self,symbol,interval):
        sql="create table {}_ORDER_{}(time timestamp,updateTime bigint primary key,orderId bigint,positionSide varchar(20),side varchar(20),origQty float,price float);".format(symbol,interval)
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

    def get_last_order(self,symbol,interval):
        table_name = "{}_ORDER_{}".format(symbol, interval)
        sql="select * from {} order by id desc limit 1".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results

    def get_maxOpenTime(self,symbol,interval):
        table_name = "{}_KLINES_{}".format(symbol, interval)
        sql="select max(Open_time) from {};".format(table_name)
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results[0][0]

    def to_datetime(self,timestamp)->(int):
        Time = datetime.datetime.utcfromtimestamp(timestamp // 1000 + 8 * 60 * 60)
        return Time
