from sympy.vector import *

C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = 3 * x * y * i + 20 * y * pow(z, 2) * j - 15 * x * z * k
print('Solenoidal') if divergence(f) == 0 else print('NOT SOLENOIDAL')
