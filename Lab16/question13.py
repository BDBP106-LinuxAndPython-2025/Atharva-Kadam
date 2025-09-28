#(13) Write a program to extract elements of a list, if it occurs more than k times.
inp=input("Enter the elements:").split()
for i in range(len(inp)):
    inp[i]=int(inp[i])
print(inp)
extract=int(input("Enter the value of k:"))
rep=[]
for i in inp:
    if inp.count(i) > extract:
        rep.append(i)
print(rep)



