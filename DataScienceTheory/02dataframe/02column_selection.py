import pandas as pd
import numpy as np

#%%

df = pd.read_csv('data/aapl_us_d.csv',index_col=0)
df.columns = ['Open','High','Low','Close','Volume']


#%%

print(df.columns)

open_price = df["Open"]
open_price = df.iloc[:,0] #to samo co wyzej

high_price = df['High']

#%%

close_price = df.Close #trzeci sposób na pobranie kolumny, kolumny ze spacją nie działają, lepiej zamienic na podkreslnik albo innym sposobem

volume = df.Volume

#%%

last_col = df.iloc[:,-1]

#%%

two = df[['Open','Close']]
three = df.iloc[:,[0,3]]

#%%
from_open_to_close = df.iloc[:, :-1]














