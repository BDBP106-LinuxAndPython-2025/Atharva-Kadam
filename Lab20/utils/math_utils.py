"""Inside utils create two python files called math_utils.py and string_utils.py.
The former should contain functions to perform operations such as addition, subtraction,
multiplication, division and getting remainder with two numbers as inputs. The latter file
should contain functions to convert lower case to upper case, upper case to lower case and
to concatenate strings. In a different program, import math_utils and string_utils to
use the modules to print the output for the following: a) 34 and 45, b) ’BDBH’ and ’101’."""
def add(num1,num2):
    addition=num1+num2
    return f'The addition is {addition}'
def sub(num1,num2):
    return f'The subtraction is {num1-num2}'
def multiply(num1,num2):
    return f'The multiplication is {num1*num2}'
def divide(num1,num2):
    return f'The division is {num1/num2}'
def remainder(num1,num2):
    return f'The remainder is {num1%num2}'


