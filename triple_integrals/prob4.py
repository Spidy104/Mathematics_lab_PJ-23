from sympy import *

x, y, z = symbols('x y z')
f = x+y+z
ans = integrate(f, (z, 0, (x+y)), (y, 0, x), (x, 0, 1))
print(simplify(ans))