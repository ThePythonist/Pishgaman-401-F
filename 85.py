lines = open('words.txt').readlines()
# five_letters = ""
# for i in lines :
#     if len(i) == 6 :
#         five_letters += i
#
# open("five-letters.txt", "w").write(five_letters)
# print("Done")

five_letters = [i for i in lines if len(i) == 6]
output = "".join(five_letters)
open("five-letters.txt", "w").write(output)
print("Done")
