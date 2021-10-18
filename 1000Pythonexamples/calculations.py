print(" Calculate the area and circumference of the rectangle")
width = 23
height = 17
area = width * height
print("The area is: ", area)

circumference = 2 * (width * height)
print("The circumference is:", circumference)

print()
print("write a script to calculate the area and circumference of the circle")


def radius(a):
    r = a
    return r


print(radius(7))

import math

areacircle = math.pi * radius(7) ** 2
print("The area of circle:", areacircle)

circumferencecircle = 2 * math.pi * radius(7)
print("The circumeference of circle:", circumferencecircle)

print()
print(" Write a script that has two numbers a and b and calculate a + b, a - b, a * b , a / b ")


def sumofinteger(a, b):
    sum = a + b
    return sum


def diffferenceofinteger(a, b):
    difference = a - b
    return difference


def multiplicationofinteger(a, b):
    multi = a * b
    return multi


def divisionofinteger(a, b):
    divis = a / b
    return divis


print()
print(sumofinteger(3, 4))
print(diffferenceofinteger(3, 4))
print(multiplicationofinteger(3, 4))
print(divisionofinteger(3, 4))

# Approach2#
print()
print("Approach 2")


def main():
    a = input("First Integer:")
    b = input("Second Integer:")
    print("The sum of two integer is", int(a) + int(b))
    print("The difference of two integer is", int(a) - int(b))
    print("The product of two integer is", int(a) * int(b))
    print("The division of two integer is", int(a) / int(b))


main()


# *** conditionals if ***

def main():
    expected_answer = "42"
    inp = input("What is the answer:")
    if inp == expected_answer:
        print("Welcome to Caba!")
    else:
        print("Go back")


# conditionals: elif

def main2():
    a = input('First number:')
    b = input('Second number:')
    if a == b:
        print('They are equal')
    elif int(a) > int(b):
        print('First number is greater than Second')
    else:
        print('Second Number is greater than First')


main2()


main()
