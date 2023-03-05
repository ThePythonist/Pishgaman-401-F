# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# a = A()
# b = B()
#
# b.say_goodbye()
# b.say_hello()


class Father:
    def __init__(self, address, eyecolor, familyname):
        self.address = address
        self.eyecolor = eyecolor
        self.familyname = familyname

    def say_hello(self):
        print("Hello")


class Child(Father):
    def __init__(self, address, eyecolor, familyname, name, haircolor):
        super().__init__(address, eyecolor, familyname)
        self.name = name
        self.haircolor = haircolor

    def say_goodbye(self):
        print("Goodbye")


pedar = Father("Azadi Street", "Black", "Ahmadi")
pesar = Child("Azadi Street", "Black", "Ahmadi", "Arshia", "Brown")
print(pedar.address)
print(pesar.haircolor)
