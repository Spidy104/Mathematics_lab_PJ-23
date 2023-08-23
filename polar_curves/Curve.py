from sympy import *

x, c = symbols('x c')
y = c * cosh(x / c)
r1 = diff(y, x).subs({x: 0, y: c}).evalf()
r2 = diff(y, x, 2).subs({x: 0, y: c}).evalf()
rho = (1 + r1 ** 2) ** 1.5 / r2
print(abs(rho))
