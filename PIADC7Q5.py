# write a function and write a method to calculate the quotient to include the
# error handling using try and except "-1" when invalid numbers or strings are entered

class Calculator:

    def ___init__(self, action=None):
        self.action = action

    def calculateQuotient(self):
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            result = int(integer1 / integer2)
            return result
        except:
            return -1


quotient = Calculator()
print(quotient.calculateQuotient())
