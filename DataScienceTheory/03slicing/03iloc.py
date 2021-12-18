import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,5), columns=list('abcde'), index=list('abcdefghijklmnoprstu'))
#%% by col
# iloc[row_indexer, column_indexer]

col1 = df.iloc[:,0]


col1_to2 = df.iloc[:,0:2]
#or
col1_to2_v2 = df.iloc[:,[0,1]]
#or
col1_to2_v3 = df.iloc[:, :2]
#all are the same

#%%
col_last = df.iloc[:,-1]
col_last = df.iloc[:,4]

#%%
col_by_2 = df.iloc[:, ::2]

#%% by row

row1 = df.iloc[0, :] #jako series
row1_v2 = df.iloc[[0], :] #jako dataframe

row_last = df.iloc[-1, :]
row_last_v2 = df.iloc[[-1], :]

row_by2 = df.iloc[::2, :]

#%%

df_ = df.iloc[[0,19], [0,4]]




