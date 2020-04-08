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

# continue to use "Continue"- this program will continue to print the numbers whenever the number divided by 2
# and remainder is zero

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Write a program which doesn't process items when price is more than certain number and print message for them
cart = [10, 20, 30, 400, 50, 600, 700, 9000]
for item in cart:
    if item > 500:
        print("Can't process this item:", item)
        continue
    print(item)
