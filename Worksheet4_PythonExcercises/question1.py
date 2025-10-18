""" (1) Write a list comprehension to extract all even gene lengths from a list
of genes. For example, gene_lengths=[450,300,725,1024,512,815]."""
gene_lengths=[450,300,725,1024,512,815]
even_length=[length for length in gene_lengths if length%2==0]
print(even_length)