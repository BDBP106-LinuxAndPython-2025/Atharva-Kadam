"""(3) We know how to reverse the elements in a 1D array- a[::-1].
 How would you reverse the rows in a 2D array?
 How would you reverse the columns in a 2D array?"""
import numpy as np
array_2d_a=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print("Original: \n", array_2d_a)
reverse_column=array_2d_a[::-1]
print("Reverse column: \n",reverse_column)
reverse_row=array_2d_a[:,::-1]
print("Reverse row: \n",reverse_row)

