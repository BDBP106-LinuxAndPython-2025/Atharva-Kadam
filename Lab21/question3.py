"""(3) Child class and user-defined error Define a custom error class called AgeTooYoungError
that extends Exceptions. In a function called checkAge that takes age as input, if the
age is less than 18, raise the AgeTooYoungError with the message (”Age must be more
than 18”). In the except block, print the error message thrown in the try block. Call
the function checkAge with 3 as the input."""
class AgeTooYoungError(Exception):
    pass

def checkage(age):
    try:
        if age < 18:
            raise AgeTooYoungError("Age must be more than 18")
        else:
            print("Age is valid.")

    except AgeTooYoungError as e:
        print("Error:",e)
        
print(checkage(3))





