# write a program to read 2 from key board and print sun

# x = int(input("Enter an integer1:"))
# y = int(input("Enter an integer2:"))
# print("The Sum:", x + y)

# print() with variables numbers of arguments.
a, b, c = 10, 20, 30
print("The values are :", a, b, c)

a, b, c = 10, 20, 30
print(a, b, c, sep=',')
print(a, b, c, sep=':')

# print() with end attribute
a = 10
b = 5
c = 6
print("integerb: %i and integerc: %i are smaller than integera:%i" % (b, c, a))

# print () with replacement operator {}
name = "teckze"
salary = 10000
gf = "ritika"
print("{x} has girlfiend:{y} and he has salary:{z}".format(x=name, y=gf, z=salary))
print("{0} has girlfiend:{1} and he has salary:{2}".format(name, gf, salary))
