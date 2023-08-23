from sympy import *

r, t = symbols('r t')
a = Symbol('a', positive='true')
f = r
ans = integrate(f, (r, a * (1 + cos(t)), 3 * a * cos(t)), (t, 0, pi / 3))
print(2 * simplify(ans))
