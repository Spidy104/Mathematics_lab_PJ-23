from random import randint

from sympy import Eq, plot_implicit, symbols

x, y = symbols('x y')
a = randint(1, 6)
eq = Eq((a * y) ** 2, x ** 2 * (a ** 2 - x ** 2))
plot_implicit(eq, (x, -10, 10), (y, -10, 10), title="Lower half of circle")
