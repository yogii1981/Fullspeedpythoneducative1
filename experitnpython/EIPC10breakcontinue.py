# program to use break statement to break loop execution on same condition

for i in range(10):
    if i == 7:
        print("The processing is enough...plz break")
        break
    print(i)

# program2 - break

cart = [10, 20, 30, 400, 50, 600, 70]
for item in cart:
    if item > 500:
        print("To place this order insurance is required")
        break
    print(item)
