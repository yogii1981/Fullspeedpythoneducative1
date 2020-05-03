"""
for index in sequence:
    statement
"""

"""
For Looping through list
"""

""" find square of list values using for loop"""
l = [0, 1, 2, 3, 4, 5]
for value in l:
    print(value * value)

"""find sum of list"""
l = [0, 1, 2, 3, 4, 5]
sum = 0
for value in l:
    sum = sum + value
print(sum)

"""Loppoing using range"""

for i in range(6):
    print(i)

"""find sum of index"""
l = [0, 1, 2, 3, 4, 5]
sum = 0
for i in range(len(l)):
    i = i + i
    print(i)
    sum = sum + i
print(sum)

"""
Looping Using enumerate #
Sometimes you may need both things (indexes and values), and you can use the "enumerate" function:
"""

mylist = [1, 5, 7]

for i, value in enumerate(mylist):
    print("Index:", i, "Value:", value)
    print("index + value:", i + value)

"For loop through the string"
string = "my python is still not perfect"
for i in string:
    print("value is:", i)
