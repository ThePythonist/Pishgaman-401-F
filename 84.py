lines = open('words.txt').readlines()

# five_letters = []
#
# for i in lines:
#     if len(i) == 6:
#         five_letters.append(i)

five_letters = [ i for i in lines if len(i) == 6 ]

print(five_letters[:500])
