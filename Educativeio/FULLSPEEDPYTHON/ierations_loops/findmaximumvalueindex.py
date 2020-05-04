def findMaxvalueindex(list):
    maximum = list[0]  # first value is assumed as maximum
    index = 0
    for i, value in enumerate(list):
        # loop which check whether any value in the loop is greater than first value or not
        if value > maximum:
            maximum = value
            index = i
    return ["Index is {} and maximum value is {}".format(index, maximum)]


l = [1, 2, 3, 4]
print(findMaxvalueindex(l))
