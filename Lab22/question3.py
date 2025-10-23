"""(3) Implement matrix multiplication of matrices A and B without using any external pack-
ages as an instance method in a class called LinearAlgebra. Get the no. of rows and
columns and elements of each matrix from the user. Raise errors in case the condition
for matrix multiplication is not met. Once you have a working code for this, decorate a
function that returns the matrices A and B using @property. Then also define a setter
function to allow the modification of A and B, since the user may make mistakes in
inputting the matrices and should be able to change elements as desired. Lastly, define
a custom decorator for calculating time in multiplying matrices A and B of size 50x50."""
import time
def time_to_multiply(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Multiplication of matrices took:{end_time-start_time}seconds")
        return result
    return wrapper

class LinearAlgebra:
    def __init__(self,A,B):
        self.A=A
        self.B=B
        if len(A[0])!=len(B):  #here we are comparing the number of columns of 1st Matrix and number of rows in the 2nd matrix
            raise ValueError("The columns and rows of the matrices should be the same for multiplication")
    @property
    def a(self):
      return self.A

    @a.setter
    def a(self,mod_A):
        if len(self.A[0])!=len(self.B):
            raise ValueError("Columns and Rows of the matrices should be equal")
        self.A=mod_A

    @property
    def b(self):
        return self.B

    @b.setter
    def b(self, mod_B):
        if len(self.A[0]) != len(mod_B[0]):
            raise ValueError("Columns and Rows of the matrices should be equal")
        self.B = mod_B

    @time_to_multiply
    def matrix_multiplication(self):
        rows_A=len(self.A)
        cols_A=len(self.A[0])
        rows_B=len(self.B)
        cols_B=len(self.B[0])
        AB=[[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(rows_B):
                    AB[i][j]+= self.A[i][k]*self.B[k][j]
        time.sleep(3)
        return AB

# A = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
#
# B = [[9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]]
import random
A = [[random.randint(1,4) for _ in range(50)] for _ in range(50)]
B = [[random.randint(3,6)  for _ in range(50)] for _ in range(50)]
LA=LinearAlgebra(A,B)
print(f"The resultant matrix is:{LA.matrix_multiplication()}")


