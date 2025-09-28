# (6) Write print alternate characters of a string, S
string=str(input("Enter a string"))
result=""
for i in range(0,len(string),2):
    result+=string[i]
print(result)

