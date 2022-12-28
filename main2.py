import csv
from Database.Database import Database as Database
import time
import matplotlib.pyplot as plt
import numpy

Database=Database()

symbol="ETHUSDT"

trades=Database.select_trade(symbol=symbol,minqty=2500000)

start=100
lever=3
x=[]
y=[]
pre=trades[0][4]
preprice=trades[0][1]
length=len(trades)
for i in range(1,length):
    x.append(i)
    if(pre==trades[i][4]):
        y.append(start)
        continue
    elif(pre==1 and trades[i][4]==0):
        start=start+start*(trades[i][1]/preprice-1-0.0004)*lever
        preprice=trades[i][1]
        pre = trades[i][4]
        y.append(start)
    else:
        start = start+start*( 1-trades[i][1] / preprice-0.0004)*lever
        preprice = trades[i][1]
        pre = trades[i][4]
        y.append(start)

plt.plot(x,y)

plt.show()


