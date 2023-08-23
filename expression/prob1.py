import sympy as sp
c1, c2= sp.symbols('c1 c2')
A = sp.Matrix([[-1, 2], [4, 1]])
AB = sp.Matrix([[-1, 2, 3], [4, 1, 6]])
rA = A.rank()
rAB = AB.rank()
print('RANK OF THE MATRIX A', rA)
print('RANK OF THE AUGMENTED MATRIX', rAB)
if rA == rAB:
    print('u1 u2  is a linear combination of v')
    x = sp.solve_linear_system(AB, c1, c2)
    print("{}*u1 + {}*u2  = v".format(x[c1], x[c2]))
else:
    print('u1 u2 is not a linear combination of v')