"""(12) Write a python script that lists out each line of a file prefixed with its line number."""
basedir='/Users/athar/Worksheet4-Python Excercises/'
a=open(basedir+'question12.txt','r')
l1=1
for line in a:
    print(l1,line,end="")
    l1+=1

#method2
# r=a.readlines()
# l=1
# for line in r:
#       print(l,line,end="")
#       l=l+1