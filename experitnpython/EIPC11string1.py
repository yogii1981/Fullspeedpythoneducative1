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
