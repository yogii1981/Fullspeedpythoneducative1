# conditional statement
# If condition
# if-else condition
# If-elif-else


# program to find biggest among two numbers

n1 = int(input("enter number1:"))
n2 = int(input("enter number2:"))
if n1 > n2:
    print("n1:%s is greater than n2:%s" % (n1, n2))
else:
    print("n2:%s is greater than n1:%s" % (n2, n1))

# program to find biggest among three numbers

n1 = int(input("enter number1:"))
n2 = int(input("enter number2:"))
n3 = int(input("enter number3:"))
if n1 > n2 and n1 > n3:
    print("n1:%s is greater than n2:%s, n3:%s" % (n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print("n2:%s is greater than n1:%s, n3:%s" % (n2, n1, n3))
else:
    print("n3:%s is greater than n1:%s, n2:%s" % (n3, n1, n2))
