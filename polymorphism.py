# one method and multiple implementation

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangele is:", self.length * self.breadth)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of sqaure:", self.side ** 2)


shape = [Rectangle(4, 5), Square(8)]
shape[0].area()
shape[1].area()
