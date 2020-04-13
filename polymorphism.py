# One method and multiple imp

class Shape:
    def __init__(self):
        self.s1 = 0

    def area(self):
        print("No generic implemntation")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self)
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle is: ", self.length * self.breadth)


class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self)
        self.side = side

    def area(self):
        print("Area of square is: ", self.side ** 2)


shape = [Rectangle(4, 5), Square(8)]
shape[0].area()
shape[1].area()
