import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
plt.plot(x, x, color='c', label='Linear')
plt.plot(x, x ** 2, color='g', label='Quadratic')
plt.plot(x, x ** 3, color='y', label='Cubic')
plt.grid()
plt.title('LINEAR, QUADRATIC AND CUBIC CURVES')
plt.xlabel('X - AXIS')
plt.ylabel('Y - AXIS')
plt.legend()
plt.show()
