"""
This is example
"""
#pylint: disable=invalid-name

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")
start = dt.datetime(2007, 1, 1)
end = dt.datetime(2018, 1, 1)
#Get data from yahoo finance
#df = web.DataReader("0700.hk", "yahoo", start, end)
#df.to_csv("0700.csv")

#Read data from csv file
df = pd.read_csv("0700.csv", parse_dates=True, index_col=0)
df['Avg Price'] = (df['High'] + df['Low'] + df['Adj Close']) / 3
df['10MA'] = df['Adj Close'].rolling(window=10).mean()
df['20MA'] = df['Adj Close'].rolling(window=20).mean()
df['50MA'] = df['Adj Close'].rolling(window=50).mean()
df['250MA'] = df['Adj Close'].rolling(window=250).mean()
df = df.round(2)

df['SD'] = df['Avg Price'].rolling(window=20).std()
df['Middle'] = df['Avg Price'].rolling(window=20).mean()
df['Lower'] = df['Middle'] - 2 * df['SD']
df['Upper'] = df['Middle'] + 2 * df['SD']
print(df.tail(20))

print("Program finish without error.")
