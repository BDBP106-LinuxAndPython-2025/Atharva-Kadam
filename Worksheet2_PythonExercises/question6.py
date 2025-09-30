# (6) Write a script to find the highest frequency character in a string, S.
S=input("Enter a string:")
count=0
max_char=""
for i in S:
    count2=0
    for j in S:
        if i==j:
            count2+=1
    if count2>count:
     count=count2
     max_char=i
print(f"The character {max_char} in string {S} occurs maximally:{count} times")

