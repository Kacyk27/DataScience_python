import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



#%% import data
df = pd.read_csv('./data/Consumer_Reviews_Amazon.csv')

#%%                 FAZA 1
#             Przetworzenie danych

df.describe()

#%%
for col in df.columns:
    print(col)

df.info()

df.columns = [col.replace(".","_") for col in df.columns]
#%%

df = df[['name','primaryCategories','reviews_rating','reviews_text']]

df.columns=['name','category','rating','text']
#%%
df.info()
df.describe()

#%%
df.to_csv('./data/reviews_clean.csv')

#%%                FAZA 2
#              Analiza danych

del df
del col
#%%import data

df = pd.read_csv('./data/reviews_clean.csv', index_col=0)
#%% plotting categories

df['category'].value_counts().plot(kind='pie')
#%% plotting rating frequency

df['rating'].value_counts().sort_index().plot(kind='bar', legend=True, title='Frequency')

#%% extract top 3 most rating products
tmp = df.groupby('name').count()['rating'].rename('count').nlargest(3)

#%% extract top 3 high rated products

tmp1 = df.groupby('name').agg('mean').rename(columns={'rating':'avg_rating'}).nlargest(3,'avg_rating')

#%% extract bottom 3 products

tmp2 = df.groupby('name').agg('mean').rename(columns={'rating':'avg_rating'}).nsmallest(3,'avg_rating')








