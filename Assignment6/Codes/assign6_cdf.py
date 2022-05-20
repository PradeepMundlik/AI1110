from matplotlib import pyplot as plt


X = [0,1,2,3,4]
#y = pr(x)
k = 0.15
Y = [0.1, k, 2*k, 2*k, k]

s = 0
cdf = []
for i in Y:
    s += i
    cdf.append(s)

plt.grid()
plt.stem(X,cdf)
plt.title("CDF")
plt.xlabel("X=x")

# plt.plot(x,y)
plt.show()