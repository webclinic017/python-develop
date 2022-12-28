import csv
from Database.Database import Database as Database
import time

Database=Database()

symbol="ETHUSDT"


i=1
qty=0.002
#with open("E:\\data\\ETHUSDT-trades-2022-01.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-02.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-03.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-04.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-05.csv", "r", encoding="utf-8") as f:
with open("E:\\data\\ETHUSDT-trades-2022-06.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-07.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-08.csv","r",encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-09.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-10.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-11.csv", "r", encoding="utf-8") as f:
#with open("E:\\data\\ETHUSDT-trades-2022-12.csv", "r", encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for item in reader:
        #print(item)
        #break

        #if (float(item["0.002"]) >= 100):     #10000
        #if(float(item["0.071"])>=50 and float(item["0.071"])<100):     #28000
        if (float(item["0.592"]) >= 20 and float(item["0.592"]) < 100):  #199000

            i+=1
            Database.insert_trade(symbol=symbol,trade=item)
            if(i%1000==0):
                print("YES",i)
        #time.sleep(1)

#28000
#