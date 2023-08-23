from numpy import *


def seidel(a, x, b):
    n = len(a)
    for j in range(n):
        d = b[j]
        for i in range(n):
            if j != i:
                d = d - a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x


a = array([[27.0, 6.0, -1.0], [6.0, 15.0, 2.0], [1.0, 1.0, 54.0]])
x = array([[0.0], [0.0], [0.0]])
b = array([[85.0], [72.0], [110.0]])
for i in range(100):
    x = seidel(a, x, b)
print("The solution of the system is: ", x)
