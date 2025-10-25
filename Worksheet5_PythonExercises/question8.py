"""(8) In the above exercise, let’s use an in-built decorator function called lru_cache, where
lru stands for least recently used – It caches/stores the results of function calls, so
that if the same input occurs again, it reuses the stored result instead of recomputing it.
Least recently used means that it keeps the most recent results and discards the oldest
ones if the cache gets full. We have control over the size of this cache, An example usage
is given below.
from functools import lru_cache
@lru_cache(maxsize=None)
def factorial(n):
if n==0 or n==1: return 1
if n>1: return n*factorial(n-1)
(i) Use a similar setup for the Fibonacci series calculation with maxsize=5. What is
the time difference you see with and without the use of lru_cache?

(ii) Provide a docstring with ‘”This function outputs the sum of n Fibonacci num-
bers”’ inside the function. Print fibonacci.__doc__ and observe the output.

(iii) Use a custom decorator log_time to print the datetime.now() value at entry
and exit for every func.__name__ call with the n (args) value."""
from functools import lru_cache
from datetime import datetime

@lru_cache(maxsize=5)
def fibonacci(n):
    """This function outputs the sum of n Fibonacci numbers."""
    if n<=1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci.__doc__)

def log_time(func):
    def wrapper(*args,**kwargs):
        print(f"[{datetime.now()}] Calling {func.__name__}{args}")
        result = func(*args,**kwargs)
        print(f"Exiting {func.__name__}{args}\n")
        return result
    return wrapper

@log_time
def fibonacci_cache(n):
    if n<=1:
        return 1
    return fibonacci_cache(n-1)+fibonacci_cache(n-2)

print("Without cache:")
fibonacci.cache_clear()
print(fibonacci_cache(10))

print("\nWith cache:")
print(fibonacci(10))
