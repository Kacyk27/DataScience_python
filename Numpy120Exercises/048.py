import numpy as np


A = np.arange(12, dtype='int').reshape(-1, 4)

print(A[::-1,::-1])