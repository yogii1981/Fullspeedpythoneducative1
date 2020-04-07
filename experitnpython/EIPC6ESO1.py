c = 10
d = 10
print(c is d)

a1 = "teckze"
b1 = "teckze"
print(id(a1))
print(id(b1))
print(a1 is b1)

list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
print(id(list1))
print(id(list2))  # list are stored at seperate location
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)
