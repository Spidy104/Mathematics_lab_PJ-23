from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = 3 * pow(y, 4) * pow(z, 2) * i + 4 * pow(x, 2) * pow(z, 2) * j - 3 * pow(x, 2) * pow(y, 2) * k
print('Solenoidal') if divergence(f) == 0 else print('NOT SOLENOIDAL')