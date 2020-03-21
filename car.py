class car:
    def __init__(self, pMake, pModel, pColor, pPrice):
        self.make = pMake
        self.model = pModel
        self.color = pColor
        self.__price = pPrice  # adding two underscore makes "price" variable private and no one can update it anymore outside the class

    def __str__(self):
        return 'Make = %s, Model = %s, Color = %s, Price = %s' % (self.make, self.model, self.color, self.__price))

        def selectColor(self):
            self.color = input('What is the new color? ')

        def calculateTax(self):
            priceWithTax = 1.1 * self.price
            return priceWithTax

    myFirstCar = car("Honda", "Civic", "White", 15000)
    print(myFirstCar.make)
    print(myFirstCar.__str__())
    myFirstCar.price = 18000
    print(myFirstCar.__str__())

    myFirstCar.selectColor()
    print(myFirstCar.__str__())
