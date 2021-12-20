import numpy as np


v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])

v1_norm = np.linalg.norm(v1)
v2_norm = np.linalg.norm(v2)
 
print(np.arccos(np.dot(v1, v2) / (v1_norm * v2_norm)))