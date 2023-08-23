from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = 3 * pow(y, 4) * pow(z, 2) * i + 4 * pow(x, 2) * pow(z, 2) * j - 3 * pow(x, 2) * pow(y, 2) * k
g = 0 * i + 0 * j + 0 * k
print('Irrotational') if curl(f) == g else print('NOT Irrotational')
print(curl(f))
