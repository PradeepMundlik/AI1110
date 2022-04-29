'''Name: Pradeep Mundlik'''
'''Roll no: AI21BTECH11022'''
'''AI1110 Assignment 1'''
'''Question 6(b) ICSE 2019'''

a = float(input("Enter first term : ")) #first term
l = float(input("Enter last term : ")) # last term
r = float(input("Enter common ratio : ")) # common ratio
'''
    a, a*r, a*r^2, a*r^3,......, a*r^(n-1)
    nth term = a*r^(n-1)
    l = a*r^(n-1)
    r^(n-1) = (l/a)
    L/(r*r*r*r*....(n-1 times r)) = a
    So, if we continously divide l by r until it becomes equal to a,
    and count all operations needed then it will give n-1.
'''
def number_of_terms(a,l,r): #counts number of terms. 
    n = 1 #number of terms initialized as 1 as we need to consider a first. 
    while(l != a):
        l = l / r
        n += 1
    return n 

n = number_of_terms(a,l,r)

def calculate_sum(a,r,n):
    # To calculate sum of all terms, we will use loop. 
    sum = 0 # initializing sum as zero.
    i = 0
    while(i<n):
        sum = sum + a
        a = a*r
        i += 1
    return sum

sum = calculate_sum(a,r,n)

#priniting all results.
print("\nNumber of terms in given GP sequence is", n)
print("Sum of all terms in given GP sequence is", sum)