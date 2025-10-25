import math
def isPrime(x):
    if x==1:
        return "It is not prime."
    for i in range(2,x):
        if x%i==0:
          return "Not prime"
    return "Prime"


# print(isPrime(8))