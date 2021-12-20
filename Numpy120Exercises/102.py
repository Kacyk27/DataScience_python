import numpy as np

a = np.array([[1,1,1],[2,1,5],[1,-1,-1]])
b = np.array([[1],[0],[0]])
c = np.dot(np.linalg.inv(a),b)

x = c[0][0]
y = c[1][0]
z = c[2][0]
print(f'x = {x:.2f}')
print(f'y = {y:.2f}')
print(f'z = {z:.2f}')