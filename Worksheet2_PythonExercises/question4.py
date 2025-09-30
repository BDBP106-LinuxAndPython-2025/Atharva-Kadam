#(4) Write a program to concatenate two strings, S1 and S2.
S1=str(input("Enter the first string:"))
S2=str(input("Enter the second string:"))
S3=""
for i in S1:
    S3+=i
for j in S2:
    S3+=j
print(S3)
#or S3=S1+S2