import numpy as np
from sympy import *

x, y, z = symbols('x y z')
a = np.matrix([[6, 3, 4], [6, 3, 4], [2, 1, 6]])
b = np.matrix([[0], [0], [0]])
ab = np.concatenate((a, b), axis=1)
rA = np.linalg.matrix_rank(a)
rAB = np.linalg.matrix_rank(ab)
n = a.shape[1]
if rA == rAB:
    print('The system has unique solution') if rA == n else print('The system has infinite solutions')
    print(solve_linear_system(ab, x, y, z))
else:
    print("The system has no solutions")
