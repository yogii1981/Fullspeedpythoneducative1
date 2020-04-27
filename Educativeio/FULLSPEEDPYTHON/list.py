"example of list"

l = [1, 2, 3, 4,
     5]  # l = list name, 1,2,3,4,5 = list element , l[0] , l[1] = will give index of list element 1 and 2 respectively
print(l)
print(l[0])

"""creating a sublist from a list"""
l1 = l[0:3]
print(l1)

"""Operation on list"""
l2 = l + l1
print("Add", l2)
l3 = l * 2
print("mul", l3)
l4 = l - l1
# print("sub",l4)   """This will give error"""

""" use the following piece of code on python """
l = [1, 3, 4, 8, 20]
for val in l:
    print(val)

""" use the following piece of code on python and adding to each value """
l = [1, 3, 4, 8, 20]
for val in l:
    val = val + 3
    print(val)

""" use the following piece of code on python and adding to 3 each element and then removing fr """
l = [1, 3, 4, 8, 20]
for val in l:
    val = val + 3
    previous = val
    previous = previous - 5
    #   print(val)
    print(previous)
