#(1) Write a program to iterate over a dictionary and print the key-value pairs.
# for key in D: print(key) # print the keys
# keys=D.keys(); for i in keys: print(i)
# values=D.values(); for i in values: print(i)
# What does this do?
# for key in D: print(D[key])
# for key in D: print(D.get(key))
# Printing keys and values
# for key,value in D.items(): print(key,value)
# ‘apple’ in D
dict={}
D=int(input("Enter the number of key value pairs:"))
for i in range(D):
    k = input(f"Enter the  key {i+1}: ") #key
    v = input(f"Enter value for {k}: ") #value
    dict[k] = v

print("The key value pairs of the dictionary are:",dict)

for k,v in dict.items(): print(k,v)