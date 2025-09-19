number=int(input("Enter the number: "))
reverse=""
number_str=str(number)
for i in number_str:
    reverse=i + reverse
print(reverse)