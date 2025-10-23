"""(1) Create a logging decorator to record function calls, arguments, and return values. For
example, if we have an add function shown below and invoke it as add(2,3), create a
decorator that prints the following:
# add function
def add(a, b):
return a + b
# the decorator should print
Calling add with args: (2, 3), kwargs: {}

add returned: 5"""
def logging_function(func):
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args: {args},kwargs: {kwargs}")
        a=func(*args,**kwargs)
        print(f"{func.__name__} returned: {a}")
        return a
    return wrapper

@logging_function
def add(a,b):
    return a+b

#test output
add(2,3)
