import numpy as np

x = np.array(np.arange(12)).reshape((3,4))
x = x[::-1]
print(x)