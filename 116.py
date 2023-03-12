import sqlite3

con = sqlite3.connect("info.db")
cur = con.cursor()

# cur.execute("""
# CREATE TABLE employees (
# id INTEGER PRIMARY KEY,
# fname,
# lname,
# age,
# phonenumber,
# jobtitle
# )
# """)

people = [
    {"fname": "Matin", "lname": "Shojaei", "age": "17", "phonenumber": "09336502730", "job": "Backend Dev"},
    {"fname": "Arman", "lname": "Halati", "age": "14", "phonenumber": "09136506771", "job": "Frontend Dev"},
    {"fname": "Sepehr", "lname": "Mirzaei", "age": "21", "phonenumber": "09386505050", "job": "Security Engineer"},
]

for person in people:
    cur.execute(
        f"INSERT INTO employees ('fname','lname','age','phonenumber','jobtitle') VALUES (?,?,?,?,?);", (
            person['fname'],
            person['lname'],
            person['age'],
            person['phonenumber'],
            person['job'],
        ))

# cur.execute("DELETE FROM employees;")
# cur.execute("DROP TABLE employees")

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    print(i)

con.commit()
con.close()
print("Done")

