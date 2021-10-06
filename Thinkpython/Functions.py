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
