from random import randint


# def generate(length):
#     password = []
#     for i in range(length):
#         x = randint(0, 9)
#         password.append(str(x))
#
#     pwd = "".join(password)
#     print(pwd)
#
#
# length = int(input("Enter length : "))
# generate(length)


def generate2(length):
    password = ""

    for i in range(length):
        x = str(randint(0, 9))
        password += x

    print(password)


length = int(input("Enter length : "))
generate2(length)
