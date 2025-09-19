number = str(input("Enter a number: "))
reverse=number[::-1]
if number == reverse:
    print ("Number is palindrome")
else:
    print ("Number is not a palindrome")
#Method2
a=int(input("Enter a number: "))
b=str(a)
temp=a
reverse=""
while temp>0:
    remainder=temp%10
    remain_str=str(remainder)
    reverse=reverse+remain_str
    temp=temp//10
if b==reverse:
        print(f'It is Palindrome')
else:
        print(f'It is Not Palindrome')
