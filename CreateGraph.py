import matplotlib.dates
import matplotlib.pyplot as plt

from Сandle import Candle


class CreateGraph:
    graph = None

    def __init__(self):
        pass

    @classmethod
    def create_graph(cls, candle_list: list[Candle]):
        times = list(map(lambda n: n.open_time, candle_list))
        prices = list(map(lambda n: n.avg_price, candle_list))
        num = matplotlib.dates.date2num(times)
        plt.plot_date(num, prices)
        plt.ylabel('AVG kline price')
        plt.xlabel('Time')
        plt.title('Bitcoin price graph')
        cls.graph = plt.show()
