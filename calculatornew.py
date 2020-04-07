from pythoninaday import pythoninadayfunction


class Calculatornew:

    def ___init__(self, integer1=None, integer2=None):
        self.integer1 = integer1
        self.integer2 = integer2

    def enternumber(self):
        self.integer1 = int(input("Enter an integer1:"))
        self.integer2 = int(input("Enter an integer2:"))
        return (self.integer1, self.integer2)

    def calculateQuotient(self):
        result = int(self.integer1 / self.integer2)
        return result

    def addition(self):
        resultaddition = int(self.integer1 + self.integer2)
        return resultaddition

    def subtraction(self):
        resultsubtraction = int(self.integer1 - self.integer2)
        return resultsubtraction

    #
    # def multiplication(self):
    #     resultmuliplication = int(self.integer1 * self.integer2)
    #     return resultmuliplication

    def remainder(self):
        resultremainder = int(self.integer1 % self.integer2)
        return resultremainder


def main():
    calculate = Calculatornew()

    calculate.enternumber()
    print(calculate.addition())
    print(calculate.subtraction())
    print(calculate.remainder())
    print(calculate.calculateQuotient())


if __name__ == '__main__':
    main()
    newValue = pythoninadayfunction.valueYear()
    print(pythoninadayfunction.is_leap(newValue))
