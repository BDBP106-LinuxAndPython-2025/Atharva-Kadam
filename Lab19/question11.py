""" (11) Write a decorator log_function_call that prints Running DNA analysis.... before
 and Analysis complete! after any function. Apply it to the above function that returns
 the GC % of a DNA sequence."""
def log_function_call(func):
    def wrapper():
        print("Running DNA analysis")
        func()
        print("Analysis complete")
    return wrapper

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

@log_function_call
def run_analysis_dna():
    analyse_dna("ATGCATATACGCG")

run_analysis_dna()
