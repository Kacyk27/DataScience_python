import numpy as np


A = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [-3, 4, 2]])
def minus(col):
    return max(col) - min(col)

print(np.apply_along_axis(minus,axis=0,arr=A))
