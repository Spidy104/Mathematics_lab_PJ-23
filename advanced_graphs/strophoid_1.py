from sympy import Eq, symbols, plot_implicit

x, y = symbols('x y')
a = 2
eq = Eq((y ** 2) * (a - x), (x ** 2) * (a + x))
_ = plot_implicit(eq, (x, -10, 10), (y, -10, 10), title="Strophoid : $y^2 (a-x)=x^2 (a+x), a> 0$", line_color='g')
