""" (4) Write a function enzyme_activity(name,subs_conc) that accepts the name of the en
zyme and substrate concentration as parameters. This will have an inner function called
 michelis_menten(Vmax,Km) that computes the reaction rate
 v = Vmax×[S]
 Km+[S]
 (1)
 and the outer function should return the reaction rate for given values. Write a main
 program that demonstrates the use of this inner and outer function with a meaningful
 example."""
def enzyme_activity(name,subs_conc):
    def michelis_menten(Vmax, Km):
        reaction_rate=(Vmax*subs_conc)/(Km+subs_conc)
        return reaction_rate

    Vmax=50
    Km=2
    rate=michelis_menten(Vmax, Km)
    return (f"The reaction rate with Vmax {Vmax} and Km {Km} is {rate:.2f}")

print(enzyme_activity("Hexokinase",2))