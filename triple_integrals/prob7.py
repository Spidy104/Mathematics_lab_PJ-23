from sympy import *

x, y, z = symbols('x y z')
f = x+y+z
ans = integrate(f, (x, x-z, x+z), (y, 0, z), (z, -1, 1))
print(simplify(ans))
