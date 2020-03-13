# Mathematical calculation

# n1 = int(input("Enter a number:"))  # input enter a number 1
# n2 = int(input("Enter a number:"))  # input enter a number 2
#
#
# def mathop(n1, n2):  # define a function "mathop" and has two variables n1, n2
#     classic_division = n1/n2
#     floor_division = n1//n2
#     modulus = n1 % n2
#     power = n1 ** n2
#     return [classic_division, floor_division, modulus, power]
#
#
# test = mathop(n1, n2)  # calling the mathop function
# print(test)


# Check Parity of a Number

n = int(input("Enter a value: "))  # input a number


def checkparity(n):
    result = (n % 2)
    return result


test = checkparity(10)
print(test)
