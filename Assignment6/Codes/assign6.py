k  = (1 - 0.1)/6
print(f"The value of K is {k}")

print(f"Probability that you study atleast two hours a day is {2*k + 2*k + k}")
print(f"Probability that you study exactly two hours a day is {2*k}")
print(f"Probability that you study atmost two hours a day is {0.1 + 2*k + k}")