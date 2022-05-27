from cProfile import label
import numpy as np
from matplotlib import pyplot as plt

n = [i for i in range(1,1001)]
P = []
for i in n:
    A = np.random.choice([1,2,3,4,5,6],size=(i,2))
    B = [j for j in A if j[0]+j[1] != 7]
    P.append(len(B)/len(A))
plt.scatter(n,P,label="Actual Probability")
X = np.arange(0,1000,0.01)
Y = 1 - np.power(5/6,X)
plt.plot(X,Y,color="r",label="Theoratical Probality")
plt.xlabel("Number of Trials")
plt.ylabel("Probability {Not Seven}")
plt.grid()
plt.legend(loc = 'right')
plt.show()