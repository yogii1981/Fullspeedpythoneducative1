# python in a day chapter 6 question 24

# The code below leads to an infinite loop.
# Try modifying the code using the break keyword to exit the loop when users enter -1.

while 0 == 0:
    userInput = input('Press any key to continue or -1 to exit: ')
    if userInput == -1:
        break

print('You entered', userInput)
