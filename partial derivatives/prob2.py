from sympy import *

x, y = symbols('x y')
u = ln((x ** 2 + y ** 2) / (x + y))
ux = diff(u, x)
uy = diff(u, y)
w1 = simplify(x * ux + y * uy)
print("VERIFIED") if w1 == 1 else print("NOT VERIFIED")
