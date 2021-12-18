import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df = pd.read_csv('./data/googleplaystore.csv')
#%% preprocessing
df.info()

df.columns = [col.replace(" ","_") for col in df.columns]
col = [col for col in df.columns]

df.drop(10472, inplace=True)

df = df.reset_index()

df.Reviews = pd.to_numeric(df.Reviews)
#%% categories frequency
tmp = df.groupby('Category').size().rename('Count')
tmp.plot(kind='bar', color='purple', alpha=0.5, title='Categories')



#%% type frequency

tmp1 = df.groupby('Type').size().rename('Count')
tmp1.plot(kind='pie', cmap='icefire', fontsize=10)

#%%
df = df[['Genres','Rating','Type']]
tmp = df.groupby(['Genres','Type']).agg({'Rating':['count','mean']})
tmp.columns = ['_'.join(x) for x in tmp.columns.ravel()]
tmp = tmp.sort_values('Rating_count',ascending=False)
tmp = tmp[tmp['Rating_count'] > 100]
tmp.plot(kind='bar', subplots=True, cmap='plasma')

#%% top5

top5 = tmp.nlargest(5, columns='Rating_count')['Rating_count']
top5.plot(kind='pie', cmap='plasma')




