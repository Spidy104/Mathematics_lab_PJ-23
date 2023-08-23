# r = 2 * (1 + cos(t)), r = 2 * (1 + sin(t))
import math

from sympy import *

t = symbols('t')
r1 = 2 * (1 + cos(t))
r2 = 2 * (1 + sin(t))
dr1 = diff(r1, t)
dr2 = diff(r2, t)
t1 = r1 / dr1
phi1 = atan(simplify(t1))
print("The angle between the radius vector and tangent is", phi1)
t2 = r2 / dr2
phi2 = atan(simplify(t2))
print("The angle between the radius vector and tangent is", phi2)
q = solve(r1 - r2, t)
w1 = t1.subs({t:float(q[0])})
w2 = t2.subs({t:float(q[0])})
y1 = atan(w1)
y2 = atan(w2)
w = abs(y1 - y2)
print("The angle between the curves in radians is", w)
print("The angle between the curves in degrees is", math.degrees(w))
