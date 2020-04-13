# replace the string with another string
s = "Learning Python is very difficult"
s1 = s.replace("difficult", "easy")
print(s1)

# splitting of strings:
s2 = "rocky mountain, this is a camp"
l = s2.split(',')
for x in l:
    print(x)

s3 = "10-12-1984"
l = s3.split('-')
for x in l:
    print(x)

# joining of strings,
s3 = ('Peter', 'John')
l1 = '-'.join(s3)
print(l1)

#  uppercase,lowercase,swapcase,title,capitalize
s4 = "This is a python"
print(s4.upper())
print(s4.lower())
print(s4.swapcase())
print(s4.title())
print(s4.capitalize())

# format with strings and using replacement
name = 'david'
age = 48
salary = 100000
print("{} at {} will make {}".format(name, age, salary))
print("{x} at {y} will make {z}".format(x=name, y=age, z=salary))

#  write a program to display the input display in string
# method1
s = input("enter a string")
print(s[::-1])

# method2

s = input("Enter some string:")
i = len(s) - 1
target = " "
while i >= 0:
    target = target + s[i]
    i = i - 1
print(target)

# write a program to reverse order of words
s = input("Enter a string:")
l = s.split()
print(s.split())
l1 = []
i = len(l) - 1
while i >= 0:
    l1.append(l[i])
    i = i - 1
output = ''.join(l1)
print(output, end=' ')

# write a program to reverse the internal content of each word

s = input("Enter a word:")
l = s.split()
l1 = []
i = 0
while i < len(l):
    l1.append(l[i][::-1])
    i = i + 1
output = ''.join(l1)
print(output)

# write a program to merge characters of 2 strings into a string by string by taking characters

s1 = input("enter first string:")
s2 = input("enter a second string:")
output = ""
i, j = 0, 0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output + s1[i]
        i += 1
    if j < len(s2):
        output = output + s2[j]
        j += 1
print(output)

# write a program to sort the character of the string and first alphabet symbols followed by numeric

s
