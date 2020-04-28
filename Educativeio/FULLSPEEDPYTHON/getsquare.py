"""Use list comprehension to get square"""


def getSquare():
    y = [x * x for x in range(1, 11)]
    return y


firsttensquare = getSquare()
print(firsttensquare)
