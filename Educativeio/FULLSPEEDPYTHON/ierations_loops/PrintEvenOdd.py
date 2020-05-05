"""Using For loop"""


def printEvenodd(list):
    for i in list:
        if (i % 2 == 0):
            print("Even Number:", i)
        else:
            print("Odd Number:", i)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
printEvenodd(l)

"""using While loop"""


def printEvenOdd(n):
    while (n > 0):
        if (n % 2 == 0):
            print("Even number:", n)
        else:
            print("Odd number:", n)
        n = n - 1


printEvenOdd(10)
