from sympy import *

x, y = symbols('x y')
f = sqrt(25 - (x ** 2))
fy = Derivative(f, x).doit()
fy1 = fy.subs({x: 3})
fyy = Derivative(fy, x).doit()
fyy1 = fyy.subs({x: 3})
rho = ((1 + fy1 ** 2) ** 1.5) / fyy1
print(abs(rho))
