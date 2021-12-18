import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%
df = pd.DataFrame(np.random.randn(100,4), columns=list('ABCD'))
#%%
#bar plot

df1 = df.cumsum()
bardata= df1.iloc[-1].apply(abs)
bardata.plot(kind='bar', title='random generated data', color='green', alpha=0.3)

#%% multiple bar plot vertical

df_bar = pd.DataFrame(np.random.rand(10,4), columns=list('ABCD'))

#df_bar.plot(kind='bar', cmap='viridis',title = 'mutiple bar plot', alpha=0.7)
df_bar.plot.bar(cmap='viridis',title = 'mutiple bar plot', alpha=0.7)

#%% multiple bar plot horizontal
df_bar.plot.barh(cmap='plasma',title = 'mutiple bar plot', alpha=0.7)

#%% stacked bar plot vertical

df_bar.plot.bar(cmap='viridis',title = 'mutiple bar plot', alpha=0.7, stacked=True)
#%% stacked bar plot horizontal

df_bar.plot.barh(cmap='plasma',title = 'mutiple bar plot', alpha=0.7,stacked=True)

