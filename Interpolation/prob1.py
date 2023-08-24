import numpy as np
x = [i * 5 for i in range(1, 6)]
y = [26, 101, 226, 401, 626]
h = x[1] - x[0]
x_r = 7
p = (x_r - x[0]) / h
prod = p
k = 1
sum = y[0]
for i in range(len(x) - 1):
    y = np.diff(x)
    sum += prod*y[0]
    prod *= (p-k) / (k+1)
    k += 1
    print('delta^', i+1, y)
    print(sum, prod)
print('Approximation of y at xr = 1420 is:', sum)