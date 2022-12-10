word = input("Entry : ")

for character in word:
    if character == word[-1]:
        print(character)
    else:
        print(character, end="***")
