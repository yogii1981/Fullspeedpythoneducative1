for i in range(10):
    userInputtest = input('Enter a number %d:' % (i + 1))

    # Assign the first user input
    # to largest and smallest
    if i == 0:
        largest = userInputtest
        smallest = userInputtest
    # from the second user input onwards,
    # compare user input with
    # current largest and smallest
    elif float(userInputtest) > float(largest):
        largest = userInputtest
    elif float(userInputtest) < float(smallest):
        smallest = userInputtest

print('The smallest number is %s' % (smallest))
print('The smallest number is %s' % (largest))
