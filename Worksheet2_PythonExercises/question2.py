#(2) Write a script to convert the decimal number D into binary.
dec=int(input("Enter a decimal number:"))
binary_number=""
while dec > 0:
    remainder=dec%2
    binary_number=str(remainder)+binary_number
    dec=dec//2
print(binary_number)




