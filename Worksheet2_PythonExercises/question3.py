#(3) Write a script that computes the number of 1s in a binary representation of a decimal number, N.
dec=int(input("Enter a decimal number:"))
binary_number=""
while dec > 0:
    remainder=dec%2
    binary_number=str(remainder)+binary_number
    dec=dec//2
print(binary_number)
count=0
for i in binary_number:
    if i=="1":
        count+=1
print(f"Number of 1s in the binary representation is:{count}")
