"""
this function will show you how to calaulate
least difference between different numbers
and maximum difference between the values entered
"""


class Difference:

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def entervalues(self):
        self.a = int(input("enter a value a:"))
        self.b = int(input("enter a value b:"))
        self.c = int(input("enter a value c:"))
        return self.a, self.b, self.c

    def least_difference(self):
        diff1 = abs(self.a - self.b)
        diff2 = abs(self.b - self.c)
        diff3 = abs(self.a - self.c)
        return min(diff1, diff2, diff3)

    def max_difference(self):
        diff1 = abs(self.a - self.b)
        diff2 = abs(self.b - self.c)
        diff3 = abs(self.a - self.c)
        return max(diff1, diff2, diff3)


finddifference = Difference()
print(finddifference.entervalues())
print(finddifference.least_difference())
print(finddifference.max_difference())
