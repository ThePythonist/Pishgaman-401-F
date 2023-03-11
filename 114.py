import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

# cur.execute("INSERT INTO students VALUES ('Matin',17,'Mehregan','Riazi');")
# cur.execute("INSERT INTO students VALUES ('Arman',14,'Pishgaman','Riazi');")
# cur.execute("DELETE FROM students WHERE name='Arman';")
cur.execute("SELECT * FROM students;")
records = cur.fetchall()
print(records)

con.commit()
con.close()
print("Done")
