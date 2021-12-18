import pandas as pd

#%%

df = pd.read_csv('./data/cdr.csv', index_col=('Data'))

df.describe()

#%% 

df_ = pd.read_csv('./data/cdr.csv', index_col=0, skiprows=200)

#%%

df_ = pd.read_csv('./data/cdr.csv', index_col=0, nrows=100)


#%%

df1 = pd.read_csv('./data/reviews_clean.csv', index_col=0)



