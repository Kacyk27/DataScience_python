import pandas as pd
import numpy as np



#%%
df = pd.read_csv('data/aapl_us_d.csv', index_col='Data')

#%%
first_50 = df.iloc[:50]
df.iloc[10:20]
df.iloc[10:]
df.head()
df.tail()
df.iloc[[1,4,20,500,793],[0,4]]
df.iloc[::30]
df.iloc[:,::2]
#%%
df.iloc[:, :2]
df.iloc[:, :3]
df.iloc[:5, :2]

df.iloc[5:10, 3:]



























