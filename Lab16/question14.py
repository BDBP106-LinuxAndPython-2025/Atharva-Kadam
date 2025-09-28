#(14) Write a program to remove all occurrences of an element from a list, L.
l=input("Enter the list elements :").split()
L=list(l)
for num in range(len(L)):
    L[num]=int(L[num])
print(L)
ele=int(input("Enter the element to be removed:"))
new_list=[]
for num in L:
    if num!=ele:
        new_list.append(num)

print(new_list)
