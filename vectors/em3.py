from numpy import *
import matplotlib.pyplot as plt

x, y = meshgrid(arange(-5, 5, 0.1), arange(-5, 5, 0.1))
u = ((x + 1) / (pow(x+1, 2) + pow(y, 2))) - ((x-1) / (pow(x-1, 2) + pow(y, 2)))
v = (y / (pow(x + 1, 2) + pow(y, 2))) - (y / (pow(x - 1, 2) + pow(y, 2)))
plt.subplot(1, 3, 1)
plt.quiver(x, y, u, v, color='g')
plt.title('VECTOR FIELD')
plt.subplot(1, 2, 2)
plt.title('VECTOR FIELD WITH STREAM LINES')
plt.streamplot(x, y, u, v, color='b')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.show()
