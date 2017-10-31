import datetime as dt
import pandas as pd
import pandas_datareader.data as pd_reader
import matplotlib.pyplot as mp_pyplot

df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
df.columns = df.ix[0]
df.drop(df.index[0], inplace=True)
