from sympy import *

x, y, z = symbols('x y z')
f = 1/(1 - x**2 - y**2 - z**2)
ans = integrate(f, (z, 0, (1 - x**2 - y**2)), (y, 0, (1 - x**2)), (x, 0, 1))
print(simplify(ans))
