from sympy import *

x, y = symbols('x y')
f = x * y
ans = integrate(f, (x, y, 2 * y), (y, 0, 2))
print(ans)
