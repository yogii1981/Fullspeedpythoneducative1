def isSorted(list):
    flag = 0
    i = 1
    while i < len(list):
        if (list[i] < list[i - 1]):  # compare with the previous element
            flag = 1
        i += 1

    if (not flag):
        return True
    else:
        return False


l = [9, 12, 5, 6, 7, ]
print(isSorted(l))
