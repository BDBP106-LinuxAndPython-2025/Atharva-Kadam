"""(6) 11. You’re going to write an interactive calculator! User input is assumed to be a formula
that consists of a number, an operator (at least + and -), and another number, separated
by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the
resulting list is valid:
• If the input does not consist of 3 elements, raise a FormulaError, which is a custom
Exception.
• Try to convert the first and third input to a float (like so: float_value = float(str_value)).
Catch any ValueError that occurs, and instead raise a FormulaError
• If the second input is not ’+’ or ’-’, again raise a FormulaError
• If the input is valid, perform the calculation and print out the result. The user is
then prompted to provide new input, and so on, until the user enters quit."""
class FormulaError(Exception): #creating a class for a custom error
    pass
def interactive_calculator():
    while True:
      user_in=input("Enter a number an operator and the second number:")
      if user_in.lower()=="quit":
          print("Calculator exiting")
          break

      char=user_in.split()

      if len(char)!=3:
         raise FormulaError(" Input should contain 3 elements-a number, an operator and a second number")
      num1, op, num2 = char

      try:
        num1=float(num1)
        num2=float(num2)
      except ValueError:
         raise FormulaError(" Please input number1 and number2 as 1st and 2nd element")

      if op not in("+","-"):
         raise FormulaError("The second element should be an operator.")

      if op=="+":
         print(f"The sum of the 2 numbers is: {num1+num2}")
      else:
        print(f"The difference of the 2 numbers is: {num1-num2}")


if __name__=="__main__":
    try:
        interactive_calculator()
    except FormulaError as a:
        print(f"Formula Error:{a}")