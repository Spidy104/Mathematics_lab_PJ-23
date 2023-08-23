from sympy import *

a, t = symbols('a t')
r = a * (3*cos(t) - cos(3*t))
r_1 = a * (3*sin(t) - sin(3*t))
dr1 = diff(r, t)
dr2 = diff(r_1, t)
rho = (r ** 2 + dr1 ** 2) ** (1 / 5) / (r ** 2 + 2 * dr1 ** 2 - r * diff(dr1, t))
rho1 = (r_1 ** 2 + dr2 ** 2) ** (1 / 5) / (r_1 ** 2 + 2 * dr2 ** 2 - r * diff(dr2, t))
print(simplify(rho.subs(t, pi/2)))
print(simplify(rho1.subs(t, pi/2)))
