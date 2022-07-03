from os import rename
import numpy as np
import matplotlib.pyplot as plt
import scipy

a = np.loadtxt("../1/uni.dat")
# print(a)
a = 1 - a
a = np.array([i for i in a if i>0])
a = np.log(a)
a = -2*a
# print(a)
with open("q31.dat",'w') as f:
    for i in a:
        f.write(str(i)+"\n")

x = np.linspace(-10,10,60)
x_1 = np.linspace(-10,10,1000)

err = []
v = np.loadtxt("q31.dat",dtype="double")
N = len(v)

for i in range(60):
    err_ind = np.nonzero(v < x[i]) 
    err_n = np.size(err_ind)
    err.append(err_n/N) 

def cdf(x):
    if x < 0 : x = 0
    return 1 - np.exp(-x/2)

v_cdf = scipy.vectorize(cdf)


plt.plot(x_1,v_cdf(x_1))#plotting the CDF
plt.plot(x[0:60].T,err,'o')
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig("../../figs/3/q3_1.pdf")
plt.savefig("../../figs/3/q3_1.eps")