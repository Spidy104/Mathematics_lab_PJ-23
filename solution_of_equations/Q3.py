from sympy import *
import numpy as np

x, y, z = symbols('x y z')
a = np.matrix([[1, 1, 1], [2, 2, -2], [1, -2, -1]])
b = np.matrix([[2], [4], [5]])
ab = np.concatenate((a, b), axis=1)
rA = np.linalg.matrix_rank(a)
rAB = np.linalg.matrix_rank(ab)
n = a.shape[1]
if rA == rAB:
    print("UNIQUE SOLUTION") if rA == n else print("INFINITE SOLUTIONS")
    print(solve_linear_system(ab, x, y, z))
else:
    print("The set of equations are inconsistent")
