# write a program to find minimum of 3 numbers

a = int(input("Enter an integer:"))
b = int(input("Enter an integer:"))
c = int(input("Enter an integer:"))
if a < b and a < c:
    print("a is minimum of all integer which is", a)
elif b < a and b < c:
    print("b is minimum of all integer which is", b)
else:
    print("c is minimum of all integer which is", c)
