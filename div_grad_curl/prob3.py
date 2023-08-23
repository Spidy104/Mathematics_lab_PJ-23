from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
f = pow(x, 2) * pow(y, 2) * pow(z, 3)
delop = Del()
F = delop(f).subs({x: 1, y: -1, z: 2}).evalf().doit()
print("GRAD IS:")
print(simplify(F))