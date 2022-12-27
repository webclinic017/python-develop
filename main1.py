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

#    2584838691
symbol="ETHUSDT"
interval="5m"
client=Client(key=api_key,secret=secret_key)
Database=Database()

fromId=1
table_trade_name="{}_TRADE".format(symbol)
if(Database.exist_table(table_name=table_trade_name)):
    id=Database.get_last_trade(symbol=symbol)
    fromId=id+1
while(True):
    response=client.historical_trades(symbol=symbol,fromId=fromId,limit=1000)
    Database.insert_trades(symbol=symbol,trades=response)
    fromId=Database.get_last_trade(symbol=symbol)+1
