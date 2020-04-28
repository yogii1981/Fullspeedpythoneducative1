def showeven():
    y = [x for x in range(1, 21) if (x % 2 == 0)]
    return y


displayevennumbers = showeven()
print(displayevennumbers)


def showodd():
    y1 = [x for x in range(1, 21) if (x % 2 != 0)]
    return y1


displayoddnumbers = showodd()
print(displayoddnumbers)

"""Given the participants' score sheet for your University Sports
 Day, you are required to find the runner-up score. You are given 
  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains . The second line contains an array  
 of  integers each separated by a space.
Constraints
Output Format

Print the runner-up score."""

if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))
    a = set(arr)
    b = list(a)
    b.sort()
    print(b[-2])

"""
Given the names and grades for each student in a 
Physics class of  students, store them in a nested list 
and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the
 first line contains a student's name, and the second line contains
  their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics;
 if there are multiple students, order their names alphabetically and print
  each one on a new line.
"""

# if __name__ == '__main__':
#     arr = []
#     scrarr =[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    arr = arr + [[name, score]]
    scrarr = scrarr + [score]
b = sorted(list(set(scrarr)))
b = b[1]
for a, c in sorted(arr):
    if c == b:
        print(a)
