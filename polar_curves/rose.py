from pylab import *

theta = linspace(0, 2 * pi, 1000)
r = 2 * abs(cos(2 * theta))
polar(theta, r, 'c')
title('Four leaved rose')
print('OUTPUT:')
show()
