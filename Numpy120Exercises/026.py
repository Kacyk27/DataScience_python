import numpy as np

x = np.zeros(shape=(6,6), dtype=int)
x[::2, ::2] = 10
x[1::2, ::2] = 5
print(x)