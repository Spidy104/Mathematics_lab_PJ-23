import matplotlib.pyplot as plt
from random import randint

x = [_ for _ in range(20)]
y = [randint(1, 21) for _ in range(20)]
plt.scatter(x, y)
plt.xlabel('X - AXIS')
plt.ylabel('Y - AXIS')
plt.title('MY SCATTER GRAPH')
plt.grid()
plt.show()
