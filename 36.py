odds = list()

for i in range(1, 50):
    if i % 2 != 0:
        # odds.append(i)
        odds += [i]
print(odds)
