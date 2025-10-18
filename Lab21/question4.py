"""(4) Write a Python function checkList that accepts a list and an index, and prints the
element of the list at the index position. Catch the IndexError and TypeError and
display appropriate messages. Call the function for (a) number list and index, (b) A
string input and index, (c) A boolean value (True) and index and (d) A string input and
incorrect index."""
def checkList(list1,idx):
    try:
         if not all(isinstance(i, int) for i in list1) or type(idx) != int:
             raise TypeError("The index and the elements of the list should be integers.")

         if idx not in range(len(list1)):
             raise IndexError("Index Out of Range")

         else:
             print(f"The element of the list is:{list1[idx]}")
    except TypeError as g:
         print("TypeError:",g)
    except IndexError as e:
        print("IndexError:", e)

checkList([1,2,3,4,5],3)
checkList("w",3)
checkList(True,3)
checkList([1,2,3,4,5],"h")
checkList([1,2,3,4,5],6)
