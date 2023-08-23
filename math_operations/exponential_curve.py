import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.001)
y1 = np.exp(x)
plt.plot(x, y1, color="c", linestyle="--", label="e^x curve")
plt.title("Exponential Curve")
plt.grid()
plt.xlabel('X - AXIS')
plt.ylabel('Y - AXIS')
plt.legend()
plt.show()
