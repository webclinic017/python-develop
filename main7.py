import csv
from Database.Database import Database as Database
import time
import matplotlib.pyplot as plt
import numpy
import datetime
import pandas as pd

Database=Database()

symbol="ETHUSDT"

interval=10

sel=Database.select_trade_to_csv(symbol=symbol,minqty=70,limit=5000000)

times=[]
prices=[]
qtys=[]

for i in sel:
    ti=datetime.datetime.utcfromtimestamp(i[0]//1000+8*60*60)
    price=i[1]
    qty=i[2]
    if(i[3]=='0'):
        qty=-i[2]
    times.append(ti)
    prices.append(price)
    qtys.append(qty)

dataframe = pd.DataFrame({'time':times,'price':prices,'qty':qtys})

dataframe.to_csv("D:\\ETHUSDT.csv",index=False,sep=',')




