import numpy as np


A = np.array([[4, 3, 6],
              [5, 2, 7],
              [8, 3, 10],
              [3, 4, 2]])
def calc(col):
    for i in col:
        i = (col - min(col)) / (max(col)-min(col))
        return i

print(np.apply_along_axis(calc,axis=0,arr=A))
