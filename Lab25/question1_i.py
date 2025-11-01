"""(1) SQLite exercise:
(i) Write a program to create an SQLite database in the file IBABEmployee.db that
contains a table called Employee with fields ID, name, research area, designation
and gender."""
import sqlite3
conn=sqlite3.connect('IBABEmployee.db')
curs=conn.cursor()
# print(curs)

curs.execute('''CREATE TABLE IF NOT EXISTS ibabemployees
                (
                emp_id INTEGER,
                emp_name TEXT,
                emp_research_area TEXT,
                emp_designation TEXT,
                emp_gender TEXT
                )
            ''')
curs.execute('SELECT * FROM ibabemployees')
rows=curs.fetchall()
print(rows)
conn.commit()
curs.close()
conn.close()