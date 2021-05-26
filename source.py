import pandas_datareader as webtart,end)
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt
from datetime import timedelta

crypto = "DOGE"
currency = "USD"

start = dt.datetime(2021,4,25)
end = dt.datetime.now()

data = web.DataReader(f"{crypto}-{currency},"yahoo",start,end)

mplf.plot(data)
