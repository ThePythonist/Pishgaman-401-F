items = ["Ali",True, 12, 4.3, 5, "Farzad", 7, False]
words = []

for i in items:
    if type(i) == str:
        words.append(i)

print(words)
