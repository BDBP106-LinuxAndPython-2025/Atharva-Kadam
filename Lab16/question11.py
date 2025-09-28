# (11) Write a program to print the duplicate elements in a list, L
L=list(map(int,input("ENTER THE ELEMENTS FOR LIST:").split()))
print(f'The entered list is:{L}')
dup=[]
for i in range(len(L)):
    count=0
    for j in range(len(L)):
       if L[i]==L[j]:
         count+=1
    if count > 1:
     dup.append(L[i])
print(f'The elements which are duplicated are:{dup}')
#sorting
for i in range(len(dup)):
    for j in range(i+1,len(dup)):
        if dup[i] > dup[j]:
            dup[i],dup[j]=dup[j],dup[i]
print(dup)


