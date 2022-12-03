n = int(input("Enter any number : "))

# if n == 0:
#     print("Zero")
# elif n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

if n % 2 == 0 and n != 0:
    print("Even")
elif n == 0:
    print("Zero")
else:
    print("Odd")
