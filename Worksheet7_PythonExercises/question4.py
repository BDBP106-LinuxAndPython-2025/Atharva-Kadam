"""(4) Database exercise:
(i) Create a database called school.db. You are going to build a simple student
marks management system using SQLite3. Inside this databse, create a table
called students with the following columns: id of type INTEGER, name of type
TEXT, subject of type TEXT and marks of type INTEGER.
(ii) Insert the following records into the students table:
id name subject marks
1 Ravi Math 85
2 Meena Science 90
3 Arjun English 78
4 Priya Math 92
5 Suresh Science 65
(iii) Write SQL queries using Python to a) display all records in the table, b) display
the names of students who scored above 80 marks, c) display the average marks
in each subject.
(iv) Update ”Suresh’s” science marks from 65 to 75.
(v) Delete the record of the student who scored the lowest marks in English.
(vi) Add a new column called ’grade’ to the table, and assign ”A” for marks >= 85,
”B” for marks between 70-84, and ”C” for marks< 70."""
import sqlite3 as sql
#(i)
conn=sql.connect("school.db")
curs=conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
""")
#(ii)
records=[
    (1,"Ravi","Math",85),
    (2,"Meena","Science",90),
    (3,"Arjun","English",78),
    (4,"Priya","Math",92),
    (5,"Suresh","Science",65)
]
curs.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?,?)",records)
conn.commit()

#(iii)
print("\nRecords:")
for i in curs.execute("SELECT * FROM students"):
    print(i)

print("\nStudents who scored above 80 marks:")
for i in curs.execute("SELECT name FROM students WHERE marks > 80"):
    print(i)

print("\nAverage marks of each subject:")
for row in curs.execute("SELECT subject,AVG(marks) FROM students GROUP BY subject"):
    print(row)


#(iv)Updating Suresh's marks
curs.execute("UPDATE students SET marks=75 WHERE name='Suresh'")
conn.commit()

#(v)delete record of student who scored lowest marks in english
curs.execute("DELETE FROM students WHERE subject='English' AND marks=(SELECT MIN(marks) FROM students WHERE subject='English')")
conn.commit()

#(vi)Grade column
curs.execute("ALTER TABLE students ADD COLUMN grade TEXT")
curs.execute("UPDATE students SET grade='A' WHERE marks >= 85")
curs.execute("UPDATE students SET grade='B' WHERE marks BETWEEN 70 AND 84")
curs.execute("UPDATE students SET grade='C' WHERE marks < 70")
conn.commit()
print("\nFinal records:")
for i in curs.execute("SELECT * FROM students"):
    print(i)

conn.close()
