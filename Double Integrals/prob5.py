from sympy import *

s, t = symbols('s t')
f = pow(s + t, 0.5)
ans = integrate(f, (s, 0, t), (t, 0, 1))
print(ans)





