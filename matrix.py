import numpy as np

a=np.array([[1,2,2],[1,2,2]])
b=np.array([[2,3,3,],[2,3,3]])
print(" a=",a)
print("b=",b)
c=np.matrix(a)+np.matrix(b)
print("sum of two matrixes:")
print(c)