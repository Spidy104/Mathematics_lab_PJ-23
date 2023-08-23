from sympy import *
x, y = symbols('x y')
M = x*y + pow(y, 2)
N = pow(x, 2)
f = diff(N, x) - diff(M, y)
soln = integrate(f, [y, pow(x, 2), x], [x, 0, 1])
print(simplify(soln))