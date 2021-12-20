import numpy as np


np.random.seed(42)

A = np.random.randint(low=0, high=2, size=(10, 6))

print(np.count_nonzero(A))

