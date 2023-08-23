from sympy import *

x, y = symbols('x y')
f = x * pow(y, 2)
ans = integrate(f, (x, 0, pow(y, 0.5)), (y, 0, 4))
print(ans)
