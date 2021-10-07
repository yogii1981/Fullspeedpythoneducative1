# Function call
a = str(32)
print(a)

# Math functions
import math

signal_power = 30
noise_power = 60
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)

print()
print("degree to radians")
degrees = 45
radians = degrees / 180.0 * math.pi
print(math.sin(radians))

print()
print("math sqrt")
print(math.sqrt(4.4))

print()
print("Composition")
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)

print()
print("Adding new functions")


def print_lyrics():
    print("I am lumberjack")


print(print_lyrics())

print_lyrics()

print()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# Parameters and arguments
print()


def print_twice(bruce):  # Inside the function arguments are assigned to a parameter named bruce
    print(bruce)
    print(bruce)


# print_twice('radhika')
#
# print_twice(12)
#
# print_twice('Rads' * 2)


# Variables and parameters are local
print()

line1 = 'bing ding '
line2 = "tindle kindle"


def print_twice(bruce):  # Inside the function arguments are assigned to a parameter named bruce
    print(bruce)
    print(bruce)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


cat_twice(line1, line2)

# Fruitful Functions and Void functions
print()
print("function which doesn't bring result is called void function like print_twice")
print("functipon which brings result is called fruitful functions like cat_twice")

print()

import math

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
