"""Write a program which check when one element is divided by other then remainder is zero"""


def checkdivisiblity(a, b):
    if a % b == 0:
        print("{} is divisible by {}".format(a, b))
    elif b % a == 0:
        print("{} is divisible by {}".format(b, a))
    elif a % b != 0 and b % a != 0:
        print("{} and {} is not divisible by each other".format(a, b))
    else:
        print("Warning: there is an error and check your input")


checkdivisiblity(15, 4)
