import matplotlib.pyplot as plt

x, y, u, v = [0, 0], [0, 0], [2, 1], [3, 1]
plt.quiver(x, y, u, v, units='xy', scale=1)
plt.title('PLOT OF TWO VECTORS')
plt.xlim(-2, 6)
plt.ylim(-2, 4)
plt.grid()
plt.show()
