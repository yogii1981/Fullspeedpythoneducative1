def f(a, b='b', c='c', type='T'):
    print("Input", a, b, c, type)


# print(f(1000))
# print(f(a=1000))
# print(f(a=100000,c='ccc'))
# # print(f())
# print(f(c='ccc',a=10000))
# print(f('happy','life','rich'))

print(f(actor='johny'))

"""""example1"""

wordlist = ["Pomellie", "Rome", "Venice"]
tweet = """
"The floor is Lava!"
-Everyone , Pomellie 79AD.
"""

s = tweet.split()
res = map(lambda x: x in s, wordlist)
print(list(res)[0])

# example2
d = dict([(i, i % 3) for i in range(8)])
print(d[5])

"""
The two key points in the puzzle are:
1. list comprehension
2. create dictionary from a list of tuples
With the list comprehension we create a list of tuples which looks like this:
[(0, 0), (1, 1), (2, 2), (3, 0), (4, 1), (5, 2), (6, 0), (7, 1)]
With this list we create a dictionary. In the dictionary each tuple becomes one entry.
The first value of each tuple becomes the entry‘s key and the second value becomes the entry‘s value.
As you can see in the list of tuples, key = 5 will return value 2. Therefore d[5] returns 2.
"""

# example 3


w1 = "Step"
w2 = "on"
w3 = w1 + " " + w2
print(w3)
print(w3[len(w3)::-1])
w4 = w3 + " " + w3[len(w3)::-1]
w5 = "." * 3
print(w5)
w6 = w4 + w5
w7 = ''.join(list(i for i in w6[:-2]))
print(w7)
