import numpy as np


np.random.seed(42)

A = np.random.randint(low=0, high=7, size=(5, 8))
A[:, :2] = 0
A[:, -2:] = 1

A1, A2, A3 = np.split(A, [2, 6], axis=1)
print(A1)
print(A2)
print(A3)