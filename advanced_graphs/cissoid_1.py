from sympy import Eq, symbols, plot_implicit

x, y = symbols('x y')
a = 2
eq = Eq((y ** 2) * (a - x), x ** 3)
_ = plot_implicit(eq, (x, -2, 5), (y, -5, 5), title="$Cissiod: y^2(a-x)=x^3, a > 0$", line_color='g')
