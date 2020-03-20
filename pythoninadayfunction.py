# # write a program to greetuser
#
# if __name__ == '__main__':
#     def greetuser():
#         print("Hello World")
#
# greetuser()


#
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0:
        if year % 100 == 0:
            print(leap)

    return leap


year = int(input())
print(is_leap(year))
