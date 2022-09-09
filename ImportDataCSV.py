import pandas as pd
import json
from datetime import datetime
import os

from ImportData import ImportData
from Сandle import Candle


class ImportDataCSV(ImportData):

    def __init__(self):
        super().__init__()
        self.source_csv = os.getcwd() + "\\csv\\Bitcoin Historical Data - Investing.com.csv"

    def get_data(self, start_time, end_time):
        csv_data = pd.read_csv(self.source_csv).to_json(orient="records")
        data_list = json.loads(csv_data)
        filter_data = [data for data in data_list if start_time < self.string_to_timestamp(data['Date']) < end_time]

        candle_list = []
        for candle_source in filter_data:
            candle = Candle(
                datetime.strptime(candle_source['Date'], '%b %d, %Y'),
                float(candle_source['Open'].replace(',', '')),
                float(candle_source['High'].replace(',', '')),
                float(candle_source['Low'].replace(',', '')),
                float(candle_source['Price'].replace(',', ''))
            )
            candle_list.append(candle)

        return candle_list

    @staticmethod
    def string_to_timestamp(datestr):
        tmstamp = datetime.strptime(datestr, '%b %d, %Y').timestamp() * 1000
        return tmstamp



