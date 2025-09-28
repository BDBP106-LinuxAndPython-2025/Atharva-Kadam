# (10) Write a program to find the even numbers in a list, L.
n = int(input("Number of elements to be entered: "))
str_list = []
for _ in range(n):
     num = int(input("Enter a number: "))
     str_list.append(num)
     even_list=[]
     for n in (str_list):
          if n % 2 == 0:
              even_list.append(n)
print(f'The list of elements entered by user: {str_list}')
print(f'The list of even numbers among the entered elements :{even_list}')



