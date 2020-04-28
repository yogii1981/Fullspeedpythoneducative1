"""Use list comprehension to get square"""


def getSquare():
    y = [x * x for x in range(1, 11)]
    return y


firsttensquare = getSquare()
print(firsttensquare)


def getCube():
    y1 = [x * x * x for x in range(1, 11)]
    return y1


firsttencube = getCube()
print(firsttencube)
