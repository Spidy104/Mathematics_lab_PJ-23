import sympy as sym
A = sym.Matrix([[1, -1, 3, 4],
                [2, 1, 6, 8],
                [1, 1, 1, 1],
                [3, 2, 7, 9]])
m, n = sym.shape(A)
print(n)
B = A.rref()
r = A.rank()
print(r)
print(B[0])
print('LINEARLY INDEPENDENT') if n == r else print('LINEARLY DEPENDENT')
