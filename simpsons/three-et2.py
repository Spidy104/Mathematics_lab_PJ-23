from numpy import *
a = 0
b = 1
n = 7
h = (b-a)/n
x = linspace(a, b, n+1)
print(x)
y = 1 / (x+1)
print('Y values are:', y)
sum = 0
for i in range(1, n):
    if i % 3 == 0:
        sum += 2*y[i]
    else:
        sum += 3 * y[i]
I = (3 * (h / 8)) * (y[0] + y[-1] + sum)
print('Approximation of the Integral is', I)