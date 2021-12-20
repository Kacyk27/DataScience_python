import numpy as np

x = np.array(np.arange(12)).reshape((3,4))

np.savetxt('array.txt',x)

arr = np.loadtxt('array.txt')
print(arr)