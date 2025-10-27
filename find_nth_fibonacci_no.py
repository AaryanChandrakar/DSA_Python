# Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 55 89 
#            Index: 0 1 2 3 4 5 6  7  8  9 10 11 

# Problem Statement:
"""
if I write n=5, then output must be '5'
and if I write n=7 then, the output must be '13'
similarly for n=9, the output must be '34'.
"""
# Solution using loop
def nth_fibonacci(n):
    a=0
    b=1

    for i in range(n-1):
        temp = b
        b = a+b
        a = temp

    return b

n = 5
print("For n =",n,", Fobonacci Number is:",nth_fibonacci(n))
n = 7
print("For n =",n,", Fobonacci Number is:",nth_fibonacci(n))
n = 9
print("For n =",n,", Fobonacci Number is:",nth_fibonacci(n))

#  Time Complexity: 0(n)
# Space Complexity: 0(1)



# Solution uisng recursion

def nth_fibonacci_rec(n):
    if n==0 or n==1:
        return n
    return nth_fibonacci(n-1) + nth_fibonacci_rec(n-2)

n = 9
print("For n =",n,",(using recursion) Fobonacci Number is:",nth_fibonacci_rec(n))
n = 11
print("For n =",n,",(using recursion) Fobonacci Number is:",nth_fibonacci_rec(n))

#  Time Complexity: 0(2^n)
# Space Complexity: 0(2^n)

#Attempt the question on GFG related to this.