flag = True

while flag:
    # while flag == True:
    entry = input("Entry : ")
    print(entry)
    if entry == "exit":
        # break
        flag = False
else:
    print("Flag has turned into False")
