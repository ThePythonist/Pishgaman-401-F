word = "Python"
d = {}

for i in range(len(word)):
    d.setdefault(word[i],i)
print(d)

