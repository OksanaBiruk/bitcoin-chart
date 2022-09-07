from datetime import datetime


class Candle:

    def __init__(self, open_time: datetime, open_price: float, high_price: float, low_price: float, close_price: float):
        self.open_time = open_time
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.avg_price = (self.open_price + self.close_price)/2
