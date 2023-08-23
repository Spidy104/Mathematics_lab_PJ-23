from sympy import *

x, y = symbols('x y')
u = atan((2 * x * y) / (x ** 2 - y ** 2))
uxx = diff(u, x, x)
uyy = diff(u, y, y)
w1 = simplify(uxx + uyy)
print("VERIFIED") if w1 == 0 else print("NOT VERIFIED")
