import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open','High','Low','Close','Volume']
clean_price = df[['Open','High','Low','Close']]

#%% computing corelation matrix

corr_matrix = clean_price.corr()



#%% corr between Series

df['Open'].corr(df['Close'])



#%% plot correlation matrix using matplotlib

plt.matshow(corr_matrix)


#%% plot correlation matrix using seaborn


sns.heatmap(corr_matrix)


