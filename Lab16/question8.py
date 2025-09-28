#(8) Write a script to count the number of occurrences of a word, W, in a sentence, S.
string=str(input("Enter a string:"))
word=str(input("Enter a word:"))
count=0
sub_string=string.split()
for i in sub_string:
   if i == word:
    count+=1
print(count)

