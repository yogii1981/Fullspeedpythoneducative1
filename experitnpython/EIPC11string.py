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

# a program in access each character forward and backward

s1 = input("enter the word:")
i = 0
for x in s1:
    print("The character of the string in forward is {} and index is {}".format(x, i))
    i = i + 1
for x in s1:
    print("The character of the string is backward is {} and index is {}".format(x, i - len(s1)))
    i = i - 1

# find() : s.find(substring) : returns index of first occurence of the given substring.If it is not available then we
# will get -1
s = "learning Python is very easy"
print(s.find("Python"))  # 9
print(s.find("Java"))  # -1
print(s.find("r"))  # 3
print(s.rfind("r"))  # 21
print(s.find("P", 3, 10))

# index() method:
s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found")

# program to display all positions of substring in a given main string
s = input("Enter main string:")
subs = input("enter sub string")
flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs, pos + 1, n)
    if pos == -1:
        break
    print("Found at position", pos)
    flag = True
if flag == False:
    print("Not Found")
