# chapter1

myFavNumber = 11

myFavWord = "python"

username = "Lee"
print(username)

num1 = 5
NUM1 = 7
print(num1)
print(NUM1)

# 1num = 7 + 5 ; wrong naming convention used

# a = 17
# b = 12
# a = b
# print(a)  # since "a" has been assigned the value of b , print(a) will show value of b which now also is value for a


x, y = 13, 4
print(x + y)  # add
print(x - y)  # subtact
print(x * y)  # multiply
print(x / y)  #
print(x // y)
print(x % y)  # Divides left hand operand by right hand operand and returns remainder
print(
    x ** y)  # The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −

# print the values of sum,product and r
a = 12
b = 5
sum = print(a + b)
product = print(a * b)
reaminder = print(a % b)

# print the value  after assigning 3 values.
a = 13
b = 7
c = 5
result = (a + c) * b + c - a
print(result)

# chapter3 - question10
s = 1
s = s - 3
print(s)

# question11
num = 5
num = num + 10
print(num)

# question12
t = 10
t = t + 1
t = t * 2
t = t / 5
print(t)

# question13
p, q = 12, 4
p += 3
print(p)

q **= 2
print(q)

# question14
r = 11
s = 7
r = r + s
print(r)
print(s)

# question15
d = 4
d = d + 4
d = 2 * d
d = d - 4
d = 2 * d
d = d / 4
result = d - 20
print(result)

# chapter 4
# chap4 question1
name1 = 'Jamie'
name2 = 'Aaron'.upper()
print(name2)

message = 'The names are %s and %s.' % (name1, name2)
print(message)

# chap4 question2
lang1 = 'python'
lang2 = 'java'
lang3 = 'c#'
message1 = 'The most popular programming language are %s, %s and %s.' % (lang1, lang2, lang3)
print(message1)
message2 = ' The most popular programming language are %s, $s and $s.' % (lang1, lang3, lang2)
print(message2)

# chap4 question3
num = 12
message = '%d' % (num)
print(message)

# chap4 question4
decnum = 1.72498329745
message = '%5.3f' % (decnum)  # round off to 3 digit
print(message)
message = '%7.2f' % (decnum)  # rounf off to 2 digit
print(message)

# chap4 question5
p = 111
q = 13
result = (p / q)
result1 = '%5.3f' % (result)
print(result1)

# chap4 question6
message5 = "My name is {} and I am {} year old.".format('Ironman', 18)
print(message5)

# chap4 question7
message6 = 'my fav color {}, {} and {}'.format('orange', 'blue', 'black')
print(message6)

message7 = 'my favorite colors are {1},{0} and {2}'.format('orange', 'blue', 'black')
print(message7)

# chap4 question8

student1 = "Aaron"
student2 = "Beck"
student3 = "Carol"

sentence1 = "My bests friends are {}, {} and {}".format(student1, student2, student3)
print(sentence1)

# chap4 question9
message8 = '{:7.2f},{:d} and {:d}'.format(21.3124, 12, 15)

message9 = '{1} and {0}'.format(21.3124, 12)

print(message8)
print(message9)

# chap4 question10

x1 = 12
y1 = 7
quotient = (x1 / y1)
message12 = "The result divided by {:d} by {:d} is {:7.4f} , correct to 4 decimal places".format(x1, y1, quotient)
print(message12)

# chap4 question11

number = 2.7123
number = int(number)
print(number)

# chap4 question12
s1 = 2.12431  # assign a value to variables1
s1 = str(s1)  # convert variable s1 to string
print(s1)  # print s1
print(type(s1))  # check type of s1 variable

# chap4 question13
