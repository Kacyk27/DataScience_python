import pandas as pd
import numpy as np

#%%

df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
#%%

df = df1.append(df2)
df = df.reset_index()
del df['index']

#%%

df = df1.append(df2).reset_index()
df.drop('index',axis=1, inplace=True)
#%%

df = df1.append(df2, ignore_index=True)








