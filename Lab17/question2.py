#(2) Write a program to sum all the values of a dictionary.
dict={}
D=int(input("Enter the number of key value pairs:"))
for i in range(D):
    k = input(f"Enter the  key {i+1}: ") #key
    v = input(f"Enter value for {k}: ") #value
    dict[k] = v
print("The key value pairs of the dictionary are:",dict)

sum=0
v=dict.values()
for i in v:
    v_int=int(i)
    sum=sum+v_int
print(f"The sum of all the values in the dictionary is: {sum}")


