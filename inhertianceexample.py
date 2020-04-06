class Mobile:
    def __init__(self, screen, color, memory, radio):
        self.screen = screen
        self.color = color
        self.memory = memory
        self.radio = radio

    def printMobileDetail(self):
        print("Screen is: ", self.screen)
        print("Color is: ", self.color)
        print("Memory is: ", self.memory)
        print("Radio is: ", self.radio)


class Iphone(Mobile):
    def __init__(self, screen, color, memory, radio, os):
        Mobile.__init__(self, screen, color, memory, radio)
        self.os = os

    def printIphoneDetail(self):
        self.printMobileDetail()
        print("Os is: ", self.os)


class AndroidMobile(Mobile):
    def __init__(self, screen, color, memory, radio, os, camera, liquidtouch):
        Mobile.__init__(self, screen, color, radio, memory)
        self.os = os
        self.camera = camera
        self.liquidtouch = liquidtouch

    def printAndroidMobileDetail(self):
        self.printMobileDetail()
        print("Os is: ", self.os)
        print("Camera is: ", self.camera)
        print(("Liquidtouch is:", self.liquidtouch))


phoneObject = Iphone("1080P", "Black", "4GB", "4G", "iOS")
phoneObject.printIphoneDetail()

phoneObject2 = AndroidMobile("1080P", "Black", "4GB", "4G", "ketchup", "120px", "yes")
phoneObject2.printAndroidMobileDetail()
