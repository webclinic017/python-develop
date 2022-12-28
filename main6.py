import csv
from Database.Database import Database as Database
import time
import matplotlib.pyplot as plt
import numpy

Database=Database()

symbol="ETHUSDT"

interval=10

data=Database.count_trade(symbol=symbol,interval=interval)

x=[]
y=[]
length=len(data)
for i in range(length):
    x.append(i)
    y.append(data[i])

print(length)
plt.plot(x,y)

plt.show()




