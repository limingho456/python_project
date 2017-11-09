"""
This is example
"""
#pylint: disable=invalid-name

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from mpl_finance import candlestick2_ohlc

style.use("ggplot")
start = dt.datetime(2004, 1, 1)
end = dt.datetime(2018, 1, 1)
#Get data from yahoo finance
#df = web.DataReader("^HSI", "yahoo", start, end)
#df.to_csv("HSI.csv")
#Read data from csv file
df = pd.read_csv("HSI.csv", parse_dates=True, index_col=0)
#df = df[np.isfinite(df['Adj Close'])]
df = df[pd.notnull(df['Adj Close'])]
df['Average'] = (df['High'] + df['Low'] + df['Adj Close'])/3
df['10MA'] = df['Adj Close'].rolling(window=10, min_periods=10).mean()
df['20MA'] = df['Adj Close'].rolling(window=20, min_periods=20).mean()
df['50MA'] = df['Adj Close'].rolling(window=50, min_periods=50).mean()
df['250MA'] = df['Adj Close'].rolling(window=250, min_periods=250).mean()
df['SD'] = df['Average'].rolling(window=20, min_periods=20).std()
df['Lower'] = df['20MA'] - 2 * df['SD']
df['Upper'] = df['20MA'] + 2 * df['SD']
df = df.round(2)
#print(df.tail(100))

#Print chart
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=2)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=2, sharex=ax1)
ax1.xaxis_date()
candlestick2_ohlc(ax1, df['Open'], df['High'], df['Low'], df['Adj Close'], width=0.2, colorup='g', colordown='r', alpha=0.75)
ax2.fill_between(df['Volume'])
plt.show()

print("Program finish without error.")
