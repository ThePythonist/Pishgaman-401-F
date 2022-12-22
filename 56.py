ages = {
    "tara": 23,
    "kian": 28,
    "ali": 19,
    "maryam": 15,
    "reza": 20
}

oldest = max(ages.values())

for k, v in ages.items():
    if v == oldest:
        print(k)
        print(v)
