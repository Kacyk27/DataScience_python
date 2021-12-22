import pandas as pd
import numpy as np

series = pd.Series(['001', '002', '003', '004'], list('abcd'))
series = series.astype('int64')
print(series)