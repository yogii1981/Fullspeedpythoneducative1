def showeven():
    y = [x for x in range(1, 21) if (x % 2 == 0)]
    return y


displayevennumbers = showeven()
print(displayevennumbers)


def showodd():
    y1 = [x for x in range(1, 21) if (x % 2 != 0)]
    return y1


displayoddnumbers = showodd()
print(displayoddnumbers)
