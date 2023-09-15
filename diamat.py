import numpy as np
mat1=np.matrix([[1,2,3],
                [2,3,4],
                [4,5,6]])

#print the main matrix
print("the main matrix: \n",mat1)
#extract the diagonal from main matrix
vec=np.diagonal(mat1)
#print diagonal as vector
print("diagonal as a vector: \n",vec)

#creating a matrix using the extract diagonal
diamat=np.diag(vec)
print("extracted matrix using diagonal vector: \n",diamat)