#(5) Write a script to find the first occurrence of a character, c, in a string S.
S=input("Enter a string:")
c=input("Enter the character c:")
for i in range(len(S)):
    if S[i]==c:
        position=i
        break
print(f"The position of the first occurrence of character {c} in {S} is:{position}")
