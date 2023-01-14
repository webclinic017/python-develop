import csv
from Database.Database import Database as Database
import time
import matplotlib.pyplot as plt
import numpy

Database=Database()

symbol="ETHUSDT"

trades=Database.select_trade(symbol=symbol,minqty=1000,desc=True,limit=100)

print(trades)

x=[]
y=[]
z=[]
length=len(trades)

for i in range(length):
    x.append(i)
    y.append(trades[i][1])
    if(trades[i][4]=='1'):
        z.append("green")
    else:
        z.append("red")

plt.scatter(x,y,c=z)
print(z)
plt.show()


