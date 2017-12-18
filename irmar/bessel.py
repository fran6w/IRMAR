# fonctions de Bessel

from numpy import linspace, pi
from scipy.special import jn
from matplotlib.pylab import plot

x = linspace(0, 4*pi)
for i in range(5,-1,-1):
    plot(x, jn(i, x))
