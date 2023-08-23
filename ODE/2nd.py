from sympy import *
from matplotlib.pyplot import show
from sympy.plotting import plot

t = symbols('t')
y = Function('y')(t)
yd = y.diff(t)
ydd = y.diff(t, 2)
eq = Eq(ydd - 2 * yd + y, sin(t))
ysol = dsolve(eq, y, ics={y.subs(t, 0): 1, yd.subs(t, 0): 0})
an_sol = ysol
print(an_sol)
plot(ysol.rhs, (t, 0, 0.5))
show()
