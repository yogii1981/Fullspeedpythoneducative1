# def len_(x):
#     length = len(x)
#     # print everything in a same row
#     print(length, end = ' ')
#     return length
#
#
# items = [3.14, 'moon', {}]
# i = 0
#
# while i < len_(items):
#     i += 1


# # print the outcome
# s1 = "AAA"
# s2 = "BBBB"
#
# s = list(s2)
# for i, c in enumerate(s1):
#     s.insert(i * 2, c)
# print("".join(s))




# print the outcome
matrix = [
    (0, 1, 1),
    (2, 1, 1),
    (-1, 0, 3),
]

d = [row[col] for col, row in enumerate(matrix)]

print(d)
