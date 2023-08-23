from sympy import *
from sympy.vector import *

C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
f = pow(x, 2) + pow(y, 2) - z
delop = Del()
vec = delop(f).subs({x: 1, y: 1, z: 2}).evalf()
F = vec / (sqrt(vec.dot(vec)))
print(simplify(F))
