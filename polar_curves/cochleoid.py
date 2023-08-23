from pylab import *
from random import randint

t = linspace(1, 2 * pi, 1000)
a = randint(1, 10)
r = (a * sin(t)) / t
polar(t, r, 'c')
title('cochleoid')
print('OUTPUT:')
show()
