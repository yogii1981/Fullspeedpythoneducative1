# a program to sort the characters of the string and first alphabet symbols followed by numeric values

s = input("Enter some string:")
s1 = s2 = output = ""
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x
print(output)

#  a program to replace numeric number by the previous alphabet as no of times that number
s = input("Enter a string:")
output = " "
for x in s:
    if x.isalpha():
        output = output + x
        previous = x
    else:
        output = output + previous * (int(x) - 1)
print(output)

# write a program to perform following activity:
# input = "a4k3b2"
# output = "aeknbd"
s = input("Enter an integer:")
output = " "
for x in s:
    if x.isalpha():
        output = output + x
    previous = x
else:
    output = output + chr(ord(previous) + int(x))
print(output)

#  a program to remove duplicates characters from the given string
# input: ABCDABBEFGGGAAAA
# output: ABCDEFG


# program 1

s = 'terfinx'
s = ''.join(sorted(list(s)[3:7] + list(s)[0:3]))
print(s)


# program 2
def func(x):
    return x + 1


f = func
print(f(2) + func(2))


# leap year
def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0):
        # Note that in your code the condition will be true if it is not..
        leap = True
    elif (year % 100 == 0) and (year % 400 != 0):
        leap = False
    elif (year % 400 == 0):
        # For some reason here you had False twice
        leap = True
    else:
        leap = False

    return leap


#
a = 'hello'
b = 'world'
print(a, b, sep=' Python', end="!")

text = "# Is this a comment?"
print(text)

nums = [1, 2, 3]
nums.append(nums[:])
print(len(nums))
print(nums)

print(list(range(3)))

5 // -3.0 * 4


# test this
def contextSensitiveWishes(religion):
    if religion in ['C']:
        a, b = zip(*[('h', 'c'), ('a', 'm')])
    elif religion in ['J']:
        a, b = zip(*[('h', 'c'), ('a', 'b')])
    else:
        a, b = zip(*[('g', 'd'), ('r', 'a')])
    print(''.join(a) + " " + ''.join(b))


contextSensitiveWishes("B")

print(50 // 11

words = ['cat', 'mouse']
for w in words:
    print(len(w))

x = 1
if x < 0:
    x = 0
print('Negative to zero')
elif x == 0:
print('Zero')
elif x == 1:
print('Single')
else:
print('More')

a = ['mary', 'had', 'a', 'lamb']
for i in range(len(a)):
    print(a[i])


def swap():
    b, a = a, b


a, b = 1, 2
swap()
print(b - a)


def bubblesort(lst):
    for passesleft in range(len(lst) - 1, 0, -1):
        for index in range(passesleft):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


l = [66, 89, 49, 62, 9, 53, 59]
print(bubblesort(l))

word = 'galaxy'
print(word[2:60])

l = [[]]

if l:
    print(True)
else:
    print(False)

cubes = [1, 8, 27]
cubes.append(4 ** 3)
print(cubes)

# write a program to calculate the price

item_prices = [('apple', 0.45), ('banana', 0.75), ('kiwi', 0.5), ('orange', 0.8)]
prices = [price for item, price in item_prices]
print(sum(prices))

# write a program to find outcome

import re

string = 'Coconut'

c1 = re.search('C', string)
c2 = 'C' in string[0]
c3 = string.startswith('C')
c4 = 'C' == string[:1]

result = c1 and c2 and c3 and c4

print(result)
# outcome = true

# write a program to find outcome
omega3_table = {"Salamon": 2260, "Hering": 1729, "Sardiness": 1480, "Flaxseeds": 53400, "Egss": 400}
y = max(omega3_table,
        key=lambda x: omega3_table[x])
print(y)

#
s1 = "Ronaldo is better than Messi"

print(s1.find("Ronaldo", 5))
print(s1.find("Football"))
print(s1.find("Messi", 5, 100))


#

def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y


print(factorial(6))
print(factorial(4))
print(factorial(6) / factorial(4))


#
def ping(i):
    if i > 0:
        return pong(i - 1)
    else:
        return "0"


def pong(i):
    if i > 0:
        return ping(i - 1)
    else:
        return "1"


print(ping(14))

# write a program to find outcome

import re

matches = re.findall('\.', 'Coconut')
result = len(matches)
print(result)

# print the outcome of this program
t1 = 5 + 2 == 7
f1 = 2 - 1 > 3

r = t1 or False
r = r and True and f1

print(r)

# print the outcome of this program

import re

text = 'Spiderman'
matches = re.findall('...', text)
result = len(matches[2])
print(result)

# print the outcome of this program

meal_1 = "meat"
meal_2 = "Flaxseeds"
meal_3 = "Marsmallows"

healthyFoods = ["kale", "Apples", "Strawberry", "Banana", "Flaxseeds"]


def isHealthy(food):
    return food in healthyFoods


m_1 = isHealthy(meal_1)
m_2 = isHealthy(meal_2)
m_3 = isHealthy(meal_3)

print((not m_1 or m_2) and (meal_2 is "Flaxseeds") and isHealthy("Kale"))

# print the outcome of this program
friends = ["Alice", "Bob", "Ann"]
friends.pop()
print(friends.pop(0))
