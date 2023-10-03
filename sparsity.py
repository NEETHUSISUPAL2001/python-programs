import numpy as np
A=np.matrix([[1,0,0],
             [0,0,1],
             [0,1,0]])
print("matrix A = :\n",A)
ele=A.size
zeroele=np.count_nonzero(A==0)
sparsity=zeroele/ele
print("sparsity of the matrix: \n",sparsity)
print("\n")