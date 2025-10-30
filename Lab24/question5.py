"""(5) You are given two 1D arrays. Write a function to create
a new array that contains the maximum of the respective elements
in the two arrays. For example, if a=[1,2] and
b=[0,5] then the new array will be c=[1,5]."""
import numpy as np

p=np.array([1,2,3])
q=np.array([0,10,4])
r=np.maximum(p,q)    #it doesnt give the maximumm of each of the arrays it compares the element present on the same index in both the arrays and which ever is the maximum it prints that
print("The array containing the maximum of the respective elements of the arrays",r)


a=np.arange(10)
b=np.arange(10,20)
c=np.max(a)
d=np.max(b)
print("The maximum element of each of each of the array is:",[c,d])