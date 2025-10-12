# (1) Write a program to convert temperature in Celsius to Fahrenheit using map function.

def temp_conversion(temp_C):
    temp_C=(temp_C*(9/5)) + 32
    return temp_C

temp_in_C=map(int,input("Enter temperature in Celsius:").split())
temp_in_F=map(temp_conversion,temp_in_C)
print(list(temp_in_F))

