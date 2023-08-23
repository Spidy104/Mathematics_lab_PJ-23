from sympy import *

x, y, z = symbols('x y z')
f = 1
ans = integrate(f, (y, 1, 6 - x - z), (z, 0, 6 - x), (x, 0, 6))
print(simplify(ans))
