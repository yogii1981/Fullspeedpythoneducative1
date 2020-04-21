print(1, 2, 3, sep='<')

""" greet function"""


def greet(who="Colin"):
    print("Hello,", who)


greet()
greet(who="kaggle")

""" multiply function"""


def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """call fn on arg"""
    return fn(arg)


def square_call(fn, arg):
    return fn(fn(arg))
    """call fn on the result of calling fn on arg"""


print(call(mult_by_five, 1), square_call(mult_by_five, 1))

"""Program to  find the remainder"""


def mod(x):
    """return the remainder of x after dividing by 5"""
    return x % 5


print(mod(33))

"""Program to find the exact quotient """


def quotient(x, y):
    """return the quotient value"""
    quotientvalue = x / y
    return (quotientvalue)


print(quotient(16, 3))

"""Program to print quotient with some remainder"""


def modu(x, y):
    qv = x // y
    return qv


print(modu(16, 3))

"""Program to print remainder"""


def modu1(x, y):
    qv = x % y
    return qv


print(modu1(16, 3))
