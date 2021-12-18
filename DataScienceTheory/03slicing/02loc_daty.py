import pandas as pd
import numpy as np

#%%

df = pd.DataFrame(np.random.randn(31,5),columns=list('abcde'), index=pd.date_range(start='2019-01-01', periods=31))

#%%

idx = df.index

day = df.loc['2019-01-02']
week = df.loc['2019-01-01':'2019-01-07']

after_15 = df.loc['2019-01-15':]














