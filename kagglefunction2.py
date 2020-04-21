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

""" the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. 
For the sake of their friendship, any candies left over would be smashed. 
For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

Below is a simple function that will calculate the number of candies to smash for 
any number of total candies.

Modify it so that it optionally takes a second argument representing the number 
of friends the candies are being split between. If no second argument is provided, 
it should assume 3 friends, as before."""


def to_smash(total_candies, number_of_candidates):
    """ return the number of candies to be smashed after equal distribution between 3 friends"""
    return total_candies % number_of_candidates


print(to_smash(127, 4))
