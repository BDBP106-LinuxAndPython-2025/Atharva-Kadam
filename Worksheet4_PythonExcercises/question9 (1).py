"""(9) How do you read a file’s contents one line at a time?"""

'''To read a file's contents one line at a time we can use many methods like:
var1_contents=var1.readlines()
print(var1_contents)
for i in var1_contents:
    print(i.strip())'''

'''for line in var1:
      print(line,end="")'''

'''while True:
      line=var1.readline()
      if not line:
         break
      print(line,end="")'''