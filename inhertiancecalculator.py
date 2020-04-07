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


class Calculateadvance(Calculator):
    def __init__(self, integer1=None, integer2=None, squareroot=None):
        Calculator.__init__(self, integer1, integer2)
        self.squareroot = squareroot

    def squarerootcalculation(self):
        n = 2
        self.enternumber()
        print(self.integer2, self.integer1)
        if self.integer1 != 0 and self.integer2 != 0:
            self.integer1 = self.integer1 ** 0.5
            self.integer2 = self.integer2 ** 0.5
            print(self.integer1, self.integer2)


specialcalculation = Calculateadvance()
specialcalculation.squarerootcalculation()
