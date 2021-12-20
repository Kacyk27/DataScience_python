import numpy as np


A1 = np.array([[2, 3],
               [-1, 4],
               [-5, 2]])
A2 = np.array([[4, 3, -1],
               [2, 0, 1]])

x = np.matmul(A1,A2)
print(np.linalg.det(x))