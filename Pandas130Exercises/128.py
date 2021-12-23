import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

result = pd.pivot_table(tips,values=['tip','total_bill'],index=['day','sex'],aggfunc='mean')
print(result)