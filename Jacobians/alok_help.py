from sympy import *

# f = xy + ((a ^3)/ ( x ^ 2)) + ((a ^ 3) / (x ^ 2))

x, y, a = symbols('x y a')
f = x * y + ((a ** 3) / x) + ((a ** 3) / y)
dx, dy = diff(f, x), diff(f, y)
eq1, eq2 = Eq(dx, 0), Eq(dy, 0)
sol = solve([eq1, eq2], (x, y))
dx2, dy2, dyx = diff(dx, x), diff(dy, y), diff(f, y, x)
r = dx2.subs({x: sol[0][0], y: sol[0][1]}).evalf()
s = dyx.subs({x: sol[0][0], y: sol[0][1]}).evalf()
t = dy2.subs({x: sol[0][0], y: sol[0][1]}).evalf()
dis = r * t - s ** 2
if dis > 0 and r > 0:
    print("Minima at {} and {}".format(sol[0][0], sol[0][1]))
    q1 = f.subs({x: sol[0][0], y: sol[0][1]}).evalf()
    print("The minima is {}".format(q1))
elif dis > 0 > r:
    print("Maxima at {} and {}".format(sol[0][0], sol[0][1]))
    q1 = f.subs({x: sol[0][0], y: sol[0][1]}).evalf()
    print("The maxima is {}".format(q1))
elif dis < 0:
    print("{} and {} is a saddle point".format(sol[0][0], sol[0][1]))
else:
    print("It requires a bit more investigation")
