""" (9) Write a function population_growth(initial,rate, time) that definss
 an inner function exponential_growth() using the formula
  N(t) = N0 + exp(rate ∗ time)
where N0 represents the initial population and N(t) is population after time t.
The inner function returns the population after time, and the outer function
rounds and prints it."""
import math
def population_growth(initial,rate, time):
    def exponential_growth(N0,r,t):
        e=math.e
        return N0 * e**(r * t)
    Nt=round(exponential_growth(initial,rate,time))
    return f"Population after {time} years: {Nt}"

print(population_growth(1000,0.2,20))



