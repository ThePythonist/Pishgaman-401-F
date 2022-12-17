while True:
    entry = input("Entry : ")

    try:
        entry = int(entry)
        print("Its a number")
        try:
            print(entry[0])
        except:
            print("Numbers dont have index")

        break
    except ValueError:
        print("Entry must be number")
