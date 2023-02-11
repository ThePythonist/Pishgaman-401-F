lines = open('words.txt').readlines()
rev = []

for line in lines:
    rev.append(line[::-1])

open("rev-words.txt", "w").write("".join(rev))
print("Done")
