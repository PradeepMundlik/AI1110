'''Pradeep Mundlik AI21BTECH11022'''

'''We can see in plot that Y vs Z is straight line.'''
import math
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1.05, 0.001)
y = np.exp(np.arcsin(x))
z = np.exp(np.arccos(x)*-1)
plt.plot(x , y, color = 'r', label = 'X vs Y = exp(arcsin(x))' )
plt.plot(x , z, color = 'b', label = 'X vs Z = exp(-1*arccos(x))')
plt.plot(y, z, color = 'g', label = 'Y vs Z')
plt.grid()
plt.legend(loc = 'right')
plt.show()