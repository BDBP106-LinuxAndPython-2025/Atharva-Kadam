# (9) A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
# sequence called a codon. For example, the sequence fragment AGTCTTATATCT con-
# tains the codons AGT, CTT, ATA, TCT if read from the first position. If read from
# the second position, it yields the codons GTC, TTA, TAT and if read from the third
# position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
# 3-letter strings given a sequence and from what position (input as an integer) the se-
# quence should be read. As an example, output the 3-letter strings from the sequence
# GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position.
def extract_codons(seq,pos):
    codons=[]
    for i in range(pos-1,len(seq),3):
        cod=seq[i:i+3]
        if len(cod)==3:
            codons.append(cod)
    print(codons)
extract_codons("ATCGGTCAT",1)
extract_codons("ATCGGTCAT",3)
#####
#if input is taken from user
def extract_codons():
    sequence=input("Enter the sequence: ")
    position=int(input("Enter the position: "))
    codons=[]
    for i in range(position-1,len(sequence),3):
        cod=sequence[i:i+3]
        if len(cod)==3:
            codons.append(cod)
    print(codons)
extract_codons()