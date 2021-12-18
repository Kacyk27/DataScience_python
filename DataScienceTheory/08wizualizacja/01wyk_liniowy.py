import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


#%%

ts = pd.Series(np.random.randn(1000), index=pd.date_range('2019-01-01',periods=1000))

#%%

ts = ts.cumsum()

ts.plot()

#%%

ts = ts.cummin()
ts.plot()

#%%
ts = ts.cummax()
ts.plot()

#%%

df = pd.DataFrame(np.random.randn(1000,5), index=pd.date_range('2019-01-01',periods=1000), columns=list('ABCDE'))
#%%

df = df.cumsum()
#%%
df.plot()
#%%
df['B'].plot()

#%%
abs(df.iloc[5]).plot(kind='bar', title='Bar chart')











