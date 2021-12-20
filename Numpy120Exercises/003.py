import numpy as np


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

elements=[A,B,C,D]

for name,element in zip('ABCD', elements):
    print(f"{name}: {np.any(element)}")