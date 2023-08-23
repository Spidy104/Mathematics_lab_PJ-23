from sympy import *

x, y, z = symbols('x y z')
w = x ** 2 * y + y ** 2 * z + z ** 2 * x
wx = diff(w, x)
wy = diff(w, y)
wz = diff(w, z)
print(simplify(wx + wy + wz))
