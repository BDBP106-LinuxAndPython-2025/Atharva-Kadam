#(5) Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the set() function might be useful here.)
sentence=input("Enter a sentence:")
word=sentence.split()
print(word)
word_set=set(word)
print(word_set)
for word in word_set:
    print(word,end=' ')

