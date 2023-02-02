number = input("Enter your phone number : ")

if number[0] == "0":
    number = number.replace("0", "+98", 1)
    print(number)
else:
    number = f"+98{number}"
    # number = "+98"+number
    print(number)
