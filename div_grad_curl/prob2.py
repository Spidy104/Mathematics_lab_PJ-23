from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
f = 3 * pow(x, 2) * y - (pow(y, 3) * pow(z, 3))
delop = Del()
F = delop(f).subs({x: 1, y: -2, z: -1}).evalf().doit()
print("GRAD IS:")
print(simplify(F))