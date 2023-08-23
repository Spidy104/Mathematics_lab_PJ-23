from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = x * i + y * j + z * k
print(curl(f))