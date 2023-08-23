from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
f = 3 * pow(x, 2) * y - (pow(y, 3) * pow(z, 2))
delop = Del()
F = delop(f).doit()
print("GRAD IS:")
print(simplify(F))