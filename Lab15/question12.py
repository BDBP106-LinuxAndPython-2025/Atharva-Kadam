string=str(input("Enter the string: "))
reverse=""
for i in string:
    reverse=i + reverse
if reverse==string:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")