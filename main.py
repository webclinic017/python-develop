from Binance.Futures import Futures as Client
import json

api_key="cuOeSnzS4BrI3PaCIwUT8fpdLfFIyq9v6PkydhYJKzFYfL51tfHlGn2Zrs2wDiD4"
secret_key="OoyaQE33YTNg2RZ4NazoboWo1NO3vgPHo3TrYunmTJS5MmaW6mI84xcOUTbY41D4"

client=Client(key=api_key,secret=secret_key)
#response=client.new_order(symbol="BTCUSDT",type="LIMIT",side="BUY",quantity=0.0015,price=10000,timeInForce="GTC")

#response=client.new_order(symbol="BTCUSDT",side="BUY",positionside="LONG",type="LIMIT",quantity=0.001,price=10000,timeInForce="GTC")
response=client.change_margin_type(symbol="BTCUSDT",marginType="CROSSED")
#response=client.cancel_order(symbol="BTCUSDT",orderId=101785723997)
print(json.dumps(response,indent=2))
