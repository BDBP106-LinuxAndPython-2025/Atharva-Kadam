"""(7) Implement the Fibonacci function with parameter n. Call fibonacci(100) and use a
decorator function to log the time taken to run this function."""
import time
def time_taken(func):
    def wrapper(n):
        start_t=time.time()
        f=func(n)
        end_t=time.time()
        print(f"The time taken to run the function {func.__name__} is: {end_t-start_t:.7f} seconds")
        return f
    return wrapper

@time_taken
def fibonacci(n):
    l=[]
    f0=0
    f1=1
    for i in range(n):
        l.append(f0)
        f2=f0+f1
        f0=f1
        f1=f2
    return l

print(fibonacci(100))