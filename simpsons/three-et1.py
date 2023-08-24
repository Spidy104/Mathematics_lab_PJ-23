from numpy import *
a = 1
b = 2.8
h = 0.2
n = 9
x = linspace(a, b, 10)
print(x)
y = (pow(x, 2) - 1) / (pow(x, 2) + 1)
print('Y values are:', y)
sum = 0
for i in range(1, n):
    if i % 3 == 0:
        sum += 2*y[i]
    else:
        sum += 3 * y[i]
I = (3 * (h / 8)) * (y[0] + y[-1] + sum)
print('Approximation of the Integral is', I)