import numpy as np


np.random.seed(42)

A = np.random.randn(8, 4)

A = np.delete(A,2, axis=1)
print(A)