import numpy as np


A = np.array([4, 3, 5, np.nan, 5, 3, np.nan])
print(A[~np.isnan(A)])