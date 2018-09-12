import datetime as dt
import csv
from pandas_datareader._utils import RemoteDataError
import pandas as pd
import pandas_datareader.data as web
import time

start = dt.datetime(2007, 1, 1)
end = dt.datetime(2018, 2, 19)

with open('const.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg[0])
        try:
            df = web.DataReader(reg[0], 'yahoo', start, end)
            df.to_csv('data/' + reg[0] + '.csv')
            print('---------')
        except RemoteDataError:
            continue