import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


# cur.execute('CREATE TABLE users (phone,name,charge,natlcode);')
# cur.execute("INSERT INTO users VALUES ('09936256040','Sadeghi','198','123456891');")
# cur.execute("INSERT INTO users VALUES ('09150556589','Shojaei','1024','423756891');")
# cur.execute("INSERT INTO users VALUES ('09216321608','Halati','45','873456891');")

def sendwarning(phonenumber, charge):
    print(f"""
مشترک گرامی{phonenumber} موجودی حساب شما برابر با {charge} مگ میباشد. نسبت به تمدید بسته اقدام نمایید.
""")


cur.execute("SELECT * FROM users;")
records = cur.fetchall()
for user in records:
    if int(user[2]) <= 200:
        sendwarning(user[0], int(user[2]))
con.commit()
con.close()
# print("Done")
