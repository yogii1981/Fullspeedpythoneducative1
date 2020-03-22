# python in a day chapter 6 question 22

# Write a program that prompts the user to enter two integers, a and b.
# The program then calculates the product of all integers between a and b inclusive
# and displays the result to the user. For instance, the program may behave as shown below
# (user input is in bold italics):
# Example 1:
# Please enter the first integer: 10
# Please enter the second integer: 13
# Product  Note: 10*11*12*13 = 17160
# Modify the program in Question 22 to satisfy the two rules below:
#  Rule 1
#  If 0 falls within a and b, it is not multiplied with the other numbers.
# For instance, if a = -3 and b = 2,
# the program performs
#
# the calculation (-3)x(-2)x(-1)x1x2 without multiplying 0 with the other integers.

#  Rule 2 If the product is smaller than -500 or greater than 500,
#  the program stops calculating and displays the message “Range Exceeded”.
#  For instance, the program may behave as shown below (user input is in bold italics):
#  Example 1: Please enter the first integer: -3 Please enter the second integer: 2


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
            if i != 0:
                product = product * i
            if product > 500 and product < -500:
                product = -1

            if product == -1:
                print('Range Exceeded')
            else:
                print(product)
        return product


productofnumbers = Productintegers()
productofnumbers.product()
