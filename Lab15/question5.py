b=int(input("Enter the coefficient of x"))
a=int(input("Enter the coefficient of X^2"))
c=int(input("Enter the constant"))
import cmath
discriminant=(b**2)-(4*a*c)
x=((b + cmath.sqrt(discriminant))/2*a)
y=((b - cmath.sqrt(discriminant))/2*a)
print(f'The 1st root of equation is:{x}')
print(f'The 2nd root of equation is:{y}')