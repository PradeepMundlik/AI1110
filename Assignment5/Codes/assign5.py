#P(A) = 0.3
#P(B) = 0.4
P_A = 0.3
P_B = 0.4
print(f"P(A intersection B) = {P_A*P_B}")
print(f"P(A union B) = {P_A + P_B - P_A*P_B}")
print(f"P(A|B) = {P_A}")
print(f"P(B|A) = {P_B}")