import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.001)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, "g--", label='SINE CURVE')
plt.plot(x, y2, "c--", label='COSINE CURVE')
plt.grid()
plt.title('SINE AND COSINE VALUES')
plt.xlabel('Angles(in radians)')
plt.ylabel('Corresponding sine and cosine values')
plt.legend()
plt.show()
