# lines = open('words.txt').readlines()
# items = [i[:-1] for i in lines]
# print(items[:100])

lines = open('words.txt').read().replace("\n", "")
open("one-line.txt", "w").write(lines)
print("Done")
