from sympy import *
x, y = symbols('x y')
f = x - y
ans = integrate(f, (y, 2*x, 2), (x, 0, 1))
print(ans)