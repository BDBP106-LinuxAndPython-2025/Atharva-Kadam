#(3) Write a script to check if a given number, N, is prime or not
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is NOT a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a PRIME number")
    else:
        print("It is not a prime number")
