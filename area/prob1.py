from sympy import *

r, t = symbols('r t')
a = Symbol('a', positive='true')
f = r
ans = integrate(f, (r, 0, a*sqrt(cos(2*t))), (t, 0, pi/4))
print(4 * simplify(ans))