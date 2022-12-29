# def prime(n):
#     divisors = [i for i in range(1, n + 1) if n % i == 0]
#     # if len(divisors) == 2:
#     #     print("Prime!")
#     # else:
#     #     print("Not Prime")
#     print("Is prime") if len(divisors) == 2 else print("Is not prime")
#
#
# n = int(input("Entry : "))
# prime(n)


def prime(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return "Prime" if len(divisors) == 2 else "Not Prime"


n = int(input("Entry : "))
print(prime(n))
