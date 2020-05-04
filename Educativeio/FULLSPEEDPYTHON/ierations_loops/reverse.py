""" Write the program which displays the elements of the list in the reverse order"""


def reverse(list):
    length = len(list)

    s = length

    new_list = [None] * length

    for item in list:
        s = s - 1
        new_list[s] = item
    return new_list


list = [1, 2, 3, 4, 5]
print(reverse(list))
