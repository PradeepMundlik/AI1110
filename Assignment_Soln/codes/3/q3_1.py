from os import rename
import numpy as np
import matplotlib.pyplot as plt
import scipy

v = np.loadtxt("../1/uni.dat",dtype="double")

def modify(t):
	return -2*np.log(1-t)
	
a = modify(v)

x = np.linspace(-10,10,60)
x_1 = np.linspace(-10,10,1000)

err = []
#v = np.loadtxt("q31.dat",dtype="double")

N = len(a)

for i in range(60):
    err_ind = np.nonzero(a < x[i]) 
    err_n = np.size(err_ind)
    err.append(err_n/N) 

def cdf(x):
    if x < 0 : x = 0
    return 1 - np.exp(-x/2)

v_cdf = scipy.vectorize(cdf)


plt.plot(x_1,v_cdf(x_1))#plotting the CDF-
plt.plot(x[0:60].T,err,'o')
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig("../../figs/3/q3_1.pdf")
plt.savefig("../../figs/3/q3_1.eps")
