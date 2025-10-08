""""(2) One can create a set from several different objects – lists, tuples and dictionaries. Come
up with an example for each object type, and create a set out of that object using the
set() function. In the case of a dictionary, what does the set contain?."""
L=[1,2,3,"Apple",2,3,"Apple",4,5,"mango","mango"]
print(L)
print(set(L))

T=("Hello",1,2,3,4,5,"Hello",67,2,3,"Hi","Hi")
print(T)
print(type(T))
print(set(T))

D={"a":1,"b":2,"c":3,"c":4,"d":78}
print(D)
print(set(D))
#in the case of dictionary, the set only contains the keys of the dictionary and when we print the dictionary, there itself it doesn't give the repeating duplicate keys.
#and so in the set as well the keys are only shown without any duplicates