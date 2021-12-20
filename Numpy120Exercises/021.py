import numpy as np

x = np.array(np.arange(12)).reshape((3,4))

np.save('array.npy',x)

arr = np.load('array.npy')
print(arr)