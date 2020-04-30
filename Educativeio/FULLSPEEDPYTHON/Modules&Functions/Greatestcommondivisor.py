"""Method 1"""
# import math
# def findGCD(a,b):
#     return math.gcd(a,b)
#
# print(findGCD(36,12))


"""Method2"""


def findGCD(a, b):
    if a == 0 and b == 0:
        print("warning: GCD called with both arguments equal to zero")
        return 0

    # checking for negative number
    if a < 0: a = -a
    if b < 0: b = -b

    if b == 0: return a
    if a == 0: return b

    return findGCD(b, a % b)


print(findGCD(12, 18))
