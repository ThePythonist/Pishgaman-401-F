scores = {
    "riazi": 16,
    "zaban": 20,
    "shimi": 17,
    "arabi": 9,
    "farsi": 12,
}

for x, y in scores.items():
    if y >= 10:
        print("Passed :", x)
    else:
        print("Failed :", x)

moadel = sum(scores.values()) / len(scores.values())
print(moadel)
