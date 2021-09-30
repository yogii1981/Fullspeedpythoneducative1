# lists
scores = [99, 89, 12, 34, 56]
print(type(scores))
print(scores)

# position or referencing of list item in lists
print(scores[0])
print(scores[-1])
print(scores[0:3])
print(scores[-1::-1])  # starting from the last to the first in the reverse order
# print(scores[7]) # this should give error as there is no list item at the given position (out of index)

# Looping through a list
scores = [99, 89, 12, 34, 56]
for score in scores:
    print("The {} is greater than 75".format(score))
print("Done")

# Add a list item to list
names = ["Raj", "Amit", "Ketan"]
names.append("Anuj")
print(names)

# insert a list item to certain position in the list

names = ["Raj", "Amit", "Ketan"]
new_person = "Sahil"
names.insert(1, new_person)
print(names)
names[0] = "Anjali"  # changing an item in a list
print(names)

# combining lists
names = ["Raj", "Amit", "Ketan"]
names1 = ["Anjali", "Rita"]
names.extend(names1)
print(names)

# remove the item from list
names2 = ["Raj", "Amit", "Ketan"]
names2.remove("Amit")
print(names2)

letters = ["A", "B", "C", "B", "R", "C", "A"]
letters.remove("C")  # only one "C" is removed
print(letters)

#in order to remove all "C"  use while loop
letters1 = ["A", "B", "C", "B", "R", "C", "A"]
c_in_letters = letters1.count("C")  # Count the item "C" in the list
print(c_in_letters)

while c_in_letters > 0:  # While the list has count of item = "C"
    if c_in_letters == 0:  # if count of item "C" == 0
        print(letters1, "No C found")
    else:
        letters1.remove("C")  # remove the item "C" once
        c_in_letters += 1
        print(letters1)

# Counting how many times items appear in the list
grades = ["A", "B", "C", "D", "E", "E", "A", "E", "D", "B"]
# count for item "E
e_ingrades = grades.count("E")
# look for item E to count
look_for = "D"
e_ingrades = grades.count(look_for)
print("There are  " + str(grades.count("A")) + " " + "A grades in the list")
print("There are  " + str(grades.count("B")) + " " + "B grades in the list")
print("There are  " + str(grades.count("C")) + " " + "B grades in the list")
print("There are  " + str(e_ingrades) + " " + "E grades in the list")
print("There are  " + str(look_for) + " " + "D grades in the list")
