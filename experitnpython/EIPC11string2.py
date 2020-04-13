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
