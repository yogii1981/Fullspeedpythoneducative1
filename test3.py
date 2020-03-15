# Given an inRange(x,y) function, write a method that determine whether a pair (x,y) falls in
# the range ( x < 1/3 < y)/ Essentially you will be implementing the body aof a function that takes two numbers
# x and y and returns True if x <1/3 < y ; otherwise it returns False.

x = int(input("Enter a value:"))
y = int(input("Enter a value"))


def inrange(x, y):
    if x < 1 / 3 < y:
        print(True)
    else:
        print(False)

    return True if x < 1 / 3 < y else False


print(inrange(x, y))
