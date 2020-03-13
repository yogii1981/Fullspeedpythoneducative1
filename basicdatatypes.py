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

# n = int(input("Enter a value: "))  # input a number
#
#
# def checkparity(n):
#     result = (n % 2)
#     return result
#
#
# test = checkparity(10)
# print(test)

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code
evenOdd(2)
evenOdd(3)

x = int(input("Enter a value:"))

evenodd(x)


# Find values within a range or not
# Given an inRange(x,y) function, write a method that determine whether a pair (x,y) falls in
# the range ( x < 1/3 < y)/ Essentially you will be implementing the body aof a function that takes two numbers
# x and y and returns True if x <1/3 < y ; otherwise it returns False.

# x = int(input("Enter a value:"))
# y = int(input("Enter a value"))
# def inrange(x, y):
#     if x < 1/3 < y:
#         print(True)
#     else:
#         print(False)

x = 2
y = 3


def inRange(x, y):
    return (x < 1 / 3 < y)


# find a minumum between two numbers

def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)


# enter two random numbers and find maximum between two

# def maximum(n1, n2):
#     if n1 > n2:
#         return n1
#     else:
#         return n2
#
#
# n1 = int(input("Enter a value: "))
# n2 = int(input("Enter a value: "))
#
# result = maximum(n1, n2)
# print(result, "is a maximum number")


# find the cube of first 10 numbers

# def cube(n):
#     n = 0
#     for i in range(0,n+1):
#         num = n * n * n
#     num = n  # changing the value inside the function
#     print(num)
#     return n
#
# cubetest = cube(n)


# def firstten():
#      for i in range(10):
#          print(i)
#          return result
#
# result = firstten()
# print(result)

# How to read multiple values from the keyboard in a single line:

a, b = [int(x) for x in input(" Enter 2 numbers:").split()]
print(" Product is:", a * b)


# Try to guess the output of following code.
def swap(x, y):
    temp = x;
    x = y;
    y = temp;


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)
