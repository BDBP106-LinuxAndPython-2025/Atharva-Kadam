#(3) Write a program to find the maximum and minimum values of a dictionary.
dict={}
d=int(input("Number of key value pairs in the dictionary:"))
for i in range(d):
    key =input(f"Enter the key {i+1}: ")
    value=int(input(f"Enter the value of the key {key}:"))
    dict[key]=value
print(dict)

max=0
v=dict.values()
for i in v:
    if i>max:
        max=i
print(f"The maximum value of dictionary is:{max}")


v=dict.values()
list_of_v=list(v)
min=list_of_v[0]
for i in list_of_v:
    if i<min:
        min=i
print(f"The minimum value of dictionary is:{min}")

