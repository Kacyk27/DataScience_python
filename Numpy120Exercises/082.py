import numpy as np

A = np.array(['001', '002', '003'], dtype=np.str)
B = np.array(['XC', 'YC', 'ZC'], dtype=np.str)

print(np.char.add(A,B))






