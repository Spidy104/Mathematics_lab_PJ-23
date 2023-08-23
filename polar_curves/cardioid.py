import numpy as np
import pylab

theta = pylab.linspace(0, 2*np.pi, 1000)
r_2 = 5*(1 + pylab.cos(theta))

pylab.polar(theta, r_2, 'g')
pylab.show()