"""Remove sublist"""


def removeSublist():
    l = [1, 4, 9, 10, 23]
    l.remove(4)
    l.remove(9)
    return l


newlist = removeSublist()
print(newlist)
