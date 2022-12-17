n = int(input("Entry : "))
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors)

# if divisors == [1, n]:
#     print("Prime!")
# else:
#     print("Not Prime")

if len(divisors) == 2:
    print("Prime!")
else:
    print("Not Prime")
