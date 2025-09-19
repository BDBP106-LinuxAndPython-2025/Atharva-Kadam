a=float(input("Enter value of side a:"))
b=float(input("Enter value of side b:"))
c=float(input("Enter value of side c:"))
if a == b == c:
    print("It is an Equilateral triangle")
elif a == b or b == c or a == c:
    print("It is an Isosceles triangle")
else:
    print("It is a Scalene Triangle")