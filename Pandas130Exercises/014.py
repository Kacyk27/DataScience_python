import pandas as pd
import numpy as np
a = pd.date_range('2021-03-01',periods=31)
x = pd.DataFrame(data=a, columns=['day'])
x['day_of_year'] = x['day'].dt.dayofyear


print(x)