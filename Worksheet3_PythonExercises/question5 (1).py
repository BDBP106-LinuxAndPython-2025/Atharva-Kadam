"""(5) Write functions to add and subtract two matrices of m× n. Below these two functions,
create two example matrices that have the same dimensions (rows and columns) and
therefore correctly does the addition and subtraction Also come up with an example
where the addition and subtraction are not defined, and hence the runtime errors show
up."""

def add(m,n):
    if len(m)!=len(n) or len(m[0])!=len(n[0]):
        raise ValueError("The matrices should have the same dimensions.")
    result=[]
    for i in range(len(m)):
        row=[]
        for j in range(len(m[0])):
            row.append(m[i][j] + n[i][j])
        result.append(row)
    return result

def subtract(m,n):
    if len(m)!=len(n) or len(m[0])!=len(n[0]):
        raise ValueError("The matrices should have the same dimensions.")

    result=[]
    for i in range(len(m)):
        row=[]
        for j in range(len(m[0])):
            row.append(m[i][j] - n[i][j])
        result.append(row)
    return result

m=[[12,2,2],
   [8,5,4]]
n=[[1,2,3],
   [4,9,6]]
print("The sum of the matrices is:")
print(add(m,n))

print("The subtraction of the matrices is:")
print(subtract(m,n))

m=[[3,2,1],
   [4,5,2],
   [7,6,1]]
n=[[1,9],
   [2,8]]
print("The sum of the matrices is:")
print(add(m,n))