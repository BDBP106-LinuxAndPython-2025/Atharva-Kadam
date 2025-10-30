"""(6) Explore the set_printoptions() function to print
a 3x3 matrix containing random
numbers up to 3 decimal places."""
import numpy as np
np.set_printoptions(precision=3)
matrix_1=np.random.rand(3,3)
print(matrix_1)