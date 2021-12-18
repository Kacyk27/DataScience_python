import pandas as pd
import numpy as np

#%%

df_raw = pd.read_clipboard()


#%%
columns=[col for col in df_raw.columns]
#%%

df = df_raw.drop(['Czas','1r 3m'], axis=1)

#%%
df['Wolumen'] = df['Wolumen'].apply(lambda x: x.replace(' ', "")).apply(lambda x: int(x))

#%%

df['Obrót'] = df['Obrót'].apply(lambda x: x.replace(' ', "")).apply(lambda x: int(x))

#%%
df['Udział'] = df['Udział'].apply(lambda x: x.replace('%', "")).apply(lambda x: float(x))

#%%
df['Zmiana %'] = df['Zmiana %'].apply(lambda x: x.replace('%', "")).apply(lambda x: x.replace('(', "")).apply(lambda x: x.replace(')', "")).apply(lambda x: float(x))

