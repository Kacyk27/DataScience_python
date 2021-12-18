import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,5), columns=list('abcde'), index=list('abcdefghijklmnoprstu'))

#%%
col_a = df.a

mask = df.a > 0
out = df[mask]


out = df[df.a >0] #to samo co wyżej inny zapis

#%%

mask = (df.a > 0) & (df.c > 0)
out1 = df[mask]

out1V1 = df[(df.a > 0) &  (df.c > 0)]

#%%

mask2 = (df.a > 0) | (df.b < 0)
out2 = df[mask2]

out2V1 = df[(df.a > 0) | (df.b < 0)]


