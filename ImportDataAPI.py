from ImportData import ImportData
from Сandle import Candle
import requests as r
import json
from datetime import datetime


class ImportDataAPI(ImportData):
    source_api_period: None
    list_avg_price = None

    def __init__(self):
        super().__init__()
        self.source_api_period = None
        self.source_api = 'https://api1.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d'

    def get_data(self, start_time, end_time):
        self.source_api_period = self.source_api + '&startTime=' + str(start_time) + '&endTime=' + str(end_time)
        api_data = r.get(self.source_api_period)
        data = json.loads(api_data.text)
        candle_list = []
        for candle_source in data:
            candle = Candle(
                datetime.fromtimestamp(candle_source[0] / 1000),
                float(candle_source[1]),
                float(candle_source[2]),
                float(candle_source[3]),
                float(candle_source[4])
            )
            candle_list.append(candle)

        return candle_list
