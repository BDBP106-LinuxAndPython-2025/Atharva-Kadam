"""(8) Check for the presence of an AvaII recognition site, which can have two different se-
quences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC”
pattern = GGACC and GGTCC"""
import re
dna ="ATCGCGAATTCAC"
pattern = "GGACC"or "GGTCC"
ava_II=bool(re.search("GAACC|GGTCC",dna))
if ava_II==True:
    print("The Ava II site is present.")
else:
    print("The Ava II site is not present")