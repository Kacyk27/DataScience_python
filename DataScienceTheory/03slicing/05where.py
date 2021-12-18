import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(20))

df = pd.DataFrame(np.random.randn(31,2), columns=list('ab'), index=pd.date_range('20190101',periods=31))

#%%

out = s[s > 0]
out1 = s.where(s > 0) #wrzuca nan

#%%

df2 = df[df > 0]
out2 = df.where(df > 0) # daje ten sam wynik co wyżej


out2 = df.where(df > 0, 0) #zamiast nan daje 0
#%%

out_task = df.where(df > 0, 0).where(df < 1, 1)

#%%

df = df.where(df > 0, 0).where(df < 1, 1)
