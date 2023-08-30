import matplotlib.pyplot as plt
import numpy as np

x0, xn = list(map(float, input("Enter the starting and ending points: ").split()))
h = float(input("Enter the step size: "))
y0 = float(input("Enter the initial condition: "))
n = (xn - x0) / h
print(n)
f = lambda x, y: (y - x) / (y + x)
y = y0
X = np.zeros(int(n + 2))
Y = np.zeros(int(n + 2))
X[0], Y[0] = 0, 0
for i in range(int(n + 1)):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h / 2, y0 + k1 / 2)
    k3 = h * f(x0 + h / 2, y0 + k2 / 2)
    k4 = h * f(x0 + h, y0 + k3)
    y = y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    print('{} {}'.format(x0, y0))
    x0 += h
    y0 += y
    X[i + 1], Y[i + 1] = x0, y0
plt.plot(X, Y)
plt.grid()
plt.show()
