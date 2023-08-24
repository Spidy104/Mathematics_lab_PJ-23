import numpy as np
y = [5026, 5674, 6362, 7088, 7854]
x = [i for i in range(80, 105, 5)]
h = x[1] - x[0]
x_r = 105
q = (x_r - x[-1]) / h
prod = q
k = 1
sum = y[-1]
for i in range(len(x) - 1):
    y = np.diff(x)
    sum += prod*y[-1]
    prod *= (q+k) / (k+1)
    k += 1
    print('delta^', i+1, y)
    print(sum, prod)
print('Approximation of y at x_r = 105 is:', sum)