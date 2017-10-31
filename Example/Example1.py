import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")
start = dt.datetime(2017,10,1)
end = dt.datetime(2017,11,1)
#Get data from yahoo finance
#df = web.DataReader("AMZN", "yahoo", start, end)
#df.to_csv("amzn.csv")
#Read data from csv file
df = pd.read_csv("amzn.csv", parse_dates=True, index_col=0)
print(df.tail(6))

print("Program finish without error.")
