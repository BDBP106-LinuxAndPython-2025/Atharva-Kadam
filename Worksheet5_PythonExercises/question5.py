"""(5) Define a module called prime that contains a function isPrime() that returns whether
the passed argument is prime or not. Using this module and function, write another
program containing a function printPrimes() that prints the first n prime numbers."""
import prime as p
def printPrimes(n):
    for i in range(2,n+1):
        if p.isPrime(i)=="Prime":
            print(i,end=",")


printPrimes(10)

