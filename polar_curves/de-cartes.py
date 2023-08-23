from sympy import Eq, symbols, plot_implicit
from random import randint

x, y = symbols('x y')
a = randint(1, 6)
eq = Eq(x ** 3 + y ** 3, 3 * a * x * y)
plot_implicit(eq, (x, -10, 10), (y, -10, 10), title='FOLIUM OF DESCARTES')
