from sympy import *

x, y = symbols('x y')
f = 1 + 2 * y
ans = integrate(f, (y, pow(x, 2), x), (x, 0, 1))
print(ans)
