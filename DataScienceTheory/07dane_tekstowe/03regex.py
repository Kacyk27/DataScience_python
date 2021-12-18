import pandas as pd
import numpy as np
#%%


string = 'workout summer good free holiday time time hot'

#%% splitting string

split = string.split(" ")

s = pd.Series(split)

#%% contains method

s.str.contains(r'[a-z]')

s[s.str.contains(r'[rg]')]






