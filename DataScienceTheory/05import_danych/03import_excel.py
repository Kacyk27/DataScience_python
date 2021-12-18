import pandas as pd


#%%
df = pd.read_excel('./data/companies.xlsx', na_values="?",index_col=0)

#%%
df1 = pd.read_excel('./data/companies.xlsx',sheet_name='microsoft',index_col=0)
#%%
df2 = pd.read_excel('./data/companies.xlsx',sheet_name='google',index_col=0)