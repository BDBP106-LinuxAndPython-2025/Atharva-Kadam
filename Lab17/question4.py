#(4) Given a dictionary with a values list, extract the key whose value has the most unique values.
test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
v=test_dict.values()
for key,value in test_dict.items():
    value_set=set(value)
    count=0
    print(key,value_set)
    for j in value_set:
        count+=1

    test_dict[key]=count
print(test_dict)
max=0
for key,value in test_dict.items():
    if value>max:
        max=value
print(key)










