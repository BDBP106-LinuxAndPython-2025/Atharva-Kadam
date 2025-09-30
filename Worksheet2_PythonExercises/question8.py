#(8) Write a program to find the sum and average of numbers in a list, L.
L=input("Enter the elements:")
L1=list(L)
sum=0
for i in L1:
    i=int(i)
    sum+=i
avg=sum/len(L)
print(f"The sum of all elements of the list is :{sum}")
print(f"The average of all elements of the list is :{avg}")