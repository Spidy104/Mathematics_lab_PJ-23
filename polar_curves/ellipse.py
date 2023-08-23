from pylab import *
from random import randint

theta = linspace(0, 2 * pi, 1000)
a = randint(1, 10)
b = randint(1, 10)
r = (a * b) / sqrt(a * (sin(theta) ** 2) + b * (cos(theta) ** 2))
polar(theta, r, 'c')
title('ELLIPSE')
print('OUTPUT')
show()
