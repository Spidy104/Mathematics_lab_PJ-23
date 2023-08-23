from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
f = 4 * pow(x, 2) + 9 * pow(y, 2) + pow(z, 2)
delop = Del()
F = delop(f).subs({x: 5, y: -1, z: -11}).evalf().doit()
print("GRAD IS:")
print(simplify(F))