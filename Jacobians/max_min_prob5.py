"""
prob 6
Find numbers such that the sum of three numbers is constant and their product is maximum
therefore let's assume x + y + z = a, f=xyz
z = a - x - y
f = xy(a - x - y)
"""
from sympy import *
from random import randint

x, y = symbols('x y')
a = randint(1, 10)
f = x * y * (a - x - y)
dx, dy = diff(f, x), diff(f, y)
eq1, eq2 = Eq(dx, 0), Eq(dy, 0)
sol = solve([eq1, eq2], (x, y))
dx2, dy2 = diff(dx, x), diff(dy, y)
dyx = diff(f, y, x)


def return_value():
    max_value = None
    for i, j in sol:
        r = dx2.subs({x: i, y: j})
        s = dyx.subs({x: i, y: j})
        t = dy2.subs({x: i, y: j})
        dis = r * t - (s * s)
        if dis > 0 > r:
            max_value = (i, j)
            break
        else:
            continue
    return max_value


val = return_value()
try:
    third = a - sum(val)
    print("The required numbers are {}, {}, {}".format(val[0], val[1], third))
except TypeError:
    print("There are no numbers")

