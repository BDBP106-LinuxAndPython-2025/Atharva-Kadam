"""(7) Explore the set_printoptions() function to pretty-print a numpy array by
suppressing the scientific notation (like 1e10)."""
import numpy as np

np.set_printoptions(suppress=True)
matrix_2=np.random.rand(2,2)*1e-10
print(matrix_2)