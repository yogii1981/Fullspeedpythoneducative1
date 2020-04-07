# write a program to find maximum of 3 numbers

a = int(input("Enter an integer:"))
b = int(input("Enter an integer:"))
c = int(input("Enter an integer:"))
if a > b and a > c:
    print("a is maximum of all integer which is", a)
elif b > a and b > c:
    print("b is maximum of all integer which is", b)
else:
    print("c is maximum of all integer which is", c)
