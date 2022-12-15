items = [True, 12, 4.3, 5, "Farzad", 7, False]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        print("Is a number")
        numbers.append(i)
    else:
        print("Is not a number")

print(numbers)
