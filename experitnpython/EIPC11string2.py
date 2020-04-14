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

    # Write your logic here
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 400 != 0) and (year % 100 == 0):
        leap = False
    elif (year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
