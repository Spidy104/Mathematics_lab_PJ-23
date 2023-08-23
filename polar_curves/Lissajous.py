import matplotlib.pyplot as plt
import numpy as np


def lissajous(a, b, c, n):
    x = []
    y = []
    print('OUTPUT:')
    for theta in np.linspace(-5, 5, 1000):
        x.append(a * np.sin(n * theta + c))
        y.append(b * (np.sin(theta)))
    plt.plot(x, y)
    plt.title('Lissajous Curves')
    plt.show()


lissajous(2, 1, np.pi / 3, 3)
