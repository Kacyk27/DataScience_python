import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

result = pd.pivot_table(tips, index=['day', 'sex', 'smoker'], values=['tip', 'total_bill'], aggfunc=np.mean)

x = result.loc["Sun",:]

print(x.loc['Male'])

