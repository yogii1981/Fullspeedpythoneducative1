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
message2 = ' The most popular programming language are %s, %s and %s.' % (lang1, lang3, lang2)
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
userInput = 12
userInput = int(userInput)
print(userInput)

# chap4 question14
myList = [1, 2, 3, 4, 5, 6]
print(myList[1])
print(myList[-2])

# chap4 question15
testScores = [10, 11, 12, 13]
print(testScores[3])
print(testScores[-1])

# chap4 question16
myListnew = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist1 = myListnew
myList2 = myListnew[3:6]
myList3 = myListnew[:5]
myList4 = myListnew[2:]
myList5 = myListnew[1:7:2]
myList6 = myListnew[::3]
print(myListnew)
print(mylist1)
print(myList2)
print(myList3)
print(myList4)
print(myList5)
print(myList6)

# chap4 question17
q17 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sliceA = q17[2:8]  # print values from 13 till 18
print(sliceA)
sliceB = q17[2:9:3]  # print values 13,16,19
print(sliceB)

# chap4 question18

emptyList = []
emptyList.append = (12, 5, 9, 11)
print(emptyList)

# chap4 question19
q19 = [1, 2, 3, 4, 5]
q19[2] = 10
print(q19)

# chap4 question20
q20 = ['A', 'B', 'C', 'D', 'E']
del q20[:3:2]
print(q20)

# chap4 question21
daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat']
myDay = daysOfWeek[2]
print(myDay)

# chap4 question22

# nameAgeDict = {'John':12,'Mathew':15,'Aaron':13,'John':14,'Melvin':10}  # same "John" is used as the dictionary key twice


# chapter5 question 2 (use %d) method
a = 10
b = 4
sub = a - b
# print(a, "-", b, "=", a - b)
result = print("%d  - %d =  %d" % (a, b, sub))

# chapter5 question 3 (use format method)
a = 10
b = 4
sub = a - b
result = print("{} - {} = {}".format(a, b, sub))

# chapter5 question 4

# Determine the output withour running code

print(''' Date: \nJan11, 2019 Time: \n1.28pm Venue:\nConvention Center Number of Pax:\n30''')

# chapter5 question 5

print('This is a single quotation (\')mark and this is a double (") mark.')

# chapter6 question 6
# The code below shows the last few lines of a program:
day = {1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday', 7: 'Monday'}
venue = {1: 'Tokyo to Osaka', 2: 'Osaka', 3: 'Kyoto', 4: 'Kyoto to Nara', 5: 'Nara to Osaka', 6: 'Osaka to Tokyo',
         7: 'Tokyo'}
print('Day 1 (%s): %s' % (day[1], venue[1]))
print('Day 2 (%s): %s' % (day[2], venue[2]))
print('Day 3 (%s): %s' % (day[3], venue[3]))
print('Day 4 (%s): %s' % (day[4], venue[4]))
print('Day 5 (%s): %s' % (day[5], venue[5]))
print('Day 6 (%s): %s' % (day[6], venue[6]))
print('Day 7 (%s): %s' % (day[7], venue[7]))

# chapter5 question7

num1 = input("Enter an integer:")
num2 = input("Enter an integer:2")
print("you entered", num1, "and", num2)

# chapter5 question8
in1 = input("Enter a value:")
in2 = input("Enter a value:")
in1 = int(in1)
in2 = int(in2)
average = ((in1 + in2) / 2)
print('The average is %.3f' % (average))

# chapter5 question9
name = input("What is your name:")
favNum = input('Hi %s, "What is your favorite number?:' % (name))
print('%s\'s favorite number is %s.' % (name, favNum))

# chapter5 question10

cities = {'Chicago': 'USA', "Los Angeles": "USA", "New York": "USA", "Osaka": "Japan", "Tokyo": "Japan",
          "Shanghai": "China"}

print('cities: Chicago, Los Angeles, New York, Osaka, Tokyo,Shanghai')
print()

city = input("Enter your city from the list above:")
print('%s is located in %s.' % (city, cities[city]))

# Task
# Read an integer . For all non-negative integers , print . See the sample for details.
#
# Input Format
#
# The first and only line contains the integer, .
#
# Constraints
#
#
# Output Format
#
# Print  lines, one corresponding to each .
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if 1 <= n <= 20:
            print(i * i)
        else:
            print("NONE")

# chapter5 question11

userInput1 = input("Please enter 5 numbers, separated by commas:")
inputList = userInput1.split(',')
print('\nYou entered %s,%s,%s,%s,$s.' % (inputList[0], inputList[1], inputList[2], inputList[3], inputList 4]))
print('The sum is %d' % (
            int(userInput1[1]) + int(userInput1[2] + int(userInput1[3]) + int(userInput1[4]) + int(userInput1[5])))

# chapter6 question1

a = print(2 > 5)
b = print(9 < 11)
c = print(7 >= 3)
d = print(8 <= 8)
e = print(10 != 12)
f = print(6 == 3)
g = print(4 > 2 and 7 != 9)
h = print(3 > 1 and 9 == 9 and 1 > 2)
i = print(2 > 3 or 5 > 1)

# chapter6 question2
num = 5

if num == 1:
    print('num is 1')
elif num == 2:
    print('num is 2')
else:
    print('num is neither 1 nor 2'')    # this will be result as num is 5

    # chapter6 question3
    userInput2 = int(input("Enter a value: "))

    if userInput2 < 0:
        userInput2 = userInput2 * (-1)
    print("User input was negative number")
    print(userInput2)
    elif 0 == userInput2:
    print("You entered zero")
    else:
    print('userInput2 is a positive')

    # chapter6 question 4

    testScore = int(input("Enter a test score between 0 and 100 :"))


def displaygrade(testScore):
    if 70 <= testScore <= 100:
        print("A")
    elif 60 <= testScore <= 69:
        print("B")
    elif 50 <= testScore <= 59:
        print("C")
    elif 0 <= testScore <= 49:
        print("Fail")
    else:
        print("Invalid")


print(displaygrade(testScore))

# using OOP

# class grades:
#
#     def __init__(self,testScore):
#         self.testScore = testScore
#         self.testScore = int(input("Enter a testscore:"))
#
#     def displaygrade(testScore):
#         if 70 <= self.testScore <= 100:
#             print("A")
#         elif 60 <= self.testScore <= 69:
#             print("B")
#         elif 50 <= self.testScore <= 59:
#             print("C")
#         elif 0 <= self.testScore <= 49:
#             print("Fail")
#         else:
#             print("Invalid")
#
# subjectgrade = grades()
# subjectgrade.displaygrade()
# print(subjectgrade.testScore)


# chapter6 question 5
num = 5
print('orange juice' if num == 5 else 'peanut butter')

# chapter6 question6
num1 = int(input("Enter an integer: "))
print("Even" if num1 % 2 == 0 else "Odd")
# if num1 % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# chapter6 question7
myNumbers = [1, 21, 12, 45, 2, 7]
for i in myNumbers:
    print(i)

# chapter6 question8
marks = [12, 4, 3, 17, 20, 19, 16]
sum = 0
for i in marks:
    sum = sum + i

print(sum)

# chapter6 question9
# Given that classRanking = ['Jane', 'Peter', 'Michael', 'Tom'], use a for loop and the enumerate() method to display the following output:
# 1      Jane
# 2      Peter
# 3      Michael
# 4      Tom

classRanking = ['Jane', 'Peter', 'Michael', 'Tom']
n = 0
for number in classRanking:
    n = n + 1
    print(n, '     ', number)

# chapter6 question10
testScores1 = {'Aaron': 12, 'Betty': 17, 'Carol': 14}
for i in testScores1:
    print(i, 'scored', testScores1[i], 'marks.')
print(testScores1)

# chapter6 question11
# Determine the output of the following code without running the code:

ages = {'Abigail': 7, 'Bond': 13, 'Calvin': 4}
for i, j in ages.items():
    print('%s\t%s' % (j, i))

# chapter6 question12

message = 'Happy Birthday'
for i in message:
    if (i == 'a'):
        print('@')
    else:
        print(i)

# chapter6 question13
# A
for i in range(10):
    print(i)

# B
for i in range(2, 5):
    print(i)

# C
for i in range(4, 10, 2):
    print(i)

# chapter6 question14
i = 0
while i < 5:
    print('The value of i = ', i)
    i = i + 1

# chapter6 question 15
# determine the output of the following code without running code:
i = 5
while i > 0:
    if i % 3 == 0:
        print(i, 'is the multiple of 3')
    else:
        print(i, 'is not a multiple of 3')

    i = i - 1

# chapter6 question 16
userInput5 = int(input("enter a number: or End to Exit:"))
while userInput5 != "END":
    print(userInput5)
    userInput5 = input('Enter a number or END to exit:')

    print('Goodbye')

# chapter6 question 17
sum = 0
userInput6 = int(input("enter a  positive number  or -1 to Exit:"))
while userInput6 != -1:
    sum += userInput6
    print('Sum = ', sum)
    print()
    userInput6 = int(input('Enter a positive number or -1 to exit:'))

    print('Goodbye')

# chapter6 question 18
sum = 0
userInput6 = int(input("enter a  positive number  or -1 to Exit:"))
while userInput6 != -1:
    if userInput6 <= 0:
        print('You entered a non positive number')
    else:
        sum += userInput6
    print('Sum = ', sum)
    print()
    userInput6 = int(input('Enter a positive number or -1 to exit:'))
    print("Goodbye")

# chapter6 question 19

p = int(input("enter an number of rows :"))
q = int(input("enter a number of asterik:"))

for i in range(p):
    for j in range(q):
        print('*', end=' ')
    print()

# test program
a = "A"
b = "B"
print(a)
print(b)

# By default, the print() function adds a new line at the end of its output.
# If you do not want that to happen, you have to pass in end = '' to the print() function.
# This will remove the new line. Note that '' is made up of two single quotes, not a single double qiote
#

b = "B"
print("A", end=' ')
print("B", end=' ')

# chapter6 question 20

short_message = input("Enter a message:")
j = 0  # count of a

for i in short_message:
    if j == "a":
        j = j + 1
        if j <= 3:
            print('@', end=' ')
        else:
            print("A", end=' ')
    else:
        print(i, end=' ')
print()

# chapter6 question 21
for i in range(10):
    userInputtest = input('Enter a number %d:' % (i + 1))

    # Assign the first user input
    # to largest and smallest
    if i == 0:
        largest = userInputtest
        smallest = userInputtest
    # from the second user input onwards,
    # compare user input with
    # current largest and smallest
    elif float(userInputtest) > float(largest):
        largest = userInputtest
    elif float(userInputtest) < float(smallest):
        smallest = userInputtest

print('The smallest number is %s' % (smallest))
print('The smallest number is %s' % (largest))










# Datacamp - Introduction to python
p = [[3, "A", 5], [2, 6, "B"], ["C", "D", "E"]]
# print output [2,6]
print(p[1][0:2])

import numpy as np

store = np.array(["X", "Z", "Z", "Z"])
cost = np.array([7, 1, 9, 4])
select_cost = cost[store == "X"]
print(select_cost)

# what is the output of this code?
p = ['x', 'k']
q = p + ['z']
print(q)

# complete the code to return the output
# import numpy as np
#
# store = np.array([0, 9, 0, 1])
# cost = np.array([82, 82, 73, 73])
# np_cols = ((store, cost))
# print(np_cols)

# Operator	Name	Description
# a + b	Addition	Sum of a and b
# a - b	Subtraction	Difference of a and b
# a * b	Multiplication	Product of a and b
# a / b	True division	Quotient of a and b
# a // b	Floor division	Quotient of a and b, removing fractional parts
# a % b	Modulus	Integer remainder after division of a by b
# a ** b	Exponentiation	a raised to the power of b
# -a	Negation	The negative of a


# p = 27
# q = 10
# add = p + q
# subtract = p - q
# multiplication = p * q
# truedivision = p / q
# floordivision = p // q
# moudul = p % q
# print(add)
# print(subtract)
# print(multiplication)
# print(truedivision)
# print(floordivision)
# print(moudul)
