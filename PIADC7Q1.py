# write a program which greet user with "hello, World" message
class Greetings:

    def __init__(self, display=None):
        self.display = display


    def greetuser(self):
        self.display = ('Hello, World')
        return self.display

greetuserone = Greetings()
print(greetuserone.greetuser())