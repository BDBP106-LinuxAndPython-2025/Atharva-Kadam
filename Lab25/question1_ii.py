"""(ii) Write a program that allows the user to add multiple records into the above
database file. After every record, the user should be asked whether he/she wants
to add another record. Do this for all the faculty in IBAB."""

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
# num_fac=int(input("Enter the total number of faculties in ibab: "))
confirm=input("Do you want to add another record?(Yes/No): ")
while confirm!="No":
    e_id=int(input("Enter the employee id:"))
    name=input("Enter name:")
    r_area=input("Enter your area of research: ")
    desg=input("Enter designation: ")
    gend=input("Enter Gender :")
    curs.execute(
        'INSERT INTO ibabemployees (emp_id,emp_name,emp_research_area,emp_designation,emp_gender) VALUES(?,?,?,?,?)',
        (e_id,name,r_area,desg,gend)
    )
    ask = input("Do you want to add another record?(Yes/No):")
    if ask=="No" or ask=="no":
        break

curs.execute('SELECT * FROM ibabemployees')
rows=curs.fetchall()
print(rows)

# query='DROP TABLE IF EXISTS ibabemployees'
# curs.execute(query)

conn.commit()
curs.close()
conn.close()

