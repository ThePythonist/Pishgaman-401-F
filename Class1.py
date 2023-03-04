class Car:
    def __init__(self, name, color, model, hp):
        self.name = name
        self.color = color
        self.model = model
        self.horsepower = hp

    def brreak(self):
        print("Eeeeeeh")

    def horn(self):
        print("Booooogh")

    def tell_info(self):
        print(self.color)
        print(self.model)
        print(self.horsepower)


# Instance ( Shey )
samand = Car("Samand", "Black", "1401", 500)
bmw = Car("BMW", "Blue", "2023", 2000)
print(samand.name)
samand.tell_info()
print('-------------------------------')
print(bmw.name)
bmw.tell_info()
