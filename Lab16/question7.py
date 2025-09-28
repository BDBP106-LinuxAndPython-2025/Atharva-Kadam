string=str(input("Enter a string:"))
count=0
string2=""
for i in string:
    if i==" ":
        count += 1
    else:
        break
for j in range(count,len(string)):
    string2 += string[j]
print(string2)
