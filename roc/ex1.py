from sympy import *

t, r, a, n = symbols('t r a n')
r = a * cos(n * t)
r1 = Derivative(r, t).doit()
r2 = Derivative(r1, t).doit()
rho = (r**2 + r1 ** 2) ** (3/2) / (r ** 2 + 2 * r1 ** 2 - r * r2)
rho1 = rho.subs(t, pi/2)
rho1 = rho1.subs(n, 1)
print(simplify(rho1))
