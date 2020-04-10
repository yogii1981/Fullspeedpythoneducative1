# write a program using a inhertiance method to add squareroot,cuberoot,cubea nd sqaure calculation capability in
# the exisiting calculator class when the user enter 2 integers.

class Calculator:

    def __init__(self, integer1=None, integer2=None):
        self.integer1 = integer1
        self.integer2 = integer2

    def enternumber(self):
        self.integer1 = int(input("Enter an integer1:"))
        self.integer2 = int(input("Enter an integer2:"))
        return (self.integer1, self.integer2)

    def addition(self):
        resultaddition = int(self.integer1 + self.integer2)
        return resultaddition

    def subtraction(self):
        resultsubtraction = int(self.integer1 - self.integer2)
        return resultsubtraction

    def multiplication(self):
        resultmultitiplication = int(self.integer1 * self.integer2)
        return resultmultitiplication

    def division(self):
        resultdivision = int(self.integer1 / self.integer1)
        return resultdivision


class Calculateadvance(Calculator):
    def __init__(self, integer1=None, integer2=None, squareroot=None, cuberoot=None):
        Calculator.__init__(self, integer1, integer2)
        self.squareroot = squareroot
        self.cuberoot = cuberoot

    def squarerootcalculation(self):
        n = 2
        # self.enternumber()
        print(self.integer1, self.integer2)
        if self.integer1 != 0 and self.integer2 != 0:
            result_calcsquareroot1 = self.integer1 ** 0.5
            result_calcsquareroot2 = self.integer2 ** 0.5
            print("Squareroot is {}, {}".format(result_calcsquareroot1, result_calcsquareroot2))

    def cuberootcalculation(self):
        # n = 3
        # self.enternumber()
        print(self.integer1, self.integer2)
        if self.integer1 != 0 and self.integer2 != 0:
            result_calccuberoot1 = self.integer1 ** (1. / 3)
            result_calccuberoot2 = self.integer2 ** (1. / 3)
            print("cuberoot is {}, {}".format(result_calccuberoot1, result_calccuberoot2))


    def squarecalculation(self):
        # self.enternumber()
        print(self.integer1, self.integer2)
        result_square1 = self.integer1 ** 2
        result_square2 = self.integer2 ** 2
        print("square is {}, {}".format(result_square1, result_square2))

    def cubecalculation(self):
        # self.enternumber()
        print(self.integer1, self.integer2)
        result_cube1 = self.integer1 ** 3
        result_cube2 = self.integer2 ** 3
        print("cube is {}, {}".format(result_cube1, result_cube2))


specialcalculation = Calculateadvance()
specialcalculation.enternumber()
specialcalculation.squarerootcalculation()
specialcalculation.cuberootcalculation()
specialcalculation.squarecalculation()
specialcalculation.cubecalculation()
