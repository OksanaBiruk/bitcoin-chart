import datetime
import time

from ImportDataAPI import ImportDataAPI
from CreateGraph import CreateGraph
from ImportDataCSV import ImportDataCSV

# choosing the source

source_API = 'API'
source_file = 'csv'
data_valid = False

while not data_valid:
    user_source = int(input('Hello! Do you want to see graph of Bitcoin price for some period?.'
                             'Input 1 if you want to load csv file or input 0 if you want to see data from Binance API: '))
    # user_source = 1  # fixme remove hardcode user_source = 0
    if user_source != 1 and user_source != 0:
        print("Invalid value. Enter 0 or 1")
        continue
    else:
        data_valid = True
        if user_source == 1:
            user_source = source_file
        else:
            user_source = source_API

# input the period

data_valid = False
while data_valid == False:
    start_date = input('Please, input the start date-time of the period for graph in format dd/mm/yyyy: ')
    # start_date = '01/05/2022'  # fixme remove hardcode start_date = '20/08/2022'
    try:
        start_timestamp = (int(time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple())) * 1000)
        # print(start_timestamp)
        data_valid = True
    except:
        data_valid = False
        print('Invalid format date!')

data_valid = False
while data_valid == False:
    end_date = input('Please, input the end date-time of the period for graph in format dd/mm/yyyy:')
    # end_date = '22/05/2022'  # fixme remove hardcode end_date = '25/08/2022'
    try:
        timetuple = datetime.datetime.strptime(end_date, "%d/%m/%Y").timetuple()
        end_timestamp = (int(time.mktime(timetuple)) * 1000)
        # print(end_timestamp)
        # data_valid = True
    except:
        data_valid = False
        print('Invalid format date!')
    else:
        if end_timestamp <= (int(time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple())) * 1000):
            print('The end date must be greater than the start date!')
            data_valid = False
        else:
            data_valid = True

if user_source == source_API:
    importData = ImportDataAPI()
else:
    importData = ImportDataCSV()

candle_list = importData.get_data(start_timestamp, end_timestamp)
# print(candle_list)

drawGraph = CreateGraph()
drawGraph.create_graph(candle_list)
