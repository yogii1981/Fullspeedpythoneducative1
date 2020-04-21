# python list slicing for concise but clear sublists

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[0])  # 1st element indexed at 0
print(letters[-1])  # last element indexed at -1

print(letters[0:3])  # First 3 elements
print(letters[-3:0])  # last 3 elements

print(letters[3:])  # All elements except first 3 elements
print(letters[:-3])  # All elements except last 3 elements

print(letters[::-1])  # reversed - all elemenets starting from the last
print(letters[::-2])  # reveresed - starting from the last - every second element
