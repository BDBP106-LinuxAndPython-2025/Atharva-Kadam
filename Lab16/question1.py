#(1) Write a script to convert the binary number B into decimal.
bin_num=int(input("Enter a Number"))
bin_num_str = str(bin_num)
for digit in bin_num_str:
  if digit != "0" and digit != "1":
    print("Enter a Binary Number")
    break
else:
 power =0
 decimal=0
 for digit2 in bin_num_str[::-1]:
    decimal += int(digit2)*(2**power)
    power +=1
 print(f"The decimal number of the binary number {bin_num} is: {decimal}")

