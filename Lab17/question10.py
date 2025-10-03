# (10) Write a function called nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter.
# The main program should read an integer from the user and display the first prime
# number larger than the entered value.
def nextPrime(num):
    number = num + 1
    while True:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            break
        number += 1
    print(number)
nextPrime(7)

#main program
n= int(input("Enter a number: "))
nextPrime(n)

