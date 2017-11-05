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
start = dt.datetime(2017, 10, 1)
end = dt.datetime(2018, 1, 1)
#Get data from yahoo finance
df = web.DataReader("0700.hk", "yahoo", start, end)
df.to_csv("0700.csv")
#Read data from csv file
df = pd.read_csv("0700.csv", parse_dates=True, index_col=0)
df = df.round(2)
print(df.tail())

print("Program finish without error.")
