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

# Modules
import sys

print(sys.executable)


# A Main Function
def main():
    print("Hello")
    print("Hello")


print("before")
main()
print("after")


# Conditional Main

def main():
    print("Hello World")


if_name_ == "_main_":
main()

# Conditionals: If - else


print("Example1")


def main():
    expected_answer = 42
    inp = int(input("What is the answer?"))

    if inp == expected_answer:
        print("Welcome to the club")
    else:
        print("Membership not found")


main()

print("Example2")


def main():
    a = input("First number:")
    b = input("Second Number:")

    if int(b) == 0:
        print("Cannot divide by 0")
    else:
        print("Diving", a, "by", b)
        print(int(a) / int(b))


main()


# Conditionals: If else

def main():
    a = input('First number:')
    b = input('Second number:')

    if a == b:
        print("Two inputs are equal")
    else:
        if int(a) > int(b):
            print(a + " is bigger than" + b)
        else:
            print(a + " is smaller than" + b)


main()


# Write a scrpt that will ask for the sides of the rectangle and print out the area
# provide error messages if either of the sides is negative.


def main():
    length = int(input("Enter the length of the rectangle:"))
    width = int(input("Enter the width of the rectangle"))
    if length >= 0 or width >= 0:
        area_of_the_rectangle = int(length * width)
        print(area_of_the_rectangle, "square meter")
    else:
        print("Value entered is invalid")


main()


# Write a script that accepts 3 numbers and an operator (+,-,/,*), and prints the result of the operations
print("Option-A")
def calc():
    a = float(input("Enter an integer:"))
    b = float(input("Enter another integer:"))
    op = input("Operator (+-*?/):")

    if op == '+':
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a / b
    else:
        print("Invalid operator:'{}'".format(op))

    print(res)
    return


calc()

print("Option-B")


def calc():
    a = input("Number1:")
    b = input("Number2:")
    op = input("Operator(+-*/):")
    command = a + op + b
    print(command)
    res = eval(command)
    print(res)
    return


calc()

# Pseudo random number
import random

a = random.random()
print(a)

# Fixed random number
random.seed(37)
a = random.random()
print(a)

# print out the random number - rolling dice - rand range

import random

print(1 + int(6 * random.random()))
print(random.randrange(1, 7))

# Random Choice- randomly pic from the choice provided
import random

letters = "abcdfehsfkgflsfsdgah"
print(random.choice(letters))  # pick one of the letters

fruits = ["Apple", "Banana", "Citrus", "Durian", "elderberry"]
print(random.choice(fruits))

# Pick random whole number 1 to 20
# user will guess number
# computer let user know whether the guess number is greater or smaller than random generated number
import random

a = random.randrange(1, 21)
inp = int(input("Enter a guess number between 1 to 21:"))
if a < inp:
    print("Guessed number is greater than random generated number")
elif a > inp:
    print("Guessed number is smaller than random generated number")
elif a == inp:
    print("You guessed it right!")
elif inp < 1 or inp > 21:
    print(" The number is out of range")
print(a, "is a random generated number")

# exercise to select 3 random fruits which should be unique

fruits = ['apple', 'banana', 'peach', 'orange', 'durian', 'papaya']
salad = random.sample(fruits, 3)
print(salad)

# short circuit fixed
#
#
# def check_money():
#     return  money > 1000000
#
# def check_salary():
#     salary += 1
#     return salary >= 1000
#
# while True:
#     if check_money() or check_salary():
#         print("I can live")

# Triple quaoted Springs

text = """ first row
second row
third row"""

print(text)

text1 = "Hello World"
text2 = """Hello 
World"""

print("Length of text1:", len(text1))

print("Length of text2:", len(text2))
