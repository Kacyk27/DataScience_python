import pandas as pd
import numpy as np



#%%
df = pd.read_csv('data/aapl_us_d.csv',index_col=0)

df.columns = ['Open','High','Low','Close','Volume']

#%% compute new columns

df['Average'] = (df['Open'] + df['Close']) / 2.0

df['Daily_Change'] = df['Close'] / df['Close'].shift(1) -1 #shift przesuwa wszystko o jeden w dół, wiec dzieli sie przez poprzedni dzien., ile dni tyle w wartosci shift

#%% metoda assign

df = df.assign(avg = (df['Open'] + df['Close']) / 2.0)
df['avg'] == df['Average']

#%%

max_daily_change = df['Daily_Change'].aggregate(max)
min_daily_change = df['Daily_Change'].aggregate(min)
avg_daily_change = df['Daily_Change'].aggregate(np.mean)

#%%

df['Daily_Change'].hist(bins=100)    #bins - ilosc slupkow

#%%
df['Flag'] = df['Daily_Change'] > 0
df['Flag'].aggregate(sum)

#%%
days_with_positive_return = df['Flag'].aggregate(sum) / df['Flag'].aggregate('count')














