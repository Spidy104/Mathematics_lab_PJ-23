from sympy import plot_implicit, symbols, Eq

x, y = symbols('x y')
eqn = Eq(x ** 2 + y ** 2, 4)
_ = plot_implicit(eqn, (x, -10, 10), (y, -10, 10), title='$Circle:x^2+y^2=4$')
