from typing import Callable, Any

x0 = float(input("Enter the starting point: "))
xn = float(input("Enter the ending point: "))
h = float(input("Enter the step size: "))
y0 = float(input("Enter the initial condition: "))
m = int(input("Enter the number of the modification: "))
func = lambda x, y: x + y ** 2
y1 = y0 + h * func(x0, y0)
for i in range(m):
    k1 = h * func(x0, y0)
    k2 = h * func(x0 + h, y1)
    y = y0 + 0.5 * (k1 + k2)
    print('Solution at {} is {}'.format(x0 + h, y))
    y1 = y
