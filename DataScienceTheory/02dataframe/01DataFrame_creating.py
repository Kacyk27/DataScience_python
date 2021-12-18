import numpy as np
import pandas as pd

#%%

df = pd.DataFrame(data=[12,34,23])

#%% obiekt 2x3

df = pd.DataFrame(data=[[12,54,32],[53,23,74]], index =['first','second'], columns=['col1','col2','col3'])


#%% 3x3

df = pd.DataFrame(data=[[12,54,32],[53,23,74],[3123,234243,223]], index =['first','second','third'], columns=['col1','col2','col3'])

#%%

d={'one':pd.Series([1,2,3]), 'two':pd.Series([4,5,6])}

df = pd.DataFrame(d)

#%%
d={'one':pd.Series([1,2,3]), 'two':pd.Series([4,5,6]), 'flag':['yes','no','no']}

df = pd.DataFrame(d)


#%% z Series o różnej długosci

d={'one':pd.Series([1,2,3,4,5]), 'two':pd.Series([4,5,6])}

df = pd.DataFrame(d)

#%%

d = {'one': pd.Series(np.random.randn(100)), 'two': pd.Series(np.random.randn(100)), 'three': pd.Series(np.random.randn(100))}

df = pd.DataFrame(d)

# %%

df.index
df.columns

# %%
list_of_dicts = [{'apple':1, 'orange':4},{'apple':3,'orange':3,'mango':2}]

df = pd.DataFrame(list_of_dicts)

#%%

for col in df.columns:
    print(col)

big_letters = [col.upper() for col in df.columns]

df.columns = big_letters

#%%

d = {"Wig20": ["PKN Orlen",'PKO BP','LPP'], 'wMig40':['Amica','Playway','Benefit']}

df = pd.DataFrame(d)







