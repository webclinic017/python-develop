from Binance.Futures import Futures as Client
from Database.Database import Database as Database
import json
import datetime
import time
import mplfinance as mpf
import pandas as pd
import Plot

api_key="cuOeSnzS4BrI3PaCIwUT8fpdLfFIyq9v6PkydhYJKzFYfL51tfHlGn2Zrs2wDiD4"
secret_key="OoyaQE33YTNg2RZ4NazoboWo1NO3vgPHo3TrYunmTJS5MmaW6mI84xcOUTbY41D4"

symbol="ETHUSDT"
interval="5m"
client=Client(key=api_key,secret=secret_key)
Database=Database()

response=client.exchange_info()

symbols=response["symbols"]
onboardDate=1
for i in symbols:
    if i["symbol"] == "BTCUSDT":
        onboardDate=i["onboardDate"]

print(onboardDate)

startTime=onboardDate
table_klines_name="{}_KLINES_{}".format(symbol,interval)
if(Database.exist_table(table_name=table_klines_name)):
    startTime=Database.get_maxOpenTime(symbol=symbol,interval=interval)
    Database.delete_maxOpenTime(symbol=symbol,interval=interval,timestamp=startTime)
while(startTime<time.time()*1000):
    response=client.klines(symbol=symbol,interval=interval,startTime=startTime,limit=500)
    Database.insert_klines(symbol=symbol,interval=interval,klines=response)
    if(len(response)==1):
        break
    startTime = Database.get_maxOpenTime(symbol=symbol, interval=interval)
    Database.delete_maxOpenTime(symbol=symbol, interval=interval, timestamp=startTime)

klines=Database.select_klines(symbol=symbol,interval=interval,limit=400)


Plot.plot_K(klines,symbol=symbol)


