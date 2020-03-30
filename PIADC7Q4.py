# write a function and write a method to calculate the quotient

class Calculator:

    def ___init__(self, action=None):
        self.action = action

    def calculateQuotient(self):
        integer1 = int(input("Enter an integer1:"))
        integer2 = int(input("Enter an integer2:"))
        result = int(integer1 / integer2)
        return result


quotient = Calculator()
print(quotient.calculateQuotient())
