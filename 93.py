def main():
    def register():
        username = input("Enter username : ")
        password = input("Enter password : ")

        open("db-users.txt", "a+").write(username + "\n")
        open("db-passwords.txt", "a+").write(password + "\n")
        print("Registered user")

    def login():
        pass

    entry = input("""
Type 1 to sign up
Type 2 to login to your account
:
""")

    if entry == "1":
        register()
    elif entry == "2":
        login()


main()
