import numpy as np


A = np.array([['#summer#time#mood'],
              ['#sport#time']])
A = np.char.replace(A, old="#", new=" ")
print(np.char.strip(A))