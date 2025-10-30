"""(2) Array creation and manipulation exercises. Print all the arrays in each exercise.
(i) Create a 1D array from 0 to 9."""
import numpy as np
array_1D=np.arange(10)
print(array_1D)


"""(ii) Create a boolean array of size 3x3."""
bool_array=np.array([[1,1,0],
                     [1,0,1],
                     [1,0,1]],dtype=bool)
print(bool_array)

#or
bool_array2=np.full((3,3),[True,False,True])
print(bool_array2)

#or
bool_array3=np.random.choice([True,False],(3,3))
print(bool_array3)


"""(iii) Using syntax from list comprehension, create an array that satisfies the condition.
For example,
arr = np.arange(10)
arr = arr[ arr%2 == 1 ]
Create an array of prime numbers from 1 to 50 using a similar approach."""
array_prime=np.array([i for i in range(2,51) if all(i%x!=0 for x in range(2,i))])
print(array_prime)



"""(iv) Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print
the two arrays."""
array_random=np.random.randint(1,30,20)
print("The random array is:", array_random)
array_random_reshape=array_random.reshape(4,5)
print("The 4x5 random array is:\n",array_random_reshape)



"""(v) Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has
only 1s. Then stack the two arrays horizontally."""
a=np.arange(10)
print("a= ",a)
b=np.ones(10, dtype=np.int16)
print("b= ",b)
print(np.hstack((a,b)))    # h letter used before stack is used for horizontal stacking while v is used for vertical stacking



"""(vi) Define two 1D arrays, where array a has list of first 100 numbers, and b has first
100 prime numbers. Obtain a new array that is the intersection of these two
arrays (Hint: use np.intersect1d())"""
a=np.arange(100)
print("a= ",a)
b=np.array([x for x in range(2,1000) if all( x%i for i in range (2,x))][:100])
print("b= ",b)
intersection_a_b=np.intersect1d(a,b)
print("The intersection of a and b is :" ,intersection_a_b)



"""(vii) Use the above two arrays with the aim this time to remove items from a that are
in b. (We are doing a-b operation, use np.setdiff1d())"""
a=np.arange(100)
print("a= ",a)
b=np.array([x for x in range(2,1000) if all( x%i for i in range (2,x))][:100])
print("b= ",b)
difference_a_b=np.setdiff1d(a,b)
print("The difference of a and b is: ",difference_a_b)




"""(viii) Use the above two arrays with the aim of getting the indices of common elements
between the two arrays. (Hint: Use np.where(a==b))"""
a=np.arange(100)
print("a= ",a)
b=np.array([x for x in range(2,1000) if all( x%i for i in range (2,x))][:100])
print("b= ",b)
common_elements2=np.where(a==b)
common_elements=np.where(np.isin(a,b))
print(common_elements2)
print("Common elements of a and b with index are: ",common_elements)





"""(ix) Extract the elements of the array a above that are greater than 5 and less than
20."""
a=np.arange(100)
print("a= ",a)
modified_a=np.array([i for i in a if i>5 and i<20])
print(modified_a)


