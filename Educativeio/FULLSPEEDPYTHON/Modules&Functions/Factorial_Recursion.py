"""
Recursion is when a ​function calls itself again and again until it reaches the base condition.
"""
"""
factorial(n) = 0                     #base case
factorial (n) = n * factorial(n-1)   # recursive function

"""


def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial(n - 1))


print("Factorial:")
print(factorial(5))
