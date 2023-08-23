from sympy import *
from sympy.vector import *
C = CoordSys3D('')
x, y, z = C.x, C.y, C.z
i, j, k = C.i, C.j, C.k
f = pow(x, 2) * y * z * i + x * pow(y, 2) * z * j + x * y * pow(z, 2) * k
div = divergence(f).subs({x: 1, y: 2, z: 3}).evalf().doit()
cur = curl(f).subs({x: 1, y: 2, z: 3}).evalf().doit()
print("The divergence of the vector is")
print(simplify(div))
print('The curl of the vector is')
print(simplify(cur))
