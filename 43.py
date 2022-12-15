football = ["arman", "atrin", "artin", "javad"]
basketball = ["artin", "mamad", "javad", "hassan"]
eshterak = []

# for i in football:
#     for j in basketball:
#         if i == j:
#             eshterak.append(i)
#
# print(eshterak)

for i in football:
    if i in basketball:
        eshterak.append(i)

print(eshterak)
