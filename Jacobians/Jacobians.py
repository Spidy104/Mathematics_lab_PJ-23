from sympy import *

x, y = symbols('x y')
u = x + ((y ** 2) / x)
v = (y ** 2) / x
dux, duy = diff(u, x), diff(u, y)
dvx, dvy = diff(v, x), diff(v, y)
J = Matrix([[dux, duy], [dvx, dvy]])
print(J)
Jac = det(J).doit()
print("The Jacobian value is:", simplify(Jac))