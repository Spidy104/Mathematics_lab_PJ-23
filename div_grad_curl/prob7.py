from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = 3 * pow(x, 2) * y * i - pow(y, 3) * pow(z, 2) * j + x * y * pow(z, 2) * k
div = divergence(f)
print("The divergence of the vector is")
print(simplify(div))