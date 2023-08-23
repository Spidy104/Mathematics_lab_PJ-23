from sympy import *
x, y = symbols('x y')
f = (4 * pow(x, 3)) - (9 * pow(x, 2) * pow(y, 2))
ans = integrate(f, (y, 1, 2*x), (x, 0, 1))
print(ans)