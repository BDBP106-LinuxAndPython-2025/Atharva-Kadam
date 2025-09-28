# (12) Write a program to subtract two matrices, m1 and m2, using a list of lists.
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[9,8,7],
   [6,5,4],
   [3,2,1]]
C=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] - B[i][j]

for n in C:
    print(n)