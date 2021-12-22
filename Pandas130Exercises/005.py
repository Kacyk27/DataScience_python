import numpy as np
import pandas as pd

x = pd.Series(np.arange(10, 100, step = 10, dtype=np.float64))
x.index +=101

print(x)