from sympy import *

r, t = symbols('r t')
a = Symbol('a', positive='true')
f = r
ans = integrate(f, (r, a*(1-cos(t)), a*sin(t)), (t, 0, pi/2))
print(simplify(ans))