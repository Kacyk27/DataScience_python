import numpy as np


A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)