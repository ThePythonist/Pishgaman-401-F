lines = open('words.txt').readlines()
inglist = []

for line in lines:
    if line[-4:-1] == "ing":
        inglist.append(line)

open("inglist.txt", "w").write("".join(inglist))
