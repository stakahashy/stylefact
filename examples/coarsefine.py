import datetime as dt
import pandas_datareader.data as web
import numpy as np
import sys
sys.path.append('../')
import stylefact.finance as sff
import stylefact.visualize as sfv
st = dt.datetime(1990,1,1)
en = dt.datetime(2020,1,1)
data = web.get_data_yahoo('GM', start=st, end=en)
prices = data['Adj Close'].to_numpy()
log_prices = np.log(prices)
returns = np.diff(log_prices)
x,y = sff.coarsefine_volatility(returns)
sfv.coarsefine_volatility(x,y,'coarsefine')
