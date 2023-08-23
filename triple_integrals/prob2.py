from sympy import *

x, y, z = symbols('x y z')
f = 1/sqrt(pow(x, 2) - pow(y, 2))
ans = integrate(f, (y, 0, pow(x, 2)), (x, 0, 0.5), (z, 0, 4))
print(ans)