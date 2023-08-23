from sympy import *

x, y, z = symbols('x y z')
u = y/z + z/x
ux = diff(u, x)
uy = diff(u, y)
uz = diff(u, z)
w1 = simplify(x * ux + y * uy + z * uz)
print("VERIFIED") if w1 == 0 else print("UNVERIFIED")
