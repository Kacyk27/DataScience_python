import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%%

tips = sns.load_dataset('tips')

#%%

tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='mean')

pv = tips.pivot_table(values=['tip','total_bill'], index='sex', columns='day', aggfunc='mean')


pv1 = tips.pivot_table(values=['tip','total_bill'], index='sex', columns='day', aggfunc='max')

pv2 = tips.pivot_table(values=['tip','total_bill'], index='sex', columns='day', aggfunc='min')

pv3 = tips.pivot_table(values='tip', index='sex', columns=['day','smoker'], aggfunc='max')

pv4 = tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='mean').plot(kind='bar', cmap='plasma', alpha=0.5)

pv5 = tips.pivot_table(values='total_bill', index='sex', columns='day', aggfunc='mean').plot(kind='bar', cmap='plasma', alpha=0.5)

#%%
tips.pivot_table(values='tip', index='day', columns='size', aggfunc='mean').plot(kind='bar', cmap='plasma', alpha=0.5)

#%%
tips.pivot_table(values='total_bill', index='time', columns='size', aggfunc='mean').plot(kind='bar', cmap='plasma', alpha=0.5)

#%%
vals = tips[['total_bill','tip']]
vals.corr()





