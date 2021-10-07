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
