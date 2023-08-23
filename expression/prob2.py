import sympy as sp

c1, c2, c3 = sp.symbols('c1 c2 c3')
A = sp.Matrix([[-1, 1, 0], [2, 0, 2], [1, 1, 1]])
AB = sp.Matrix([[-1, 1, 0, 1], [2, 0, 2, 2], [1, 1, 1, 3]])
rA = A.rank()
rAB = AB.rank()
print('RANK OF THE MATRIX A', rA)
print('RANK OF THE AUGMENTED MATRIX', rAB)
if rA == rAB:
    print('u1 u2 u3 is a linear combination of v')
    x = sp.solve_linear_system(AB, c1, c2, c3)
    print("{}*u1 + {}*u2 + {}*u3  = v".format(x[c1], x[c2], x[c3]))
else:
    print('u1 u2 is not a linear combination of v')
