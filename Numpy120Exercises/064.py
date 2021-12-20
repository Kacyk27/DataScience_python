import numpy as np


A = np.linspace(0, np.pi / 2, 20)
B = np.full(shape=(20,), fill_value=1, dtype='float')


print(np.allclose(np.sin(A)**2 +np.cos(A)**2, B))