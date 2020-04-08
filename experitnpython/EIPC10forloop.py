# program to print characters present in the given strings
s = "python book"
for i in s:
    print(i)

# program to print characters present in the given strings and adding a comma to separate character
s = "python book"
for i in s:
    print(i, end=',')

# To print characters present in string index wise:
s = input("Enter your string:")
i = 0
for x in s:
    print("The character present at", i, "index is:", x)
    i = i + 1

# To print Hello 10 times
for x in range(10):
    print("test")

# To display numbers from 0 to 10
for x in range(0, 11):
    print(x)

# To display the odd numbers between 0 to 21
for x in range(21):
    if (x % 2 != 0):
        print(x)

# to display the number from 10 to 0 in descending order
for x in range(10, 0, -1):
    print(x)

# to display the sum of integers in list

list = eval(input("Enter list:"))
sum = 0
for x in list:
    sum = sum + x
print("The sum is sum %s" % (sum))
