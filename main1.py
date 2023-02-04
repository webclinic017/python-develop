import backtrader as bt
import pickle
from Strategy.Strategy import Strategy
import pandas as pd
import datetime

strategy=Strategy(key="TEST",secret="TEST")
symbol="BTCUSDT"

class SmaCross(bt.Strategy):
    def __init__(self):
        self.pfast=10
        self.pslow=30
        sma1=bt.ind.SMA(period=self.pfast)
        sma2=bt.ind.SMA(period=self.pslow)
        self.crossover=bt.ind.CrossOver(sma1,sma2)

    def next(self):
        if not self.position:
            if self.crossover[0]>0:
                self.buy()
        else:
            if self.crossover[0]<0:
                self.close()


class MYstrategy(bt.Strategy):
    params = dict(
        pfast=20,  # 快周期
        pslow=50)  # 慢周期

    def __init__(self):
        self.dataclose = self.datas[0].close
        # Order变量包含持仓数据与状态
        self.order = None
        # 初始化移动平均数据
        self.slow_sma = bt.indicators.SMA(self.datas[0],
                                          period=self.params.pslow)
        self.fast_sma = bt.indicators.SMA(self.datas[0],
                                          period=self.params.pfast)
        # backtrader内置函数，可以判断两线的交叉点
        self.crossover = bt.ind.CrossOver(self.fast_sma, self.fast_sma)

    # 订单相关
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # 主动买卖的订单提交或接受时  - 不触发
            return
        # 验证订单是否完成
        if order.status in [order.Completed]:
            self.bar_executed = len(self)
            # 重置订单
        self.order = None

    # next包含所有交易逻辑
    def next(self):
        # 检测是否有未完成订单
        if self.order:
            return
        # 验证是否有持仓
        if not self.position:
            # 如果没有持仓，寻找开仓信号
            # SMA快线突破SMA慢线
            if self.crossover > 0:
                self.order = self.buy()
            # SMA快线跌破SMA慢线
            elif self.crossover < 0:
                self.order = self.sell()
        else:
            # 如果已有持仓，寻找平仓信号，此地方选择10日之后平仓
            if len(self) >= (self.bar_executed + 10):
                self.order = self.close()


klines=strategy.select_klines(symbol=symbol,interval="1h",limit=1000)

show_data=strategy.get_klines_pandas(klines=klines)

#print(show_data)


cerebro=bt.Cerebro()
data=bt.feeds.PandasData(dataname=show_data)
cerebro.adddata(data)
cerebro.addstrategy(MYstrategy)
cerebro.broker.set_cash(1000000)
cerebro.broker.setcommission(0.0004)
cerebro.run()
cerebro.plot()