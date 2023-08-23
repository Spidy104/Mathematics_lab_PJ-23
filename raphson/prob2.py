from sympy import *
from math import pi
x = Symbol('x')
y = Function(x)
y = x * sin(x) + cos(x)
Y = lambdify(x, y)
y1 = diff(y, x)
Y1 = lambdify(x, y1)
x0 = pi
error = 1
i = 1
while error > 1e-15:
    x1 = x0 - (Y(x0) / Y1(x0))
    error = abs(x1 - x0)
    print('x{} = {}'.format(i, x1))
    print('Error', error)
    x0 = x1
    i += 1
