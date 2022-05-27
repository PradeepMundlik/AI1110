import numpy as np
from matplotlib import pyplot as plt

n = [i for i in range(1,1001)]
P = []
for i in n:
    A = np.random.choice([1,2,3,4,5,6],size=(i,2))
    Bool = False
    for j in A:
        if j[0]==6 and j[1]==6: 
            Bool = Bool or True 
            break
    P.append(1) if Bool else P.append(0)
    
plt.scatter(n,P,label="Actual Probability")
X = np.arange(0,1000,0.01)
Y = 1 - np.power(35/36,X)
plt.plot(X,Y,color="r",label="Theoratical Probality")
plt.xlabel("Number of Trials")
plt.ylabel("Probability {atleast one double six}")
plt.grid()
plt.legend(loc = 'right')
plt.show()