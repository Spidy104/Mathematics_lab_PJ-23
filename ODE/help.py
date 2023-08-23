from sympy import *
from matplotlib.pyplot import show
from sympy.plotting import plot

x = symbols('x')
y = Function('y')(x)
yd = y.diff(x)
eq = Eq(yd, x + y)
ysol = dsolve(eq, y, ics={y.subs(x, 0) : 2})
an_sol = ysol
print(an_sol)
plot(ysol.rhs, (x, 0, 0.5))
show()
