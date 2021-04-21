import time

import datetime
from pandas_datareader import data as pdr
from datetime import date
from datetime import datetime

import yfinance as yf
from pyspark.sql.functions import to_date

yf.pdr_override()
import pandas as pd

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list = ['LSPD.TO']
today = date.today()
#end_date = today - datetime.timedelta(days=10)

# We can get data by our choice by giving days bracket
#start_date = '17–01–01'
start_date = "1975-01-12"
end_date = "2021–04–20"

files = []

def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    print(today)
    dataname = ticker +str(today)
    files.append(dataname)
    SaveData(data, dataname)


# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv("C:\\finance_trading\\yahoo_data.csv")

# This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
    getData(tik)
for i in range(0, 100):
    df1 = pd.read_csv("C:\\finance_trading\\yahoo_data.csv")
    #print(df1.head())
    day_high = df1.High
    day_low = df1.Low
    trading_date = df1.Date
    diff_high_low = day_high - day_low
    #print(diff_high_low)
    

