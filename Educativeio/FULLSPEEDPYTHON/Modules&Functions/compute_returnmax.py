""" Write a program to find maximum between two numbers
Method-1 without using the in-built max function"""


def calcmax(a, b):
    if a == 0 and b == 0:
        print("Error: both are equal")
    if a < b:
        print("{} is greater than {}".format(a, b))
    else:
        print("{} is greater than {}".format(b, a))


calcmax(10, 6)

"""Write a program to find maximum between two numbers
Method-2  using the in-built max function
"""


def findMax(x, y):
    max2 = max(x, y)
    return max2


print(findMax(10, 12))


"""Write a program to find maximum between n numbers
Method-3  using the in-built max function"""

# def findMax1(list1):
#     # Assume first number in list is largest
#     # initially and assign it to variable "max"
#     max = list1[0]
#
#     # Now traverse through the list and compare
#     # each number with "max" value. Whichever is
#     # largest assign that value to "max'.
#     for x in list1:
#         if x > max:
#             max = x
#
#             # after complete traversing the list
#     # return the "max" value
#     return max
#
#     # Driver code
#
#
# list1 = [10, 20, 4, 45, 99]
# print("Largest element is:", findMax1(list1))


"""Write a program to find maximum between n numbers
Method-3 user enters the numbers and condition"""


def findMax2():
    # number in a list

    # creating empty list
    list2 = []

    # asking number of elements to put in the list
    num = int(input("Enter number of elements in the list: "))

    # iterating till num to append elements in list
    # need to count the elements entered
    count = 0
    for i in range(1, num + 1):
        elements = int(input("Enter elements: "))
        list2.append(elements)  # appending list
        count += 1
        if count == num:
            max3 = max(list2)
            return max


print(findMax2())

