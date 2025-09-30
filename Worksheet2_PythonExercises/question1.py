#(1) Write a script to find the sum of squares of first N numbers
N=int(input("Enter the value of 'N':"))
sum=0
for i in range(0,N+1):
    square=i**2
    sum+=square
print(sum)
