from Binance.Futures import Futures as Client
from Database.Database import Database as Database
import json

api_key="cuOeSnzS4BrI3PaCIwUT8fpdLfFIyq9v6PkydhYJKzFYfL51tfHlGn2Zrs2wDiD4"
secret_key="OoyaQE33YTNg2RZ4NazoboWo1NO3vgPHo3TrYunmTJS5MmaW6mI84xcOUTbY41D4"

client=Client(key=api_key,secret=secret_key)

response=client.exchange_info()


print(json.dumps(response,indent=2))
