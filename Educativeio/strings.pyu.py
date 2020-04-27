hi = "hello"
hi += " Word"
print(hi)

"""Integer and string can't be added"""
hi = "hello"
hi += 4
# print(hi)
"""outcome: This will give an error- can only concatenate str (not "int") to str"""

"""Integer and string multiplication"""

hi = "hello"
hi *= 3
print(hi)
"""" outcome will repeat the string 3 times"""

"""
# Problem Statement #
Given a getStr() function, write the necessary sequence of operations to transform the
 string (containing three literals) in such a way that every literal is tripled​ respectively."""


def getstr(s):
    strlen = 0
    s = s[:1] + s[0] + s[1:]
    s = s[:1] + s[0] + s[1:]
    s = s[:3] + s[3] + s[3:]
    s = s[:3] + s[3] + s[3:]
    s = s[:6] + s[6] + s[6:]
    s = s[:6] + s[6] + s[6:]

    # update the length of string
    return [s, strlen]


print(getstr("abc"))

"""
Write your code below. It is recommended​ that you try solving the exercise yourself before viewing the solution.
"""


def findOccurence(s):
    # Write your code here
    a = s.find("b")  # find first occurrence of "b" in the string
    b = s.find("ccc")  # find first occurence  of "ccc" in the string
    return [a, b]
