from sympy import *
x, y = symbols('x y')
M = y - sin(x)
N = cos(x)
f = diff(N, x) - diff(M, y)
soln = integrate(f, [y, 0, 2*x/pi], [x, 0, pi/2])
print(simplify(soln))