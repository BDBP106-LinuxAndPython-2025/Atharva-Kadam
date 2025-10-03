#(8) Write a program to interchange the even and odd components of an input list. The list can contain any type of variables. Output the result for the following example:[23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]
L=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, True,'hit']
L2=[]
for i in range(0,len(L)):
    if i % 2 ==0:
        temp=L[i]
    else:
        L2.append(L[i])
        L2.append(temp)

print(L2)


