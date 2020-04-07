# python in a day chapter 6 question 22

# Write a program that prompts the user to enter two integers, a and b.
# The program then calculates the product of all integers between a and b inclusive
# and displays the result to the user. For instance, the program may behave as shown below
# (user input is in bold italics):
# Example 1:
# Please enter the first integer: 10
# Please enter the second integer: 13
# Product  Note: 10*11*12*13 = 17160
#


# class Productintegers:
#
#     def __init__(self, integer1=None, integer2=None):
#         self.integer1 = integer1
#         self.integer2 = integer2
#
#     def firstintegerentered(self):
#         self.integer1 = int(input("Enter an integer1:"))
#         return self.integer1
#
#     def secondintegerenetered(self):
#         self.integer2 = int(input("Enter an integer2:"))
#         return self.integer2
#
#     def product(self):
#         product = 1
#         for i in range(self.integer1, self.integer2):
#             product = product * i
#
#
# productofnumbers = Productintegers()
# # productofnumbers.firstintegerentered()
# # productofnumbers.secondintegerenetered()
# productofnumbers.product()


class Productintegers:

    def __init__(self, integer1=None, integer2=None):
        self.integer1 = integer1
        self.integer2 = integer2

    def firstintegerentered(self):
        self.integer1 = int(input("Enter an integer1:"))
        return self.integer1

    def secondintegerenetered(self):
        self.integer2 = int(input("Enter an integer2:"))
        return self.integer2

    def product(self):
        product = 1
        for i in range(self.firstintegerentered(), self.secondintegerenetered() + 1):
            product = product * i
        return product


productofnumbers = Productintegers()
print(productofnumbers.product())
