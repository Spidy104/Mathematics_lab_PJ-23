from sympy import *

x, y = symbols('x y')
f = (x / y) + (y / x)
ans = integrate(f, (y, 1, pow(x, 2)), (x, 1, 4))
print(ans)
