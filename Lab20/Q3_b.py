"""(b) Next, in a new program, read in the matrix of strings in the above file as a 2D array
of list of lists. The number of rows and columns are not known in advance. Make
sure your code can figure out how many rows and columns are there in this input.
Name this list as grid and print this 2D list. Name this program as ”Q3 b.py”. In
this same program, print a list that contains lists of columns of the above matrix.
For example, the first column will be grouped into a list [A,E,I] and so on. Next,
print a list that prints the diagonal elements read in one direction. For example,
some of the elements in this list will be [‘A’],[‘B’,‘E’],[’C’,‘F’,‘I’] and so on."""
basedir='/home/ibab/Atharva-Kadam/Lab20/'
a=open(basedir+"stringmatrix.dat")
print(a)
lines=a.readlines()
print(lines)
grid=[]
for i in range(len(lines)):
    row=[]
    line=lines[i]
    letter=line.split(" ")
    for i in letter:
        if i!='\n' and i!=' ' and i!='':
            row.append(i)
    grid.append(row)
print(grid)

#for rows
for row in grid:
    print(row)
#to count the number of rows:
rows=0
columns=0
for j in grid:
    rows+=1
for i in grid[0]:
    columns+=1
print(f"The number of rows in the grid are:{rows}")
print(f"The number of columns in the grid are:{columns}")

column_list1=[]
column_list2=[]
column_list3=[]
column_list4=[]
final_column_list=[]
for k in grid:
    for l in k[0]:
        column_list1.append(l)
        for m in k[1]:
           column_list2.append(m)
           for n in k[2]:
               column_list3.append(n)
               for o in k[3]:
                    column_list4.append(o)
final_column_list.append(column_list1)
final_column_list.append(column_list2)
final_column_list.append(column_list3)
final_column_list.append(column_list4)
print(final_column_list)

#or
column2=[]
for c in range(columns):
    sub_columns = []
    for r in range(rows):
     sub_columns.append(grid[r][c])
    column2.append(sub_columns)
print(column2)

#diagnonal list

all_diagonals=[]
for i in range(rows + columns-1):
    diagonal_list = []
    if i<columns:
        row=0
        column=i
    else:
        row=i - columns +1
        column=columns -1

    while row < rows and column >=0:
        diagonal_list.append(grid[row][column])
        row+=1
        column-=1
    all_diagonals.append(diagonal_list)
print(all_diagonals)





