""" (7) Write a function analyse_dna(sequence) that defines an inner function
gc_content() to calculate GC% . The outer function should print whether the
given DNA is AT rich or GC rich sequence."""
def analyse_dna(sequence):
    seq=sequence.upper()
    def gc_content():
        count_GC=0
        for i in seq:
            if i == 'G' or i == 'C':
                count_GC+=1
        return (count_GC/len(seq))*100

    gc_cont=gc_content()
    if gc_cont>50:
        GC_or_AT="The sequence is GC Rich"
    elif gc_cont<50:
        GC_or_AT="The sequence is AT Rich"
    else:
        GC_or_AT="The sequence is balanced"
    print(f"The GC content of {sequence} is {gc_cont}%")
    return GC_or_AT
print(analyse_dna("ATGCGCATAA"))



