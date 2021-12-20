import numpy as np

A = np.array(['1','2','3'], dtype=np.str)
print(np.char.zfill(A,4))