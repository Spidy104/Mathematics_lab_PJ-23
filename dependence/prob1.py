import sympy as sym
A = sym.Matrix([[1, 2, 3],
                [0, 1, 1],
                [0, 3, 4]])
m, n = sym.shape(A)
print(n)
B = A.rref()
r = A.rank()
print(r)
print(B[0])
print('LINEARLY INDEPENDENT') if n == r else print('LINEARLY DEPENDENT')
