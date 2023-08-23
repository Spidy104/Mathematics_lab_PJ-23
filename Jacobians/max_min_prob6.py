from sympy import *

x, y, z = symbols('x y z')
f = x*y*(z ** 2)
dx, dy, dz = diff(f, x), diff(f, y), diff(f, z)
eq1, eq2, eq3 = Eq(dx, 0), Eq(dy, 0), Eq(dz, 0)
sol = solve([eq1, eq2, eq3], (x, y, z))
# for i, j, z in sol:
