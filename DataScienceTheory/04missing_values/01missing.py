import pandas as pd
import numpy as np


#%%

df = pd.DataFrame(np.random.randn(10,4), columns=['one','two','three','four'])

#%%

for row in df.values:
    i = np.random.choice([0, 1, 2, 3])
    row[i] = np.nan
    
#%%
for row in df.values:
    switch = np.random.choice([0,1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan

#%% isnull

df.isnull()
df[df.isnull()]

df['one'].isnull()
df[df['one'].isnull()]
df[~df['one'].isnull()]

#%% notnull()
df.notnull()
df[df.notnull()]
df[df['three'].notnull()]
df['three'].notnull()

#%%
df['five'] = np.nan

del df['five']







