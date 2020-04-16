def len_(x):
    length = len(x)
    # print everything in a same row
    print(length, end=' ')
    return length


items = [3.14, 'moon', {}]
i = 0

while i < len_(items):
    i += 1

print(i)
