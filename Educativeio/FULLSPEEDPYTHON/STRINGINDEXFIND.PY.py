"""FIND INDEX OF A SPECIFIC VALUE OF A STRING"""

"""
Write your code below. It is recommended​ that you try solving the exercise yourself before viewing the solution.
"""


def findOccurence(s):
    # Write your code here
    a = s.find("b")  # find first occurrence of "b" in the string
    b = s.find("ccc")  # find first occurence  of "ccc" in the string
    return [a, b]


"""Example 2 """

str = "Python Programming"
character = "y"
character2 = "m"
str.find(character)  # find the location/index  of y in string "str"
print((str.find(character)))
print(str.find(character2))  # find the location/index  of m in string "str"

"""
The following Python code demonstrates how to find the index of a specific value in a string
"""


def findOccurence(s):
    a = s.find("b")  # find first occurrence of "b" in the string
    b = s.find("ccc")  # find first occurence  of "ccc" in the string
    return [a, b]


str = "aaabbccc"
print(findOccurence(str))
