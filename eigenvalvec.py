import numpy as np
A=np.matrix([[1,2],[1,3]])
print("matrix A = :\n",A)

eigenvect=np.linalg.eig(A)
print("eigen vector: \n",eigenvect)
print("\n")