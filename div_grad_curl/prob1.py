from sympy import *
from sympy.vector import *

C = CoordSys3D('')
# x, y, z = symbols('x y z')
x, y, z = C.x, C.y, C.z
f = x ** 2 + y ** 2 + z ** 2
delop = Del()
F = delop(f).doit()
print("GRAD IS: ")
print(simplify(F))
