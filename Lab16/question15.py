#(15) Write a program to extract words from a string list, L whose first character is k.
l=input("Enter the elements:").split()
L=list(l)
k=input("Enter the element k:")
new=[]
for ch in L:
    if ch.startswith(k):
        new.append(ch)
print(new)
