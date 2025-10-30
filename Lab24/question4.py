"""(4) Thinking along the same lines of the above question,
how will you swap two columns in a 2D array?
Define a 3x3 matrix with random values, and swap first
and second columns in this array."""
import numpy as np
x=np.arange(9).reshape(3,3)
print(x)
x[:,[0,1]]=x[:,[1,0]]
print(x)