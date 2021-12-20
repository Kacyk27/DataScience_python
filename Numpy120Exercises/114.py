import numpy as np


u = np.array([1, 0, 0])
v = np.array([0, 1, 0])

result = np.dot(u+v,v+u) == np.dot(u,u) + np.dot(v,v)
print(result)


