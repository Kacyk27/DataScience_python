import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

elements=[A,B,C]

for name,element in zip('ABCD', elements):
    print(f"{name}: {np.all(element, axis=1)}")