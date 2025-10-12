""" (8) Write a function protein_energy)temp) with an inner function
 calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H −T∆S. Use
 random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0)."""
import random
def protein_energy(temp, entropy=None,enthalpy=None):
    if entropy is None:
        entropy = random.random()
    if enthalpy is None:
        enthalpy = random.random()
    def calculate_free_energy(T,delta_S,delta_H):
        return delta_H - (T * delta_S)
    delta_G=calculate_free_energy(temp,entropy,enthalpy)
    if delta_G < 0:
        stability="stable"
    else:
        stability="unstable"
    return {"∆H":enthalpy,"T":temp,"∆S":entropy,"∆G":delta_G,"stability":stability}
print(protein_energy(19290))
