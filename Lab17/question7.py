#(7) Write a program with a function to find whether a given triangle with sides a, b, c is isosceles, scalene or equilateral triangle, also provide a test case output from the program.
def check_triangle(a,b,c):
    if a==b==c:
     print("Triangle is Equilateral")
    elif a==b or b==c or c==a :
        print("Triangle is Isosceles")
    elif a!=b!=c:
        print("Triangle is Scalene")

#Test output
check_triangle(6,3,1)
check_triangle(5,5,2)
check_triangle(4,4,4)

