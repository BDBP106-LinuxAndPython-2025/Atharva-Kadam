""""(6) Write a function called cell_metabolism that takes the number of glucose and oxy-
gen molecules, that contains an inner function energy_output() to calculate ATP yield
(assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
produced."""
def cell_metabolism(num_glucose, num_oxygen):
    def energy_output(glucose, oxygen):
        glucose_available=min(glucose,oxygen//6)
        return glucose_available*38

    atp_yield=energy_output(num_glucose, num_oxygen)
    return atp_yield
#test output
print(cell_metabolism(6,12))



