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
