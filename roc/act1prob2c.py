import math

from sympy import *

t = symbols('t')
r1 = sqrt(4 * sin(2 * t))
r2 = sqrt(4 * cos(2 * t))
t1 = diff(r1, t)
t2 = diff(r2, t)
phi1 = atan(r1 / t1)
print('The angle between radius vector and tangent is', phi1)
phi2 = atan(r2 / t2)
print('The angle between radius vector and tangent is', phi2)
q = solve(r1 - r2, t)
w1 = t1.subs({t: float(q[1])})
w2 = t2.subs({t: float(q[1])})
y1 = atan(w1)
y2 = atan(w2)
w = abs(y1 - y2)
print("The angle between the curves in radians is", w)
print("The angle between the curves in degrees is", math.degrees(w))
