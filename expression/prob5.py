from sympy import *
A = Matrix([[1, 2, -3, 1], [2, 2, 1, 3]])
m, n = shape(A)
print(A)
print('Rank of the matrix is')
print(A.rank())
N = len(A.nullspace())
print('RANKNULLITY THEOREM VERIFIED') if n == A.rank() + N else print('NOT VERIFIED')