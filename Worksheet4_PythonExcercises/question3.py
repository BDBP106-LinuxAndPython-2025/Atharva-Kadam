""" (3) Write a list comprehension to create a list of names that start with
 ’H’ or ‘ase'; in a given list of protein names. For example,
 proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]"""
proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]
start_h_end_ase=[i for i in proteins if i.startswith("H") or i.endswith("ase")]
print(start_h_end_ase)