# replace the string with another string
s = "Learning Python is very difficult"
s1 = s.replace("difficult", "easy")
print(s1)

# splitting of strings:
s2 = "rocky mountain, this is a camp"
l = s2.split(',')
for x in l:
    print(x)

s3 = "10-12-1984"
l = s3.split('-')
for x in l:
    print(x)

# joining of strings,
s3 = ('Peter', 'John')
l1 = '-'.join(s3)
print(l1)

#  uppercase,lowercase,swapcase,title,capitalize
s4 = "This is a python"
print(s4.upper())
print(s4.lower())
print(s4.swapcase())
print(s4.title())
print(s4.capitalize())
