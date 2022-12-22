info = {
    "name": "roya",
    "age": 30,
    "job": "software engineer",
    "company": "digikala",
    "city": "mashhad",
}

entry = input("Enter any key to search : ")

# if entry in info:
#     print("Founded :", info[entry])
# else:
#     print("Not Found")

try:
    print("Founded :", info[entry])
except KeyError:
    print("Not Found")
