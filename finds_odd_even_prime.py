# number1 = int(input("enter a number:"))
# if number1 > 1:
#     for i in range(2,number1):
#         if (number1 % i) !=0:
#             print("{} is a prime number".format(number1))
#             return 0
#         else:
#             print("{} is a not a prime number".format(number1))
#             if (number1 % 2) ==0:
#                  print("{} is even".format(number1))
#             else:
#                 print("{} is odd".format(number1))


class Typeofnumber:

    def __init__(self, number1=None):
        self.number1 = number1

    def primenumber(self):
        if self.number1 > 1:
            for i in range(2, self.number1):
                if (self.number1 % i) != 0:
                    print("{} is a prime number".format(self.number1))
                    return 0
                else:
                    print(("{} is not a prime number".format(self.number1)))

    def evenorodd(self):
        if (self.number1) % 2 == 0:
            print("{} is a even number".format(self.number1))
        else:
            print("{} is an odd number".format(self.number1))


testresult = Typeofnumber(6)
testresult.primenumber()
testresult.evenorodd()
