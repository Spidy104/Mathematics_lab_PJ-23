from numpy import *
import matplotlib.pyplot as plt

x, y = meshgrid(linspace(-5, 5, 10), linspace(-5, 5, 10))
u, v = -y/hypot(x, y), x/hypot(x, y)
plt.subplot(1, 3, 1)
plt.quiver(x, y, u, v, color='g')
plt.title('VECTOR FIELD')
plt.subplot(1, 2, 2)
plt.streamplot(x, y, u, v, color='b')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.show()