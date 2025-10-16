"""Inside utils create two python files called math_utils.py and string_utils.py.
The former should contain functions to perform operations such as addition, subtraction,
multiplication, division and getting remainder with two numbers as inputs. The latter file
should contain functions to convert lower case to upper case, upper case to lower case and
to concatenate strings. In a different program, import math_utils and string_utils to
use the modules to print the output for the following: a) 34 and 45, b) ’BDBH’ and ’101’."""
def upper_to_lower(string):
    string2=""
    for i in string:
        if i.isupper()==True:
             k=i.lower()
             string2+=k
        elif i.islower()==True:
            string2+=i
    return string2


def lower_to_upper(string):
    string2=""
    for i in string:
        if i.islower()==True:
             k=i.upper()
             string2+=k
        elif i.isupper() == True:
            string2 += i
    return string2


def concatenate(str1,str2):
    str3=""
    str3=str1+str2
    return str3


