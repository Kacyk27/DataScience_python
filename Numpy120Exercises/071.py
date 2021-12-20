import numpy as np


np.random.seed(42)

A = np.array([['id', 'price'],
              ['001', 14.99],
              ['002', 4.99],
              ['003', 7.99],
              ['004', 2.49],
              ['005', 1.49]])
np.random.shuffle(A[1:])
print(A)