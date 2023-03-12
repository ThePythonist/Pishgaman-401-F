import sqlite3

con = sqlite3.connect("imdb.db")
cur = con.cursor()


def create_table(table_name, table_fields):
    columns = []

    for i in range(int(table_fields)):
        column = input("Column name : ")
        columns.append(column)

    command = "CREATE TABLE {} {};".format(table_name, tuple(columns))
    cur.execute(command)

    con.commit()
    con.close()
    print(f"Table {table_name} created successfuly")


while True:
    action = input("Choose an action (1:Create, 2:Insert, 3:Select) : ")
    if action == "1":
        table_name = input("Enter a table name : ")
        table_fields = input("How many fields do you need : ")
        create_table(table_name, table_fields)
        break
    else:
        print("Invalid input")
