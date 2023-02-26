from random import randint

number = randint(0, 10)
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} chances left")

    try:
        guess = int(input("Guess the number : "))

        if guess == number:
            print("You won!")
            break
        elif guess > number:
            print("Try smaller")
        else:
            print("Try bigger")

        chances -= 1

    except ValueError:
        print("Invalid input. Try again")

if chances == 0:
    print(f"Game over! The number was {number}")
