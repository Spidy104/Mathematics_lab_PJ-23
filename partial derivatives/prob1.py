from sympy import *

x, y = symbols('x y')
u = atan(y / x)
duxy = diff(u, x, y)
duyx = diff(u, y, x)
print('VERIFIED') if simplify(duxy) == simplify(duyx) else print('NOT VERIFIED')
