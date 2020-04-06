# python program to ullustrate the use of arguments (*values in this case)
# which multiplies all the values given to a function as a parameter
def multiplyall(*values):
    mul = 1

    print(values)
    print("Type= ", type(values))

    for i in values:
        mul = mul * i

    return mul


ans = multiplyall(12, 16, 14)
print(ans)
