import numpy as np
x = [i for i in range(3, 10)]
y = [4.8, 8.4, 14.5, 23.6, 36.2, 52.8, 73.9]
h = x[1] - x[0]
x_r = 1
x_r0 = 0
p = (x_r - x[0]) / h
p1 = (x_r0 - x[0]) / h
prod, prod1 = p, p
sum, sum1 = y[0], y[0]
k = 1
for i in range(len(x) - 1):
    y = np.diff(x)
    sum += prod * y[0]
    sum1 += prod1 * y[0]
    prod *= (p-k) / (k+1)
    prod1 *= (p1 - k)/(k + 1)
    k += 1
    print('delta^', i+1, y)
    print(sum, prod)
    print('delta^', i+1, y)
    print(sum1, prod1)
print('Approximation of y at x_r=1 is:', sum)
print('Approximation of y at x_r=0 is:', sum1)