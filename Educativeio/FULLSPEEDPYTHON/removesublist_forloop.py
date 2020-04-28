"""Remove sublist"""


def removeSublist():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    for element in l2:
        l1.remove(element)
    return l1


newlist = removeSublist()
print(newlist)
