import numpy as np


S = np.array([(1,1),(1,0),(0,1),(0,0)]) # 0 -> boy and 1 -> girl. # first occurence means younger.
B = np.array([i for i in S if i[0] == 1]) # B represents younger is girl. 
A  = np.array([i for i in B if i[0] == 1 and i[1] == 1]) # A represents both are girls given younger is girl. 
print(f"The conditional probability(theoratically) of both girls given that younger is girl is {len(A)/len(B)}")

W = np.random.choice([0,1], size=(1000,2))
Y = np.array([i for i in W if i[0] == 1]) # Y represents younger is girl.
X = np.array([i for i in Y if i[0] == 1 and i[1] == 1]) # A represents both are girls given younger is girl.
print(f"The conditional probability(experimentally by 1000 experiments) of both girls given that younger is girl is {len(X)/len(Y)}")
