class Shape:

    def area(self):

        print("Area of Shape")

class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        result = 3.14 * self.radius * self.radius

        print("Area of Circle:", result)

class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        result = self.length * self.width

        print("Area of Rectangle:", result)

class Triangle(Shape):

    def __init__(self, base, height):

        self.base = base
        self.height = height

    def area(self):

        result = 0.5 * self.base * self.height

        print("Area of Triangle:", result)

c1 = Circle(5)

r1 = Rectangle(10, 4)

t1 = Triangle(6, 8)

c1.area()

r1.area()

t1.area()