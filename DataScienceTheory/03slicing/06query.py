import pandas as pd
import numpy as np



df = pd.DataFrame(np.random.rand(10,5), columns=list('abcde'))

#%%

out1 = df.query('(a < b)')

#%%
out2 = df.query('(a < b) & (c < b)')
out3 = df.query('(a < b) | (b < c)')

#%%

df = df.round(1)

#%%
df.query('c == [0.2, 0.4]')

df.query('c != 0.5')

df.query('[0.5] in c')


