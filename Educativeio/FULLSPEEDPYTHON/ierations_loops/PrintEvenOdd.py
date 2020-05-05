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

Languages = ["Python", "Java", "R"]
for x in Languages:
    if x == "Java":
        break
    print(x)

    i = 1
    while i < 7:
        print(i)
        if (i == 3):
            break
        i += 1

i = 1
while i <= 7:
    i += 1
    if (i == 3):
        continue
    print(i)
