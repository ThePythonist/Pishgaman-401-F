import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute('CREATE TABLE students (name,age,school,major);')

con.commit()
con.close()
print("Done")
