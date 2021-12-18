import pandas as pd
import numpy as np

left = pd.DataFrame(np.random.rand(10,3), index=pd.date_range('2019-01-01',periods=10), columns=list('abc'))

right = pd.DataFrame(np.random.rand(10,3), index=pd.date_range('2019-01-04',periods=10), columns=list('def'))

#%% left

df_left = left.join(right, how='left')


#%% right

df_right = left.join(right, how='right')

#%% inner
df_inner = left.join(right, how='inner')



#%% outer

df_outer = left.join(right, how='outer')

