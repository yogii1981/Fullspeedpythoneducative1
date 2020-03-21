class User:

    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def username1(self):
        self.__username = input('What is the username?')

    def password1(self):
        self.__password = int(input("Enter a password"))

    def login(self):
        self.username1()
        self.password1()
        if self.__username == "Yogesh" and self.__password == 123456:
            print("login granted")
        else:
            print("incorrect username or password")


test = User()

test.login()
test.password = 2341234
test.login()
