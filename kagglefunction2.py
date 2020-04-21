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
