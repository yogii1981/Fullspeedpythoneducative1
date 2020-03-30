# chapter 6 question 26
# the factorial of a number is denoted by n!
n = int(input("Enter a number:"))
if n <= 0:
    print('The number enter is not positive')
else:
    factorial = 1
    while n > 0:
        factorial = factorial * n
        n = n - 1
        print(factorial)
