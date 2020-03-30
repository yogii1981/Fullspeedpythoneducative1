class Greetings:

    def __init__(self, name=None):
        self.name = name

    def username(self):
        inputname = input("enter a username:")
        return inputname

    def greetuser(self):
        self.name = (self.username(), 'Hello World')
        return self.name


greetuserone = Greetings()
print(greetuserone.greetuser())
