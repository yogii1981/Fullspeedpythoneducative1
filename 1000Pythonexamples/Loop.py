# Loops: For-inn and while
# For in - to iterate over well defined list of values (characters, range of numbers and shopping list etc.)
# While - repeat an action till conditiion is met or stopped being met

# For loop in strings
print("program1")
txt = "Hello world!"
for char in txt:
    print(char)

print("program2")
numb1 = range(1, 200)
for i in numb1:
    print(i in numb1)

print("program3")
for i in range(3, 7):
    print(i)

# For - In loop - early break
print("program4")
txt = 'Hello World'
for c in txt:
    if c == " ":
        break
    print(c)

# For - In loop - parts using continue
print("program5")
txt = 'Hello World'
for c in txt:
    if c == " ":
        continue
    print(c)

print("Program1 print a space between 'hello and 'world' but program 5 doesn't ")
