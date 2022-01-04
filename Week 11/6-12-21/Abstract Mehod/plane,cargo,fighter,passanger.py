from abc import *
class Plane(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def carry(self):
        pass

    @abstractmethod
    def takeoff(self):
        pass

class Cargo(Plane):
    def fly(self):
        print("Not for passangers")
         def carry(self):
             print("The luggages are carried on the cargo plane")
        def takeoff(self):
            print("NO military travels here")


class goods(Plane):
    def fly(self):
        print("Passengers are taken in the fly plane")
         def carry(self):
             print("The luggages are carried on the cargo plane")
        def takeoff(self):
            print("The military units take off in their own military plane")


class fighter(Plane):
    def fly(self):
        print("Passengers are taken in the fly plane")
         def carry(self):
             print("The luggages are carried on the cargo plane")
        def takeoff(self):
            print("The military units take off in their own military plane")


obj=Cargo()
obj.fly()
obj.carry()
obj.takeoff()

obj1=goods()
obj1.fly()
obj1.carry()
obj1.takeoff()

obj2=fighter()
obj2.fly()
obj2.carry()
obj2.takeoff()
