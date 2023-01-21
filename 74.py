def factorial(x):
    if x == 1:
        # return x
        return 1
    else:
        return x * factorial(x - 1)


while True:
    entry = input("Enter any number to see the factorial : ")
    try:
        entry = int(entry)
        if entry > 0:
            print(factorial(entry))
            break
        elif entry == 0:
            print("Factorial of zero is 1")
            break
        elif entry < 0:
            print("The factorial doesnt exist")
            break
    except ValueError or SyntaxError:
        print("Invalid input. Try again")
