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
