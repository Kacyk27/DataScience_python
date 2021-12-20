import numpy as np


data = np.array([[4.3, 4.2],
                 [3.1, 3.6]])
target = np.array([[0],
                   [1]])

print(np.concatenate((data,target), axis=1))