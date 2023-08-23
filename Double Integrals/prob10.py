from sympy import *

x, y = symbols('x y')
f = 1 / (1 + pow(x, 2) + pow(y, 2))
ans = integrate(f, (y, 0, x), (x, 0, 1))
print(ans)
