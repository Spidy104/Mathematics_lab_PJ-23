from sympy import *

A = Matrix([[1, 0, -1, -1], [1, 0, -1, -1], [1, 2, -1, 3]])
print(A)
B, pivot = A.rref()
print(B, pivot)
rA = A.rank()
print(rA)
print('ROW BASIS:')
print(B[0:rA, :])
print('COLUMN BASIS:')
print(B[:, pivot])
print('THE NULLSPACE IS')
print(A.nullspace())
print('THE DIMENSION IS')
print(len(A.nullspace()))