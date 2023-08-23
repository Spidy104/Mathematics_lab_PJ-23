import numpy as np
from sympy import *

x, y, z = symbols('x y z')
a = np.matrix([[1, 1, 1], [2, -1, 3], [4, -2, -1]])
b = np.matrix([[0], [0], [0]])
ab = np.concatenate((a, b), axis=1)
n = a.shape[1]
r = np.linalg.matrix_rank(a)
print("System has trivial solution") if n == r else print("System doesn't have trivial solutions")
print(solve_linear_system(ab, x, y, z))
