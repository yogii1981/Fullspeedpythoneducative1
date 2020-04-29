def getsquare():
    l1 = [x * x for x in range(0, 21, 2) if x % 3 != 0]
    return l1


getresult = getsquare()
print(getsquare())
