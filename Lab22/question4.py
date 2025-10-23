"""(4) Write a decorator called @track_calls that counts how many times a function has been
called. It also should print the function name and the number of calls each times it is
executed. Instead of printing the output to the screen, log the output in a file."""
def track_calls(func):
    func.count=0
    def wrapper(*args,**kwargs):
        func.count+=1

        func_calls=f"{func.__name__} was called {func.count} times.\n"

        f=open("function_call.txt","a")
        f.write(func_calls)
        f.close()

        return func(*args,**kwargs)
    return wrapper

@track_calls
def add(a=2,b=3):
    return a + b

add(2,4)
add(3,4)
add(9,3)
