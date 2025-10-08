#(3) List comprehension with strings Use list comprehension technique you learnt in class to do the following
"""(i) Using the join method.
(a) Create a string by joining the numbers in the above list a using the comma."""
a=[i for i in range(1,51)]
print(a)

a_string=','.join([str(j) for j in a])
print(a_string)

"""(b) Create a string by joining the numbers in the above list a using the period."""
a_string2='.'.join([str(y) for y in a])
print(a_string2)

"""(c) Create a string by joining the numbers in the above list a using the ‘—’."""
a_string3='—'.join([str(x) for x in a])
print(a_string3)

"""(d) Create a new string by first creating a list of squares of the elements in a,
then listing them alongside the elements of a line by line. In other words,
we want a data set that looks like
1 1
2 4
3 9
. . ."""
a_square_string=",".join([str(i*i) for i in a])
print(a_square_string)

d="\n".join([f"{i} {i*i}" for i in a])
print(d)

"""(ii) Make a list of 10 people you know, and do the following:
(a) Convert each element in the list to upper case using list comprehension"""
people=["Pratham sonone","prerna ShAmshaPure", "Atharva gabhane","poorva tillu","Parth kadam","srUshti khapekar","siddhant khapekar","jayshree Kadam","sharda chawhan","dilIP Kadam"]
people_upper=[i.upper() for i in people]
print(people_upper)

""""(b) Swap the first name and surname of each element in the list"""
people_swap=[' '.join(i.split()[::-1])for i in people]
print(people_swap)

""""(c) Join the first name and surname in each element as ’First.Last’. Note that
the first letter of the first name and first letter of the surname should be
upper case."""
people_join=[".".join([i.split()[0].capitalize() , i.split()[1].capitalize()]) for i in people]
print(people_join)


"""(iii) Find the longest word in this sentence using list comprehension: ”She sells sea
shells that she collects from the sea floor”."""
a="She sells sea shells that she collects from the sea floor"
words=a.split()
print(words)
word_longest=[i for i in words if len(i)==max(len(i) for i in words)]
print(word_longest)

"""(iv) Create a list of the words that are repeated in the above sentence."""
b="She sells sea shells that she collects from the sea floor"
words=b.lower().split()
repeated=[i for i in words if words.count(i)>1]
print(repeated)