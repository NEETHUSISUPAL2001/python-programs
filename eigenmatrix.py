

import numpy as np
A = np.array([[4, 2],
              [1, 3]])
print("matrix A : \n",A)
eigenvalues,eigenvectors = np.linalg.eig(A)
print("eigenvalues : ",eigenvalues)
print("eigenvectors : \n",eigenvectors)
D = np.diag(eigenvalues)
re_A = np.dot(np.dot(eigenvectors, D), np.linalg.inv(eigenvectors))
print("Reconstructed Matrix A:")
print(re_A )