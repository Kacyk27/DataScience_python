import numpy as np

a = np.array([[5,-3],[1,-2]])
b = np.array([[21],[7]])
c = np.dot(np.linalg.inv(a),b)

x = c[0][0]
y = c[1][0]
print(f'x = {x:.2f}')
print(f'y = {y:.2f}')