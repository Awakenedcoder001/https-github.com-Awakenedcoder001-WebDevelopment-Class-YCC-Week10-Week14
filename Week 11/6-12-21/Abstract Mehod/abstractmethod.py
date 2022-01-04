from abc import *
class Food:
    @abstractmethod
    def taste(self):
        pass
        print("Food has a smell")

    @abstractmethod
    def apperance(self):
        pass
        print("Food has to look good")

class Drinks:
    @abstractmethod
    def taste(self):
        pass
        print("Juice needs taste")

    @abstractmethod
    def fluidity(self):
        pass
        print("juice needs to be in liquid")


obj=Drinks()
obj.apperance()
obj.taste()
obj.fluidity()