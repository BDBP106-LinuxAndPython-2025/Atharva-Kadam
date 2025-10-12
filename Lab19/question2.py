# (2) Write the above program using lambda expression.

def temp_conversion(temp_C):
    temp_C=(temp_C*(9/5)) + 32
    return temp_C

celsius=list(map(int,input("Enter the temperature in Celsius:").split()))
converted_temp=(list(map(lambda temp_C:(temp_C*(9/5)) + 32,celsius)))
print(converted_temp)
