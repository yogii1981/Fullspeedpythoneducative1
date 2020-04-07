# Program to display the message to the user.

class Greetings:

    def __init__(self, message=None):
        self.mesaage = message

    def displayMessage(self):
        input_message = input("Enter a message:")
        return input_message


greetwithmessage = Greetings()
print(greetwithmessage.displayMessage())
