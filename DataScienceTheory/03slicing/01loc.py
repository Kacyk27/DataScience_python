import pandas as pd
import numpy as np

#%%

df = pd.DataFrame(np.random.randn(20,5),columns=list('abcdc'), index=list('abcdefghijklmnoprstu'))

#%% loc columns

col_a = df.loc[:,'a']
col_b = df.loc[:,'b']
col_ab = df.loc[:,['a','b']]

col_bcd = df.loc[:, 'b':'d']

#%% loc rows

row_a = df.loc['a',:]
row_a1 = df.loc[['a'],:]

row_ac = df.loc[["a","c"],:]

#%% loc rows cols

rowa_cola = df.loc['a','a']

#%%
rows_ad_cols_bd = df.loc["a":'d', 'b':'d']




