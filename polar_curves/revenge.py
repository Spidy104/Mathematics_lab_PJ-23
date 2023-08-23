from sympy import symbols, plot_implicit, Eq

x, y = symbols('x y')
a = 2
eq = Eq(x ** (2/ 3) + y ** (2/3), a ** (2/3))
plot_implicit(eq, (x, -5, 5), (y, -5, 5))