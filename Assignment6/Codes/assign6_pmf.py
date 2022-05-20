from matplotlib import pyplot as plt


X = [0,1,2,3,4]
#y = pr(x)
k = 0.15
Y = [0.1, k, 2*k, 2*k, k]
plt.grid()
plt.stem(X,Y)
plt.title("PMF")
plt.xlabel("X=x")
plt.ylabel("Pr(X=x)")

# plt.plot(x,y)
plt.show()








