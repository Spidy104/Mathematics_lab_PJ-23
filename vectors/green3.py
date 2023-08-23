from sympy import *

x, y = symbols('x y')
M = 3 * x + 4 * y
N = 2 * x - 3 * y
f = diff(N, x) - diff(M, y)
soln = integrate(f, [y, -sqrt(4 - pow(x, 2)), sqrt(4 - pow(x, 2))], [x, -2, 2])
print(simplify(soln))
