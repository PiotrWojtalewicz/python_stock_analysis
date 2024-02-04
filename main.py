#all useful library to create my project
from datetime import datetime as dt
from datetime import timedelta
import yfinance as yf
import pandas as pd

###

#First step is set period of the analysis where end of period is current date. My analysis includes period of 180 days.
endtime = dt.now()
starttime = endtime-timedelta(days=180)

#next step is download current data from yahoo finance. Special API allows me download usefull information to my project.
#in this case I compare 3 large food companies and SP500 (500 companies with the largest capitalization)
daily_sp500=yf.download("^GSPC", start= starttime, end = endtime)
# print(daily_sp500)
daily_pepsi_corp = yf.download("PEP", start =starttime, end = endtime)
# print(daily_pepsi_corp)
daily_cocacola_corp = yf.download("CC",start=starttime,end = endtime)
daily_tysonfoods = yf.download("TSN", start = starttime,end =endtime)

#convert download data to a dataframe
df_sp500 = pd.DataFrame(daily_sp500, columns = ["Adj Close"])
df_pepsi = pd.DataFrame(daily_pepsi_corp, columns = ["Adj Close"])
df_cocacola = pd.DataFrame(daily_cocacola_corp, columns = ["Adj Close"])
df_foods = pd.DataFrame(daily_tysonfoods, columns = ["Adj Close"])


# print(df_sp500)









