class Calculator:
    integer1 = 16
    integer2 = 9

    def ___init__(self, integer1, integer2):
        self.integer1 = integer1
        self.integer2 = integer2

    # def enternumber(self):
    #     self.integer1 = int(input("Enter an integer1:"))
    #     self.integer2 = int(input("Enter an integer2:"))
    #     return (self.integer1,self.integer2)

    def addition(self):
        resultaddition = int(self.integer1 + self.integer2)
        return resultaddition

    def subtraction(self):
        resultsubtraction = int(self.integer1 - self.integer2)
        return resultsubtraction


class Calculateadvance(Calculator):
    def __init__(self, integer1, integer2, squareroot=None):
        Calculator.__init__(self, integer1, integer2)
        self.squareroot = squareroot

    def squarerootcalculation(self):
        n = 2
        if self.integer1 != 0 and self.integer2 != 0:
            self.integer1 = self.integer1 ** 1 / n
            self.integer2 = self.integer1 ** 1 / n
            print(self.integer1, self.integer2)


calculateregular = Calculator()
# calculateregular.enternumber()
print(calculateregular.addition())

specialcalculation = Calculateadvance()
print(specialcalculation.squarerootcalculation())
