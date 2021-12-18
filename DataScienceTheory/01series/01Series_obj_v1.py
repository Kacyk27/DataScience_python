import pandas as pd
import numpy as np


# Przykład 1

s = pd.Series(4)

# Przykład 2

s_def = pd.Series(data=[21,34,54], index=['Adas','Tomek','Paweł'],name='age')


# %%Przykład 3

A = np.random.randn(10)

s = pd.Series(A)

# %% Przykład 4

stocks = {'Apple':'USA','CD Project':"Poland","Amazon":"USA"}
series = pd.Series(stocks, name='country')

#%% Przykład 5
stocks_price = {'Apple':196,"CD Project":215,"Amazon":1877}
stocks_price_series = pd.Series(stocks_price, name='price')

stock_price_array = stocks_price_series.values

apple_price = stocks_price_series['Apple']

'Apple' in stocks_price_series

#%% Przykład 6

np.random.seed(0)

A = np.random.randn(20)
s = pd.Series(A)
s[0]
s[1]
s[5:10]
s[5::]
s[2:10:3]




















