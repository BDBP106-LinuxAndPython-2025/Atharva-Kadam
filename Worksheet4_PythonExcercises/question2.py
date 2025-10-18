"""(2) Write a list comprehension to output the AT content in % in a list of DNA
sequences.For example, sequences=["ATGC", "GGCC","AATT","GCGC"]"""
sequences=["ATGC","GGCC","AATT","GCGC"]
At_content=[ (seq.count('A')+ seq.count('T')/len(seq) *100) for seq in sequences]
print(At_content)

