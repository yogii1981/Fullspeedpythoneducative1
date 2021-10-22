# Loops: For-inn and while
# For in - to iterate over well defined list of values (characters, range of numbers and shopping list etc.)
# While - repeat an action till conditiion is met or stopped being met

# For loop in strings
txt = "Hello world!"
for char in txt:
    print(char)

numb1 = range(1, 200)
for i in numb1:
    print(i in numb1)

for i in range(3, 7):
    print(i)

# For - In loop - early break

txt = 'Hello World'
for c in txt:
    if c == " ":
        break
    print(c)
