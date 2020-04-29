"""Sum of first n natural number"""
#
# def squaresum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + (i * i)
#
#     return sum
#
# print(squaresum(10))
#
#
#
# """sum of square of first n number"""
#
# # method1
#
# def even():
#     for i in range(10):
#         if i % 2 == 0:
#             continue
#         print('i= ', i)
#
#
# def squaresum():
#     sum = 0


# # Python program to print Even Numbers in a List

# list of numbers
# list1 = [10, 21, 4, 45, 66, 93]
# num = 0
#
# # using while loop
# while(num < len(list1)):
#
#     # checking condition
#     if num % 2 == 0:
#        print(list1[num], end = " ")
#
#     # increment num
#     num += 1


# method2

# def evenSquareSum():
#     even = [x * x for x in range(0, 21, 2)]
#     return sum(even)
#
#
# print(evenSquareSum())


"""Method3"""


def squareeven():
    sum = 0
    for i in range(1, 21):
        if (i % 2) == 0:
            square = i * i
            sum = sum + square
    return sum


printsquareeven = squareeven()
print(printsquareeven)
