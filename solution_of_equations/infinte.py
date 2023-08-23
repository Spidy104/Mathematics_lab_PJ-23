import numpy as np
from sympy import *

x, y, z = symbols('x y z')
a = np.matrix([[2, 2, 3], [1, 1, 1], [3, 3, 3]])
b = np.matrix([[17], [3], [9]])
ab = np.concatenate((a, b), axis=1)
rA = np.linalg.matrix_rank(a)
rAB = np.linalg.matrix_rank(ab)
n = a.shape[1]
if rA == rAB:
    print("UNIQUE SOLUTION") if rA == n else print("Infinite solutions")
    print(solve_linear_system(ab, x, y, z))
else:
    print("The set of equations are inconsistent")