from sympy import *

x, y = symbols = symbols('x y')
f = (x * exp(x)) / y
ans = integrate(f, (y, 1, exp(x)), (x, 0, 1))
print(ans)