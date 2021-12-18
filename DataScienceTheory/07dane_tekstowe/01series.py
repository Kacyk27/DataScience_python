import pandas as pd
import numpy as np


s = pd.Series(['Apple', '     Microsoft', np.nan , '  Google  ','Amazon'], name='stock')

#%%

s = s.str.strip()

#%%

s = s.str.upper()

#%%

s = s.str.len()

#%%

df = pd.DataFrame(np.random.randn(10, 2), columns = ['                      ID User', '         price            '])

#%%
df.columns = df.columns.str.strip()

#%%

df.columns = df.columns.str.replace(' ',"_")


df.ID_User