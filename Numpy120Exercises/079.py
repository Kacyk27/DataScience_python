import numpy as np

x = np.arange('2021-01','2022-01', dtype='datetime64[M]')
x = x.reshape(-1, 3)
print(x)