ana1=str(input("Enter 1st word: "))
ana2=str(input("Enter 2nd word: "))
if len(ana1)!=len(ana2):
    print("The two words are not anagrams.")
else:
 is_anagram=False
 for i in ana1:
   let_ana1 = 0
   let_ana2 = 0
   for j in ana1:
      if j==i:
       let_ana1+=1
   for j in ana2:
      if j==i:
       let_ana2+=1
   if let_ana1==let_ana2:
       is_anagram=True

 if is_anagram==True:
    print("The two words are anagrams.")
 else:
    print("The two words are not anagrams.")

