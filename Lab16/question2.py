# (2) Write a script that computes power - raise base to the n-th power. Eg. power(2, 5).Here base is 2 and n-th power is 5.
base=float(input("Enter the number:"))
exp=int(input("Enter the exponent:"))
if exp==0:
    print("1")
else:
    result=1
    power=abs(exp)
    for i in range(power):
     result = result * base
    if exp < 0:
     result = 1.0 / result
print(f"{base} raised to the power {exp} is: {result}")






