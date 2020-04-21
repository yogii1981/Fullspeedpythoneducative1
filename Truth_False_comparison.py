print(True == True)
print(True != False)
print(True == False)

# "is" is true if they point to the same object

print(True is True)  # True, because there is a single "True" object
s1 = 'Lambda school rocks!'
s2 = 'Lambda school rocks!'
s3 = 'Lambda school rocks!'
print(s1 == s2)  # they are same string
print(s1 is s2)  # true ;as they live at same locations
print(s2 is s3)
print(id(s1))
print(id(s2))

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list comparison", list1 == list2)
print("list location is", list1 is list2, "hence stored at different location")

# other comparison

print(4 > 3)
print(4 < 3)
print(5 >= 1.3)
print(2 < 4j)  # Error, as comparison not supported between integer and complex number
print("complex number comparison shows", 2 + 1j > 4 + 4j)
