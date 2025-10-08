"""(2) Lists and do loops
(i) Using a simple do loop structure or list comprehension, find the sum of elements
in the above list a.
(ii) Define another list b (using list comprehension again!) containing prime numbers
from 1 to 50.
(iii) Using a do loop structure, collect all the common numbers in a and b into a new
list c."""
a=[i for i in range(1,51)]
print(a)

#(i)
S=sum([i for i in a ])
print(f"The sum of elements is: {S}")

#(ii)Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b=[i for i in range(1,51) if len([j for j in range(2,i) if i%j==0])==0]
"""outer for loop iterates over elements from 1 to 50. then the if len()block checks if the number is divisible by the numbers 2 till the number itself and if there is no divisor that means it's a prime number and it gets added to the list """
print(b)

#(iii)Using a do loop structure, collect all the common numbers in a and b into a new list c
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(f"The list containing common elements of a and b is:{c}")