# look for item and positions in the list
grades = ["A", "B", "C", "L", "E", "K", "A", "E", "D", "B"]

# what you want to look for
# look_for = "E"
# e_index = grades.index(look_for)
for n, i in enumerate(grades):
    if i == "E":
        print("The position of E is ", n)
