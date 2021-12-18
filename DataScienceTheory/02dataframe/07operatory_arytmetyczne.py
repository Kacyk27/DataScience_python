import pandas as pd
import numpy as np


#%%
df1 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
df2 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))

#%%
df1 + df2
df1 - df2
df1 * df2
df1 / df2












