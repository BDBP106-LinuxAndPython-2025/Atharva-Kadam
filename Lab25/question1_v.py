"""(v) Write a program that displays all the records present in the above database in a
formatted manner."""
import sqlite3
conn=sqlite3.connect("IBABEmployee.db")
curs=conn.cursor()
query="SELECT * FROM Ibabemployees"
curs.execute(query)
print('Fetching all the records')
rows=curs.fetchall()
print(rows)
conn.commit()
curs.close()
conn.close()