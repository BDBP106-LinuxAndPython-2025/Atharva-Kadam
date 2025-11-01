"""(iii) Write a program that allows the user to edit an entry present in the above data-
base. The program should ask for the ID of the employee and should take in the
new details of the employee.
"""
import sqlite3
conn=sqlite3.connect("IBABEmployee.db")
curs=conn.cursor()

id=int(input("Enter your employee ID: "))
# curs.execute("""
#        UPDATE Employee
#        SET name=?, research_area=?, designation=?, gender=?
#        WHERE ID=?
#    """, (name, area, desig, gender, id_))

name_n=input("Enter correct name: ")
res_n=input("Enter new area of research: ")
desg_n=input("Enter new designation: ")
gen_n=input("Enter your correct gender :")

curs.execute(f"""
        UPDATE ibabemployees 
        SET emp_name='{name_n}',emp_research_area='{res_n}',emp_designation='{desg_n}',emp_gender='{gen_n}'
        WHERE emp_id={id}
    """)

curs.execute('SELECT * FROM ibabemployees')
rows=curs.fetchall()
print(rows)

conn.commit()
curs.close()
conn.close()