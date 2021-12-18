import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%%
path = 'D:\\kursy_Krakowiak\\Wprowadzenie do data science Pandas\\data\\amzn_us_d.csv'

df = pd.read_csv(path,index_col=(['Data'])) #lub index_col=0

close = df['Zamkniecie']


close = close["2010-01-01":] #wyznaczanie danych od konkretnego indeksu

#%% Wykres 

close.plot(title='Wykres notowań spółki Amazon',logy=True)

plt.savefig('./charts/close.png',format='png')

# %% do csv

close.to_csv('./data/close_amzn.csv',header=['close'])