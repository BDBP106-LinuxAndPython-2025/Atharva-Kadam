"""(2) Create a decorator to measure the execution time of a function. Please demonstrate
using a sample function (add sleep for checking) and a decorator for this sample function
that measures the execution time."""
import time
def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func_result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Time taken for executing the function-{func.__name__} is {end_time-start_time:.3f}seconds")
        return func_result
    return wrapper

@execution_time
#sample function
def multiply(a,b):
    product=a*b
    time.sleep(2)
    return product

multiply(2,3)


