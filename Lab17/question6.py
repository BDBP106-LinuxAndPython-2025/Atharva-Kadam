#(6) Write a program with a function to calculate the area of a triangle using the formula,where a,b, c are sides of the triangle, also providing a test case output from the program Area= s(s − a)(s − b)(s − c) where 2s = a + b + c.

import math

def area_triangle(a, b, c):
    s=(a+b+c)/2
    Area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(Area)

#A test case output for the program is
area_triangle(2,3,4)

#if input were to be taken from user
def area_triangle2():
    a=int(input("Enter the first side: "))
    b=int(input("Enter the second side: "))
    c=int(input("Enter the third side: "))
    s=(a+b+c)/2
    Area2= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(Area2)
area_triangle2()