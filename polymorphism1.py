class Contact:
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def input(self):
        list_1 = []
        list_2 = []
        list_3 = []
        n = int(input("enter number of contacts:"))
        for i in range(0, n):
            self.name = input("Enter a name:")
            self.phone = int(input("Enter a 10 digit phone number:"))
            self.email = input("Enter a valid email address:")
            # self.address = input("enter a valid address")
            list_1.append([self.name])
            list_2.append([self.phone])
            list_3.append([self.email])
            dict1 = dict(zip(list_1, list_2))  # to convert 3 list into a dictionary
            dict2 = dict(zip(list_1, list_3))
            return dict1, dict2


class Address:
    def __init__(self, name, phone, email, address=None):
        Contact.__init__(self, name, phone, email)  # (inherit contact, address)
        self.address = address  # property = address


def input1(self):
    list_4 = []
    n1 = input("enter number of contacts for which address has to be entered:")
    for i in range(0, n):
        self.address = input("Enter a address:")
        list_4 = list_4.append([self.address])
        dict3 = dict(zip(self.list_1, list_4))
        return dict3


class Search:
    def __init__(self, name, phone, email, address, search):
        Contact.__init__(self, name, phone, email)
        Address.__init__(self, address)
        self.search = search


def searchlogic(self):
    name2 = input("enter a name to be found:")
    if name2 in dict1 and name2 in dict2 and name2 in dict3:
        print(name2, dict1[name], dict[name], dict[name])


searchcheck = Contact(john)
searchcheck.()
searchcheck.inp

# create a method call "search" - whatever name user enter , you look up the name in the phone book
# and display  phone, email and address
