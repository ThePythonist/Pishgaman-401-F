numbers = []

for i in range(3):
    entry = input("Entry : ")

    try:
        entry = int(entry)
        numbers.append(entry)

    except ValueError:
        pass

print(numbers)
