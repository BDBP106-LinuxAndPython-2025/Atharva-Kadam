"""(10) Take a DNA sequence and determine whether or not it contains any
ambiguous bases –
i.e. any bases that are not A, T, G or C. If there is a non ambiguous base, print the non
ambiguous bases. dna = ”ATCGCGYAATTCAC”"""
import re
dna="ATCGCGYAATTCAC"
ambig_base=re.findall("[^ATGC]",dna)
if ambig_base:
    print(f"There is ambiguouse base in the sequence:{ambig_base}")
else:
    print("There is no ambiguous base in the sequence.")