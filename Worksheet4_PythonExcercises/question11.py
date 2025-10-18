"""(11) How would you read and write binary data to a file? Illustrate with suitable programs."""
basedir='/Users/athar/Worksheet4-Python Excercises/'
f=open(basedir+'question11.txt','wb')
f.write(b"hello")
f.close()

basedir='/Users/athar/Worksheet4-Python Excercises/'
e=open(basedir+'question11.txt','rb')
b=e.read()
print(b)
e.close()


