import numpy as np
vec=np.array([1,2,3])
a=np.matrix([[4,5,6],
             [7,8,9],
             [10,11,12]])
z=np.dot(vec,a)
print(z)