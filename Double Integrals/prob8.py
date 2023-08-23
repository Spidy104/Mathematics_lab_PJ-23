from sympy import *
x, y = symbols('x y')
f = pow(2*x + y, 8)
ans = integrate(f, (x, 0, y), (y, 0, 2))
print(ans)