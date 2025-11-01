"""(iv) Write a program that allows the user to delete 1 or more records from the above
database. The input is a single line containing the ID of the employees to be
deleted, separated by spaces."""
import sqlite3
conn=sqlite3.connect("IBABEmployee.db")
curs=conn.cursor()

id=input("Enter all the ids whose data has to be deleted:").split()
for emp_id in id:
   curs.execute(f"DELETE FROM ibabemployees WHERE emp_id=?",(emp_id))

curs.execute('SELECT * FROM ibabemployees')
rows=curs.fetchall()
print(rows)


conn.commit()
curs.close()
conn.close()