"""(4) Define a module called factorial that contains a function to find the factorial of a given
integer. Using this function, find the permutation and combination of the given inputs."""
import factorial
print(f"The factorial of the integer is :{factorial.find_factorial(4)}")

def permutation(x,y):
    z=x-y
    p=factorial.find_factorial(x)//factorial.find_factorial(z)   #permutation(x,y)=x!/(x-y)!
    return p

def combination(x,y):
    z=x-y                                                         #combination(x,y)=x!/y!(x-y)!
    c=factorial.find_factorial(x)//(factorial.find_factorial(y)*factorial.find_factorial(z))
    return c

print(f"There are {permutation(4,3)} permutations.")
print(f"There are {combination(4,3)} combinations.")