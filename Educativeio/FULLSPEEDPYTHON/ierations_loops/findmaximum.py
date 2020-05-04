def findMaximum(list):
    maximum = list[0]  # first value is assumed as maximum
    for number in list:  # loop which check whether any value in the loop is greater than first value or not
        if number > maximum:
            maximum = number
    return maximum


l = [1, 2, 3, 4]
print(findMaximum(l))
