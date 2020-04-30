import math

print(math.cos(0.0))
print(math.radians(275))

"""Module"""


def myCourse(name):
    return ("My Course:" + name)


test = myCourse("Full Speed Python")
print(test)

"""Functions - Non Parameterized Function"""


def do_hello():
    print("hello")
    print("World")


do_hello()

"""Functions -Parameterized Function"""


def add_one(val):
    print("Function got value:", val + 1)
    return


add_one(1)
