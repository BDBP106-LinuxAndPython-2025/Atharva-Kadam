# (7) Write a script to replace all occurrences of a character, c, with another character, d.
S=input("Enter a string:")
c=input("Enter character to be replaced:")
d=input("Enter the new character:")
new_str=""
for i in S:
    if i==c:
        new_str+=d
    else:
        new_str+=i
print(new_str)