from sympy import *

x, y, z = symbols('x y z')
a = Symbol('a', positive='true')
f = x
ans = integrate(f, (x, 0, sqrt(pow(a, 2) - pow(y, 2) - pow(z, 2))), (y, 0, sqrt(pow(a, 2) - pow(z, 2))), (z, 0, a))
print(simplify(ans))
