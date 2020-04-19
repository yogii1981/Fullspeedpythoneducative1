# write a calculator program where user enters two numbers
# and also use try and except to perform error handling
# in this program has to enter the integer again and again and
# not an efficent method


class Calculator:


    def ___init__(self, action=None):
        self.action = action

    def calculateQuotient(self):
        """
        this method will

        :return: return statment will be w
        """
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            result = int(integer1 / integer2)
            return result
        except:
            return -1

    def addition(self):
        """
        :param pa: it could be any number between 1 to 5
        :return: jsflksjf
        """
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            resultaddition = int(integer1 + integer2)
            return resultaddition
        except:
            return -1

    def subtraction(self):
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            resultsubtraction = int(integer1 - integer2)
            return resultsubtraction
        except:
            return -1

    def multiplication(self):
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            resultmuliplication = int(integer1 * integer2)
            return resultmuliplication
        except:
            return -1

    def remainder(self):
        try:
            integer1 = int(input("Enter an integer1:"))
            integer2 = int(input("Enter an integer2:"))
            resultremainder = int(integer1 % integer2)
            return resultremainder
        except:
            return -1


calculate = Calculator()
print(calculate.calculateQuotient())
print(calculate.multiplication())
print(calculate.addition())
print(calculate.subtraction())
print(calculate.remainder())
