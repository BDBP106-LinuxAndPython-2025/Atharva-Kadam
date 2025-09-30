#(9) Write a program to find the minimum and maximum number in a list, L.
L=input("Enter the elements:")
L1=list(L)
max=int(L1[0])
min=int(L1[0])
for i in L1:
    i=int(i)
    if i>max:
        max=i
    else:
        continue
    if i<min:
        min=i
    else:
        continue
print(f"The maximum element is:{max}")
print(f"The minimum element is:{min}")