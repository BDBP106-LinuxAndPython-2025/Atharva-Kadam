"""(5) Write a function that takes two numbers n1 and n2 and an operator description such
as add, subtract etc. Depending on the operation, perform the operation. Raise a
ValueError if the operator is not an arithmetic operation such as add, subtract, mul-
tiplication or division. Catch the ValueError and ZeroDivisionError and print the
appropriate messages. In the finally block, print a completion message. Call this func-
tion with different scenarios to test the above exceptions. Take screenshots of the output
while uploading your labs to GitHub."""
def operation(n1,n2,operator):
    try:
        if operator=="add":
            result=n1+n2
        elif operator=="subtract":
            result=n1-n2
        elif operator== "multiply":
            result=n1*n2
        elif operator == "divide":
            result = n1/n2
        else:
            raise ValueError("Give a valid operator")
        print("The result is: ",result)

    except ZeroDivisionError:
        print("ZeroDivisionError:Division by zero is undefined")
    except ValueError as e:
        print("ValueError:", e)
    finally:
        print("Operation was completed.")
operation(10, 5, "add")
operation(10,5,"multiply")
operation(10, 0, "divide")
operation(10, 3, "power")
operation(10,0,"idjgndkj")



