from sympy import Eq, symbols, plot_implicit

x, y = symbols('x y')
a = 4
eq = Eq((y ** 2) * (4 - x), x ** 3)
_ = plot_implicit(eq, (x, -10, 10), (y, -10, 10), title="$Cissiod: y^2(a-x)=x^3, a > 0$", line_color='c')
