"""(7) Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna
= ”ATCGCGAATTCAC” pattern = GAATTC"""
dna="ATCGCGAATTCAC"
pattern = "GAATTC"
import re
eco_site=bool(re.search(pattern,dna))
if eco_site==True:
    print("Eco R1 site is present in the sequence.")
else:
    print("Eco R1 site is not present in the sequence.")

