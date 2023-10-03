import numpy as np
A=np.matrix([[1,0,0],
             [0,0,1],
             [0,1,0]])
print("matrix A = :\n",A)
trans=A.T
print("transpose of matrix A : \n",trans)
identity=np.identity(3)
print("identity matrix : \n",identity)
AAT=np.dot(A,trans)
ATA=np.dot(trans,A)
print("AAT : \n",AAT)
print("ATA : \n",ATA)
ortho=np.allclose(np.dot(AAT,identity),np.dot(ATA,identity))
if  ortho:

    print("orthogonal matrix")
else:
    print("not an orthogonal matrix")
print("\n")
rank=np.linalg.matrix_rank(A)
print("rank of the matrix : \n",rank)
print("\n")
