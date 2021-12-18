import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


#%%
df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open','High','Low','Close','Volume']
clean_price = df[['Open','High','Low','Close']]
volume = df[['Volume']].copy()

#%% computing rank

volume['Volume_Rank'] = volume.rank(ascending=False)

volume = volume.sort_values(by='Volume_Rank',ascending=False)
#%% computing n largest volume


top_10 = volume.nlargest(n=10, columns='Volume')
top_10['Volume'].plot(kind='bar', cmap='plasma', alpha=0.5)

#%% rank by row

rank = clean_price.rank(method='first', axis=1)


