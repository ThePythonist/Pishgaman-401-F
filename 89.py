# lines = open('words.txt').readlines()
# items = [i[:-1] for i in lines]
# print(items[:100])

lines = open('words.txt').read()
lines.replace("\n", "")
print(lines)
