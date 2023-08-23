from sympy import *
from numpy import *
from matplotlib.pyplot import *
x, y, z, t = symbols('x y z t')
f = Function(t)
eq = Eq(f(t).diff(t), (2*t / (1 - t**2)) * f(t) - 1)
an_sol = dsolve(eq, hint='1st_linear', ics = {f(1) : 2})
print(an_sol)
lmbd_sol = lambdify(t, an_sol.rhs)
t_range = linspace(0, 5, 50)
Y = [lmbd_sol(ti) for ti in t_range]
T = array(t_range)
Z = array(Y)
plot(T, Z)
show()
