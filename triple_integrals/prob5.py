from sympy import *

x, y, z = symbols('x y z')
f = (x * y * z)
ans = integrate(f, (z, 0, sqrt(1-x**2-y**2)), (y, 0, sqrt(1 - x**2)), (x, 0, 1))
print(simplify(ans))
