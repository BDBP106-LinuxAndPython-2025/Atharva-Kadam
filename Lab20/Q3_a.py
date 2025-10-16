#method1
basedir='/home/ibab/Atharva-Kadam/Lab20/'
a=open(basedir+"stringmatrix.dat","w")
print(a)
for i in range(65,65+13):
    row1=""
    row2=""
    row3=""
    for j in range(65,69):
        row1+=chr(j)
        row1+=' '
    for g in range(69,73):
        row2+=chr(g)
        row2+=' '
    for h in range(73,77):
        row3+=chr(h)
        row3+=' '
a.write(row1 + "\n" + row2 + "\n" + row3 )

a.close()


# method2

dic={}
for i in range(65,77):
        key=i
        value=chr(i)
        dic[key]=value
print(dic)

count=0
for key,value in dic.items():
    print(value,end=" ")
    count+=1
    if count==4:
        print()
        count=0
        continue
a.close()

