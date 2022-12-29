def check(word):
    word2 = set(word)
    if len(word) == len(word2):
        print("Tekrari nadarad")
    else:
        print("Tekrari darad")


word = input("Enter a word to check : ")
check(word)
