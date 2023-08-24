from numpy import *
a = 4
b = 5.2
n = 6
h = (b - a) / n
x = linspace(a, b, n+1)
print(x)
y = log(x)
print('Y values are', y)
sum = 0
for i in range(1, n):
    if i % 2 == 0:
        sum += 2 * y[i]
    else:
        sum += 4 * y[i]
I = (h/3) * (y[0] + y[-1] + sum)
print('Approximation of the Integral is', I)