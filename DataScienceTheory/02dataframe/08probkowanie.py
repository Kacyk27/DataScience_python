import pandas as pd
import numpy as np

#%%
df = pd.read_csv('./data/aapl_us_d.csv',index_col=0)

#%% sampling n numbers
sample10 = df.sample(n=10)


#%%
simple10_percent = df.sample(frac=0.1)








