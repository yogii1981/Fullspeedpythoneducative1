try:
    n = int(input("Enter a number:"))
    if n <= 0:
        print('The number enter is not positive')
    else:
        factorial = 1
        while n > 0:
            factorial = factorial * n
            n = n - 1
            print(factorial)
except:
    print("You didn't enter an integer")
