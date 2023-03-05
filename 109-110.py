from math import pi


class Shape:
    def __init__(self, l=0, w=0, r=0):
        self.length = l
        self.width = w
        self.radius = r

    def rectangle_area(self):
        print(f"Rectangle area is {self.width * self.length} ")

    def rectangle_perimeter(self):
        print(f"Rectangle perimeter is {self.width + self.length * 2} ")

    def circle_area(self):
        print(f"Circle area is {self.radius * self.radius * pi} ")

    def circle_perimeter(self):
        print(f"Circle area is {self.radius * 2 * pi} ")


while True:
    shape = input("Choose a shape (1:Rectangle 2:Circle) : ")
    if shape == "1":
        l = int(input("Enter length : "))
        w = int(input("Ente width : "))

        rectangle = Shape(l=l, w=w)
        rectangle.rectangle_area()
        rectangle.rectangle_perimeter()
        break
    elif shape == "2":
        r = int(input("Enter radius : "))

        circle = Shape(r=r)
        circle.circle_area()
        circle.circle_perimeter()
        break
    else:
        print("Invalid Option. Choose 1 or 2")
