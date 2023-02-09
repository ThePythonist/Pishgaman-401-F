# lines = open('words.txt').readlines()
# lines.sort(key=len)
# print(lines[-1])
# print(lines[0])

lines = open('words.txt').readlines()
lines.sort(key=len)
maximum = max(lines, key=len)
minimum = min(lines, key=len)
# print(maximum)
# print(minimum)

for i in lines:
    if len(i) == len(maximum):
        print(i)
