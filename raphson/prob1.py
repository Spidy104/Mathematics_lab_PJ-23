from sympy import *

x = Symbol('x')
y = Function(x)
y = 3 * x - cos(x) - 1
Y = lambdify(x, y)
y1 = diff(y, x)
Y1 = lambdify(x, y1)
x0 = 0.4
error = 1
i = 1
while error > 1e-4:
    x1 = x0 - (Y(x0) / Y1(x0))
    error = abs(x1 - x0)
    print('x{} = {}'.format(i, x1))
    print('Error', error)
    x0 = x1
    i += 1
