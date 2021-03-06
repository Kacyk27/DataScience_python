import pandas as pd
import numpy as np


#%%
df = pd.read_csv('./data/ten.csv',index_col=0)
df.columns = ['Open','High','Low','Close','Volume']

#%% pct_change daily

df['Daily_Change'] = df['Close'].pct_change()

#%% pct_change 5 days

df['5_Daily_Change'] = df['Close'].pct_change(periods=5)

#%% pct_change Close to Open

df['Open_Close_Change'] = df[['Open','Close']].pct_change(axis=1).drop('Open',axis=1)

#%%
clean_price = df[["Open","High","Low","Close"]]


daily_changes = clean_price.pct_change()


