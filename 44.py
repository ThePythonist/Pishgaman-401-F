football = ["arman", "atrin", "artin", "javad"]
basketball = ["artin", "mamad", "javad", "hassan"]

# for i in football:
#     if i in basketball:
#         eshterak.append(i)
#
# print(eshterak)

eshterak = [i for i in football if i in basketball]
print(eshterak)
