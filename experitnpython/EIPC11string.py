s = 'david'
print(s[0])
print(s[-2])

# a program to accept some string from the keyword and
# display its character by indexwise(both positive and
# negative index)

s = input("Enter some string:")
i = 0
for x in s:
    print("The character present at positive index {} and at negative index {} is {}".format(i, i - len(s), x))
    i = i + 1
