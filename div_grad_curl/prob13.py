from sympy.vector import *

C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = 3 * x * y * i + 20 * y * pow(z, 2) * j - 15 * x * z * k
g = 0 * i + 0 * j + 0 * k
print('Irrotational') if curl(f) == g else print('NOT Irrotational')
print(curl(f))
