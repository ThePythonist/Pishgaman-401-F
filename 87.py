lines = open('words.txt').readlines()
sublist = []

for line in lines:
    if line[0:3] == "sub":
        sublist.append(line)

open("sublist.txt", "w").write("".join(sublist))
