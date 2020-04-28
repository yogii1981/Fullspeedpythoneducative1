"""You have been provided with some starter code and a
return statement that allows you to return the sublists.
 Don’t worry about these statements right now; we will
 be covering these in detail later.
"""


def getSublist():
    l = [1, 4, 9, 10, 23]
    l1 = l[0:3]  # sublist from index 0 to 3
    l2 = l[3:]  # sublist from 3 uptil end
    return [l1, l2]


[l1, l2] = getSublist()
print(l1)
print(l2)
